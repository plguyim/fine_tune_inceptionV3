#!/usr/bin/env bash

tflite_convert \
--output_file=pb/tmp.tflite \
--output_format=TFLITE \
--saved_model_dir=export_dir/1575029684 \
--input_arrays=input_tensor \
--output_arrays=InceptionV3/Predictions/Reshape_1 \
--input_shapes=1,299,299,3 \
--allow_custom_ops


#--graph_def_file=pb/optimized_frozen_graph.pb \
#--graph_def_file=pb/optimized_frozen_graph.pb \