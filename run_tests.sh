#!/bin/bash

for f in $(find ./tests -type f)
do 
    if [[ $f == *.lox ]]
    then
        echo -e "==== Running test for $f with valgrind memChecks ====\n"
        valgrind --leak-check-full --show-leak-kinds=all --error-exit-code=-1 $1 $f 
        echo -e "\n";
    fi
done
