#!/bin/bash
time gcc codepow.c -lm -o codepow.bin # time the compilation of c
time g++ codepow.cpp -o codepow-cpp.bin # time compilation of cpp
time ./codepow.py >> /dev/null # time run of python
time ./codepow-cpp.bin >> /dev/null # time run of cpp
time ./codepow.bin >> /dev/null #time run of c
rm codepow.bin codepow-cpp.bin # rm the bins
