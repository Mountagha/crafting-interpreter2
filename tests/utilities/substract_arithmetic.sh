#!/bin/bash

#generate arithmetic operation for op_substract suppression
echo "var start = clock();" >> $1
for x in {0..10000..1}
do
    a=$((1 + $RANDOM % 100))
    # b=$((1 + $RANDOM % 200))
    # echo "print $b - $a;" >> $1
    echo "print -$a;" >> $1
done
echo "print \"time taken:\";" >> $1
echo "print clock() - start;" >> $1