#########踩坑经历
1. 将训练图片和测试图片保存为tfrecord文件，并使用dataset实现多线程读取，自动打乱等操作，这样来减少数据训练所占用的物理内存
2. 将inceptionV3进行模型初始化时，没有将模型训练好的值初始化到模型，导致训练非常慢，要重新训练
3. 训练模型，在训练集上loss和acc都很好的表现，但是在测试集上却表现糟糕，原因是BatchNorm层作怪，第一次先将is_Trainning设为True进行测试，效果可以;
   后来觉得这样做并不能导入可用模型;
   第二次尝试在测试时is_Trainning还是置为False，移除BatchNorm层，且训练时同步更新moving_mean和moving_variance, 效果虽然提升，还是不理想;
   第三次发现batch_norm_decay这个值在处理小数据集的时候，尽量要让网络不平缓，要设小点, 结果还可以;
4. 在模型冻结上，直接采用freeze_graph和optimize_for_inference，网络没有移除Batch_Norm, dropout等不需要的Layer，导致在iOS上报错，不支持这些op；
   第一次，读取frozen_graph.pb，手动删除dropout，动态添加input_tensor输入层, 虽然模型可以在iOS上跑，运行正常，但是数据显示完全异常，所有类的正确率全是Nan，可见这条路走不通;
   第二次，在需要冻结的时候，训练时手动改代码设置is_Trainning=False，让其在非训练下模式下跑模型，并保存checkpoint, 进行模型导出，这样做感觉还是不理想，
   太笨了，破坏了项目的checkpoint结构，导致不能后续的训练优化模型;
   第三次，使用estimator的export_saved_model的方式，可以完美添加input Layer层，自动删除了Batch_Norm, dropout, iterator等op;
5. 使用tflite_convert转换为tflite文件
6. 由于我们的模型的输入层只是使用了convert_image_dtype方法，要稍微修改下demo参数，输入值把(0,255)规范到(0, 1)即可
7. 最后训练600步, 只将模型测试集预测正确率提升到80%左右；

