#!/bin/bash

PIN_OUT="21"
for OUTPIN in ${PIN_OUT}
do
    echo "${OUTPIN}" > /sys/class/gpio/export
    echo "out" > /sys/class/gpio${OUTPIN}/direction

done
