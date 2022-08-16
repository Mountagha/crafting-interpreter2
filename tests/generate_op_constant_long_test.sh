#!/bin/bash

var_dec="var long_var = "
for i in {1..255}
do
    var_dec+="\"val$i\" + "
done
var_dec+=";"
echo $var_dec >> op_constant_long.lox