#!/usr/bin/env bash

 freeze_graph \
--input_graph=train_model/graph.pbtxt \
--input_checkpoint=train_model/model.ckpt-100 \
--output_graph=pb/freeze_graph.pb \
--output_node_names=InceptionV3/Predictions/Reshape_1 \
--input_names=my_inputs \