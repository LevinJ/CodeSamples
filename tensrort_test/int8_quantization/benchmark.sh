#!/bin/bash

# Build the quantized engine using trtexec
trtexec --onnx=resnet50-v2-7.onnx --int8 --calib=calibration.cache --saveEngine=quantized_engine.trt

# Benchmark the quantized engine
trtexec --loadEngine=quantized_engine.trt --batch=8 --iterations=100
