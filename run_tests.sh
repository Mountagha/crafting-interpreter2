#!/bin/bash

for f in $(find ./tests -type f)
do 
    if [[ $f == *.lox ]]
    then
        echo -e "==== Running test for $f with valgrind memChecks ====\n"
        valgrind --leak-check=full --show-leak-kinds=all --error-exitcode=1 $1 $f 
        ret=`echo $?`
        if [[ $ret == 1 ]]
        then
            exit 1
        fi
        echo -e "\n";
    fi
done
