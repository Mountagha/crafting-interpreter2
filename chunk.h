#ifndef clox_chunk_h
#define clox_chunk_h

#include "common.h"
#include "value.h"

typedef enum {
    OP_CONSTANT,
    OP_CONSTANT_LONG,
    OP_NIL,
    OP_TRUE,
    OP_FALSE,
    OP_POP,
    OP_GET_LOCAL,
    OP_SET_LOCAL,
    OP_GET_GLOBAL,
    OP_SET_GLOBAL,
    OP_GET_UPVALUE,
    OP_SET_UPVALUE,
    OP_DEFINE_GLOBAL,
    OP_GET_PROPERTY,
    OP_SET_PROPERTY,
    OP_GET_SUPER,
    OP_EQUAL,
    OP_GREATER,
    OP_LESS,
    OP_ADD,
    OP_SUBSTRACT,
    OP_MULTIPLY,
    OP_DIVIDE,
    OP_NOT,
    OP_PRINT,
    OP_JUMP,
    OP_JUMP_IF_FALSE,
    OP_NEGATE,
    OP_LOOP,
    OP_CALL,
    OP_INVOKE,
    OP_CLOSURE,
    OP_SUPER_INVOKE,
    OP_CLOSE_UPVALUE,
    OP_CLASS,
    OP_INHERIT,
    OP_METHOD,
    OP_RETURN,
} OpCode;

/* 
    Since all constants were stuffed inside constants ValueArray, Scaling raw constants
    would be almost impossible. Let say we want a function to have more than 255 raw constants
    the way we define those constants is by creating variable by example i.e var x = "raw_constant";
    but in this case x is also an identifiant and also stuffed in the same array as the raw_constant.
    We, hence decide to create another array constantsOp which would contain all raw constants and let 
    all other kind of constants stayed in constants array. this way we can stuff as much raw constants
    as we want in the new Array since OP_CONSTANT_LONG come to rescousse when we go above 255 constants
    that OP_CONSTANT supports.
*/
typedef struct {
    int count;
    int capacity;
    int lineCount;
    int lineCapacity;
    uint8_t* code;
    int* lines;
    ValueArray constants;
    ValueArray constantsOp; // for constants from op_constant & op_constant_long ONLY. 
} Chunk;

void initChunk(Chunk* chunk);
void freeChunk(Chunk* chunk);
void writeChunk(Chunk* chunk, uint8_t byte, int line);
void writeConstant(Chunk* chunk, Value value, int line);
int addConstant(Chunk* chunk, Value value);

#endif
