#!/bin/bash
# Benchmark the quantized engine
trtexec --loadEngine=quantized_engine.trt --batch=8 --iterations=100
