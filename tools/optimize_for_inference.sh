#!/usr/bin/env bash

~/Documents/Github/tensorflow2/bazel-out/darwin-py2-opt/bin/tensorflow/python/tools/optimize_for_inference \
--input=pb/freeze_graph.pb \
--output=pb/flowers_optimize_for_inference.pb \
--frozen_graph=True \
--input_names=my_inputs \
--output_names=InceptionV3/Predictions/Reshape_1