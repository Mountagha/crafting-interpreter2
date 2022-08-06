#include <stdlib.h>

#include "chunk.h"
#include "memory.h"
#include "vm.h"

void initChunk(Chunk* chunk) {
    chunk->count = 0;
    chunk->capacity = 0;
    chunk->lineCapacity = 0;
    chunk->lineCount = 0; // line information need to grow differently than code.
    chunk->code = NULL;
    chunk->lines = NULL;
    initValueArray(&chunk->constants);
}

void freeChunk(Chunk* chunk) {
    FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
    FREE_ARRAY(int, chunk->lines, chunk->lineCapacity);
    freeValueArray(&chunk->constants);
    initChunk(chunk);
}

static int isLineAdded(Chunk *code, int line) {
    //code->lines is an array of {number_occurence}{line_number}
    // hence the double increment to jump only through lines number.
    for (int i = 0; i<code->lineCount; i += 2) {
        if (code->lines[i] == line) return i;
    }
    return -1;
}


void writeChunk(Chunk* chunk, uint8_t byte, int line) {
    // the code array and the lines array are grown differently
    // and the line array use the run-length encoding to avoid
    // wasting memory.
    if (chunk->capacity < chunk->count + 1) {
        int oldCapacity = chunk->capacity;
        chunk->capacity = GROW_CAPACITY(oldCapacity);
        chunk->code = GROW_ARRAY(uint8_t, chunk->code, 
            oldCapacity, chunk->capacity);
    }

    if (chunk->lineCapacity < chunk->lineCount + 2) {
        int oldLineCapacity = chunk->lineCapacity;
        chunk->lineCapacity = GROW_CAPACITY(oldLineCapacity);
        chunk->lines = GROW_ARRAY(int, chunk->lines, 
            oldLineCapacity, chunk->lineCapacity);
    }

    int position = 0;
    if ((position = isLineAdded(chunk, line)) != -1) {
        // still same line ? increment the occurence
        chunk->lines[position+1]++;
    } else {
        chunk->lines[chunk->lineCount++] = line;
        //chunk->lineCount++;
        chunk->lines[chunk->lineCount++] = 1; // first occurence.
        //chunk->lineCount++;
    }
    chunk->code[chunk->count++] = byte;
    //chunk->count++;
}

int addConstant(Chunk* chunk, Value value) {
    push(value);
    writeValueArray(&chunk->constants, value);
    pop();
    return chunk->constants.count - 1;
}