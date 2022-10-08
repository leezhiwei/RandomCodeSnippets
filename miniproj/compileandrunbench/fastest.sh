#!/bin/bash
time gcc test.c -lm -o test.bin
time g++ test.cpp -o test-cpp.bin
time ./test.py >> /dev/null
time ./test-cpp.bin >> /dev/null
time ./test.bin >> /dev/null
rm test.bin test-cpp.bin
