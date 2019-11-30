# 0 my_inputs Placeholder
# 1 InceptionV3/Conv2d_1a_3x3/weights Const
# 2 InceptionV3/InceptionV3/Conv2d_1a_3x3/Conv2D Conv2D
# └─── 0 ─ my_inputs
# └─── 1 ─ InceptionV3/Conv2d_1a_3x3/weights
# 3 InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const Const
# 4 InceptionV3/Conv2d_1a_3x3/BatchNorm/beta Const
# 5 InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const_1 Const
# 6 InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const_2 Const
# 7 InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Conv2d_1a_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/Const_2
# 8 InceptionV3/InceptionV3/Conv2d_1a_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm
# 9 InceptionV3/Conv2d_2a_3x3/weights Const
# 10 InceptionV3/InceptionV3/Conv2d_2a_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_1a_3x3/Relu
# └─── 1 ─ InceptionV3/Conv2d_2a_3x3/weights
# 11 InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const Const
# 12 InceptionV3/Conv2d_2a_3x3/BatchNorm/beta Const
# 13 InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const_1 Const
# 14 InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const_2 Const
# 15 InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Conv2d_2a_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/Const_2
# 16 InceptionV3/InceptionV3/Conv2d_2a_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/BatchNorm/FusedBatchNorm
# 17 InceptionV3/Conv2d_2b_3x3/weights Const
# 18 InceptionV3/InceptionV3/Conv2d_2b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2a_3x3/Relu
# └─── 1 ─ InceptionV3/Conv2d_2b_3x3/weights
# 19 InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const Const
# 20 InceptionV3/Conv2d_2b_3x3/BatchNorm/beta Const
# 21 InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const_1 Const
# 22 InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const_2 Const
# 23 InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Conv2d_2b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/Const_2
# 24 InceptionV3/InceptionV3/Conv2d_2b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/BatchNorm/FusedBatchNorm
# 25 InceptionV3/InceptionV3/MaxPool_3a_3x3/MaxPool MaxPool
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_2b_3x3/Relu
# 26 InceptionV3/Conv2d_3b_1x1/weights Const
# 27 InceptionV3/InceptionV3/Conv2d_3b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/MaxPool_3a_3x3/MaxPool
# └─── 1 ─ InceptionV3/Conv2d_3b_1x1/weights
# 28 InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const Const
# 29 InceptionV3/Conv2d_3b_1x1/BatchNorm/beta Const
# 30 InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const_1 Const
# 31 InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const_2 Const
# 32 InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Conv2d_3b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/Const_2
# 33 InceptionV3/InceptionV3/Conv2d_3b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/BatchNorm/FusedBatchNorm
# 34 InceptionV3/Conv2d_4a_3x3/weights Const
# 35 InceptionV3/InceptionV3/Conv2d_4a_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_3b_1x1/Relu
# └─── 1 ─ InceptionV3/Conv2d_4a_3x3/weights
# 36 InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const Const
# 37 InceptionV3/Conv2d_4a_3x3/BatchNorm/beta Const
# 38 InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const_1 Const
# 39 InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const_2 Const
# 40 InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Conv2d_4a_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/Const_2
# 41 InceptionV3/InceptionV3/Conv2d_4a_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/BatchNorm/FusedBatchNorm
# 42 InceptionV3/InceptionV3/MaxPool_5a_3x3/MaxPool MaxPool
# └─── 0 ─ InceptionV3/InceptionV3/Conv2d_4a_3x3/Relu
# 43 InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/weights Const
# 44 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/MaxPool_5a_3x3/MaxPool
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/weights
# 45 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 46 InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 47 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 48 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 49 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 50 InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 51 InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/weights Const
# 52 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/MaxPool_5a_3x3/MaxPool
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/weights
# 53 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 54 InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 55 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 56 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 57 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 58 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 59 InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/weights Const
# 60 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/weights
# 61 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const Const
# 62 InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/beta Const
# 63 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_1 Const
# 64 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_2 Const
# 65 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_2
# 66 InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/BatchNorm/FusedBatchNorm
# 67 InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/weights Const
# 68 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/MaxPool_5a_3x3/MaxPool
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/weights
# 69 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 70 InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 71 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 72 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 73 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 74 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 75 InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/weights Const
# 76 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/weights
# 77 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const Const
# 78 InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/beta Const
# 79 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 80 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 81 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2
# 82 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 83 InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/weights Const
# 84 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/weights
# 85 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const Const
# 86 InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/beta Const
# 87 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1 Const
# 88 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2 Const
# 89 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2
# 90 InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm
# 91 InceptionV3/InceptionV3/Mixed_5b/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/MaxPool_5a_3x3/MaxPool
# 92 InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/weights Const
# 93 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/weights
# 94 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 95 InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 96 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 97 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 98 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 99 InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 100 InceptionV3/InceptionV3/Mixed_5b/concat/axis Const
# 101 InceptionV3/InceptionV3/Mixed_5b/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_1/Conv2d_0b_5x5/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_2/Conv2d_0c_3x3/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5b/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5b/concat/axis
# 102 InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/weights Const
# 103 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/concat
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/weights
# 104 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 105 InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 106 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 107 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 108 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 109 InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 110 InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/weights Const
# 111 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/concat
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/weights
# 112 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const Const
# 113 InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/beta Const
# 114 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 115 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 116 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/Const_2
# 117 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 118 InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/weights Const
# 119 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv2d_0b_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/weights
# 120 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const Const
# 121 InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/beta Const
# 122 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const_1 Const
# 123 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const_2 Const
# 124 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/Const_2
# 125 InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/BatchNorm/FusedBatchNorm
# 126 InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/weights Const
# 127 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/concat
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/weights
# 128 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 129 InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 130 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 131 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 132 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 133 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 134 InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/weights Const
# 135 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/weights
# 136 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const Const
# 137 InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/beta Const
# 138 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 139 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 140 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2
# 141 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 142 InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/weights Const
# 143 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/weights
# 144 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const Const
# 145 InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/beta Const
# 146 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1 Const
# 147 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2 Const
# 148 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2
# 149 InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm
# 150 InceptionV3/InceptionV3/Mixed_5c/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5b/concat
# 151 InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/weights Const
# 152 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/weights
# 153 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 154 InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 155 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 156 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 157 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 158 InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 159 InceptionV3/InceptionV3/Mixed_5c/concat/axis Const
# 160 InceptionV3/InceptionV3/Mixed_5c/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_1/Conv_1_0c_5x5/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_2/Conv2d_0c_3x3/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5c/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5c/concat/axis
# 161 InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/weights Const
# 162 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/concat
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/weights
# 163 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 164 InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 165 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 166 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 167 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 168 InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 169 InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/weights Const
# 170 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/concat
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/weights
# 171 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 172 InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 173 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 174 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 175 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 176 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 177 InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/weights Const
# 178 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/weights
# 179 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const Const
# 180 InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/beta Const
# 181 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_1 Const
# 182 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_2 Const
# 183 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/Const_2
# 184 InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/BatchNorm/FusedBatchNorm
# 185 InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/weights Const
# 186 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/concat
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/weights
# 187 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 188 InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 189 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 190 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 191 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 192 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 193 InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/weights Const
# 194 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/weights
# 195 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const Const
# 196 InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/beta Const
# 197 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 198 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 199 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2
# 200 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 201 InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/weights Const
# 202 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/weights
# 203 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const Const
# 204 InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/beta Const
# 205 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1 Const
# 206 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2 Const
# 207 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/Const_2
# 208 InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/BatchNorm/FusedBatchNorm
# 209 InceptionV3/InceptionV3/Mixed_5d/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5c/concat
# 210 InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/weights Const
# 211 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/weights
# 212 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 213 InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 214 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 215 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 216 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 217 InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 218 InceptionV3/InceptionV3/Mixed_5d/concat/axis Const
# 219 InceptionV3/InceptionV3/Mixed_5d/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_1/Conv2d_0b_5x5/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_2/Conv2d_0c_3x3/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_5d/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_5d/concat/axis
# 220 InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/weights Const
# 221 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/concat
# └─── 1 ─ InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/weights
# 222 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const Const
# 223 InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/beta Const
# 224 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const_1 Const
# 225 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const_2 Const
# 226 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/Const_2
# 227 InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/BatchNorm/FusedBatchNorm
# 228 InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/weights Const
# 229 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/concat
# └─── 1 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/weights
# 230 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 231 InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 232 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 233 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 234 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 235 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 236 InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/weights Const
# 237 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/weights
# 238 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const Const
# 239 InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/beta Const
# 240 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 241 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 242 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/Const_2
# 243 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 244 InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/weights Const
# 245 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/weights
# 246 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const Const
# 247 InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/beta Const
# 248 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const_1 Const
# 249 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const_2 Const
# 250 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/Const_2
# 251 InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/BatchNorm/FusedBatchNorm
# 252 InceptionV3/InceptionV3/Mixed_6a/Branch_2/MaxPool_1a_3x3/MaxPool MaxPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_5d/concat
# 253 InceptionV3/InceptionV3/Mixed_6a/concat/axis Const
# 254 InceptionV3/InceptionV3/Mixed_6a/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_0/Conv2d_1a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_1/Conv2d_1a_1x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_6a/Branch_2/MaxPool_1a_3x3/MaxPool
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6a/concat/axis
# 255 InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/weights Const
# 256 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/concat
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/weights
# 257 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 258 InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 259 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 260 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 261 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 262 InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 263 InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/weights Const
# 264 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/concat
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/weights
# 265 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 266 InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 267 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 268 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 269 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 270 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 271 InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/weights Const
# 272 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/weights
# 273 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const Const
# 274 InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/beta Const
# 275 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1 Const
# 276 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2 Const
# 277 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2
# 278 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm
# 279 InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/weights Const
# 280 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0b_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/weights
# 281 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const Const
# 282 InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/beta Const
# 283 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1 Const
# 284 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2 Const
# 285 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2
# 286 InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm
# 287 InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/weights Const
# 288 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/concat
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/weights
# 289 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 290 InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 291 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 292 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 293 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 294 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 295 InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/weights Const
# 296 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/weights
# 297 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const Const
# 298 InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/beta Const
# 299 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1 Const
# 300 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2 Const
# 301 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2
# 302 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm
# 303 InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/weights Const
# 304 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0b_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/weights
# 305 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const Const
# 306 InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/beta Const
# 307 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1 Const
# 308 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2 Const
# 309 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2
# 310 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm
# 311 InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/weights Const
# 312 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0c_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/weights
# 313 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const Const
# 314 InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/beta Const
# 315 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1 Const
# 316 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2 Const
# 317 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2
# 318 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm
# 319 InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/weights Const
# 320 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0d_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/weights
# 321 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const Const
# 322 InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/beta Const
# 323 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1 Const
# 324 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2 Const
# 325 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2
# 326 InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm
# 327 InceptionV3/InceptionV3/Mixed_6b/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6a/concat
# 328 InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/weights Const
# 329 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/weights
# 330 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 331 InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 332 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 333 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 334 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 335 InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 336 InceptionV3/InceptionV3/Mixed_6b/concat/axis Const
# 337 InceptionV3/InceptionV3/Mixed_6b/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_1/Conv2d_0c_7x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_2/Conv2d_0e_1x7/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6b/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6b/concat/axis
# 338 InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/weights Const
# 339 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/concat
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/weights
# 340 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 341 InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 342 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 343 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 344 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 345 InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 346 InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/weights Const
# 347 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/concat
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/weights
# 348 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 349 InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 350 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 351 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 352 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 353 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 354 InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/weights Const
# 355 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/weights
# 356 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const Const
# 357 InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/beta Const
# 358 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1 Const
# 359 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2 Const
# 360 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2
# 361 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm
# 362 InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/weights Const
# 363 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0b_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/weights
# 364 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const Const
# 365 InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/beta Const
# 366 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1 Const
# 367 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2 Const
# 368 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2
# 369 InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm
# 370 InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/weights Const
# 371 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/concat
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/weights
# 372 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 373 InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 374 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 375 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 376 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 377 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 378 InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/weights Const
# 379 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/weights
# 380 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const Const
# 381 InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/beta Const
# 382 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1 Const
# 383 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2 Const
# 384 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2
# 385 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm
# 386 InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/weights Const
# 387 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0b_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/weights
# 388 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const Const
# 389 InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/beta Const
# 390 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1 Const
# 391 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2 Const
# 392 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2
# 393 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm
# 394 InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/weights Const
# 395 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0c_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/weights
# 396 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const Const
# 397 InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/beta Const
# 398 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1 Const
# 399 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2 Const
# 400 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2
# 401 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm
# 402 InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/weights Const
# 403 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0d_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/weights
# 404 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const Const
# 405 InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/beta Const
# 406 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1 Const
# 407 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2 Const
# 408 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2
# 409 InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm
# 410 InceptionV3/InceptionV3/Mixed_6c/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6b/concat
# 411 InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/weights Const
# 412 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/weights
# 413 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 414 InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 415 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 416 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 417 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 418 InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 419 InceptionV3/InceptionV3/Mixed_6c/concat/axis Const
# 420 InceptionV3/InceptionV3/Mixed_6c/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_1/Conv2d_0c_7x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_2/Conv2d_0e_1x7/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6c/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6c/concat/axis
# 421 InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/weights Const
# 422 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/concat
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/weights
# 423 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 424 InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 425 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 426 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 427 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 428 InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 429 InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/weights Const
# 430 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/concat
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/weights
# 431 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 432 InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 433 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 434 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 435 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 436 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 437 InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/weights Const
# 438 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/weights
# 439 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const Const
# 440 InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/beta Const
# 441 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1 Const
# 442 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2 Const
# 443 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2
# 444 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm
# 445 InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/weights Const
# 446 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0b_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/weights
# 447 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const Const
# 448 InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/beta Const
# 449 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1 Const
# 450 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2 Const
# 451 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2
# 452 InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm
# 453 InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/weights Const
# 454 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/concat
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/weights
# 455 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 456 InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 457 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 458 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 459 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 460 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 461 InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/weights Const
# 462 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/weights
# 463 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const Const
# 464 InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/beta Const
# 465 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1 Const
# 466 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2 Const
# 467 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2
# 468 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm
# 469 InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/weights Const
# 470 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0b_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/weights
# 471 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const Const
# 472 InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/beta Const
# 473 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1 Const
# 474 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2 Const
# 475 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2
# 476 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm
# 477 InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/weights Const
# 478 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0c_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/weights
# 479 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const Const
# 480 InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/beta Const
# 481 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1 Const
# 482 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2 Const
# 483 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2
# 484 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm
# 485 InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/weights Const
# 486 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0d_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/weights
# 487 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const Const
# 488 InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/beta Const
# 489 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1 Const
# 490 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2 Const
# 491 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2
# 492 InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm
# 493 InceptionV3/InceptionV3/Mixed_6d/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6c/concat
# 494 InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/weights Const
# 495 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/weights
# 496 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 497 InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 498 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 499 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 500 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 501 InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 502 InceptionV3/InceptionV3/Mixed_6d/concat/axis Const
# 503 InceptionV3/InceptionV3/Mixed_6d/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_1/Conv2d_0c_7x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_2/Conv2d_0e_1x7/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6d/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6d/concat/axis
# 504 InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/weights Const
# 505 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/concat
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/weights
# 506 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 507 InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 508 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 509 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 510 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 511 InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 512 InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/weights Const
# 513 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/concat
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/weights
# 514 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 515 InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 516 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 517 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 518 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 519 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 520 InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/weights Const
# 521 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/weights
# 522 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const Const
# 523 InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/beta Const
# 524 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1 Const
# 525 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2 Const
# 526 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2
# 527 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm
# 528 InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/weights Const
# 529 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0b_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/weights
# 530 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const Const
# 531 InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/beta Const
# 532 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1 Const
# 533 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2 Const
# 534 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2
# 535 InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm
# 536 InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/weights Const
# 537 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/concat
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/weights
# 538 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 539 InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 540 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 541 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 542 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 543 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 544 InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/weights Const
# 545 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/weights
# 546 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const Const
# 547 InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/beta Const
# 548 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1 Const
# 549 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2 Const
# 550 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/Const_2
# 551 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/BatchNorm/FusedBatchNorm
# 552 InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/weights Const
# 553 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0b_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/weights
# 554 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const Const
# 555 InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/beta Const
# 556 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1 Const
# 557 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2 Const
# 558 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/Const_2
# 559 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/BatchNorm/FusedBatchNorm
# 560 InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/weights Const
# 561 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0c_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/weights
# 562 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const Const
# 563 InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/beta Const
# 564 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1 Const
# 565 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2 Const
# 566 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/Const_2
# 567 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/BatchNorm/FusedBatchNorm
# 568 InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/weights Const
# 569 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0d_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/weights
# 570 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const Const
# 571 InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/beta Const
# 572 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1 Const
# 573 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2 Const
# 574 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/Const_2
# 575 InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/BatchNorm/FusedBatchNorm
# 576 InceptionV3/InceptionV3/Mixed_6e/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6d/concat
# 577 InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/weights Const
# 578 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/weights
# 579 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 580 InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 581 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 582 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 583 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 584 InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 585 InceptionV3/InceptionV3/Mixed_6e/concat/axis Const
# 586 InceptionV3/InceptionV3/Mixed_6e/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_1/Conv2d_0c_7x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_2/Conv2d_0e_1x7/Relu
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_6e/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_6e/concat/axis
# 587 InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/weights Const
# 588 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/concat
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/weights
# 589 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 590 InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 591 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 592 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 593 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 594 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 595 InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/weights Const
# 596 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/weights
# 597 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const Const
# 598 InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/beta Const
# 599 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const_1 Const
# 600 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const_2 Const
# 601 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/Const_2
# 602 InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm
# 603 InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/weights Const
# 604 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/concat
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/weights
# 605 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 606 InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 607 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 608 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 609 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 610 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 611 InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/weights Const
# 612 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/weights
# 613 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const Const
# 614 InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/beta Const
# 615 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1 Const
# 616 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2 Const
# 617 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/Const_2
# 618 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/BatchNorm/FusedBatchNorm
# 619 InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/weights Const
# 620 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0b_1x7/Relu
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/weights
# 621 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const Const
# 622 InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/beta Const
# 623 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1 Const
# 624 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2 Const
# 625 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/Const_2
# 626 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/BatchNorm/FusedBatchNorm
# 627 InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/weights Const
# 628 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_0c_7x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/weights
# 629 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const Const
# 630 InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/beta Const
# 631 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const_1 Const
# 632 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const_2 Const
# 633 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/Const_2
# 634 InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/BatchNorm/FusedBatchNorm
# 635 InceptionV3/InceptionV3/Mixed_7a/Branch_2/MaxPool_1a_3x3/MaxPool MaxPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_6e/concat
# 636 InceptionV3/InceptionV3/Mixed_7a/concat/axis Const
# 637 InceptionV3/InceptionV3/Mixed_7a/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_0/Conv2d_1a_3x3/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_1/Conv2d_1a_3x3/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7a/Branch_2/MaxPool_1a_3x3/MaxPool
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7a/concat/axis
# 638 InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/weights Const
# 639 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/concat
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/weights
# 640 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 641 InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 642 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 643 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 644 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 645 InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 646 InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/weights Const
# 647 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/concat
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/weights
# 648 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 649 InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 650 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 651 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 652 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 653 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 654 InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/weights Const
# 655 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/weights
# 656 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const Const
# 657 InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/beta Const
# 658 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_1 Const
# 659 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_2 Const
# 660 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_2
# 661 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/BatchNorm/FusedBatchNorm
# 662 InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/weights Const
# 663 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/weights
# 664 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const Const
# 665 InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/beta Const
# 666 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const_1 Const
# 667 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const_2 Const
# 668 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/Const_2
# 669 InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/BatchNorm/FusedBatchNorm
# 670 InceptionV3/InceptionV3/Mixed_7b/Branch_1/concat/axis Const
# 671 InceptionV3/InceptionV3/Mixed_7b/Branch_1/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_1x3/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/Conv2d_0b_3x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/concat/axis
# 672 InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/weights Const
# 673 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/concat
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/weights
# 674 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 675 InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 676 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 677 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 678 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 679 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 680 InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/weights Const
# 681 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/weights
# 682 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const Const
# 683 InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/beta Const
# 684 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 685 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 686 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2
# 687 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 688 InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/weights Const
# 689 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/weights
# 690 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const Const
# 691 InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/beta Const
# 692 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_1 Const
# 693 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_2 Const
# 694 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_2
# 695 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/BatchNorm/FusedBatchNorm
# 696 InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/weights Const
# 697 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/weights
# 698 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const Const
# 699 InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/beta Const
# 700 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_1 Const
# 701 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_2 Const
# 702 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_2
# 703 InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/BatchNorm/FusedBatchNorm
# 704 InceptionV3/InceptionV3/Mixed_7b/Branch_2/concat/axis Const
# 705 InceptionV3/InceptionV3/Mixed_7b/Branch_2/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0c_1x3/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/Conv2d_0d_3x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/concat/axis
# 706 InceptionV3/InceptionV3/Mixed_7b/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7a/concat
# 707 InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/weights Const
# 708 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/weights
# 709 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 710 InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 711 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 712 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 713 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 714 InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 715 InceptionV3/InceptionV3/Mixed_7b/concat/axis Const
# 716 InceptionV3/InceptionV3/Mixed_7b/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_1/concat
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_2/concat
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7b/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7b/concat/axis
# 717 InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/weights Const
# 718 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/concat
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/weights
# 719 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const Const
# 720 InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta Const
# 721 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 722 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 723 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/Const_2
# 724 InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 725 InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/weights Const
# 726 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/concat
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/weights
# 727 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const Const
# 728 InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/beta Const
# 729 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 730 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 731 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/Const_2
# 732 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 733 InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/weights Const
# 734 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/weights
# 735 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const Const
# 736 InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/beta Const
# 737 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_1 Const
# 738 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_2 Const
# 739 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/Const_2
# 740 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/BatchNorm/FusedBatchNorm
# 741 InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/weights Const
# 742 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/weights
# 743 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const Const
# 744 InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/beta Const
# 745 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const_1 Const
# 746 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const_2 Const
# 747 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/Const_2
# 748 InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/BatchNorm/FusedBatchNorm
# 749 InceptionV3/InceptionV3/Mixed_7c/Branch_1/concat/axis Const
# 750 InceptionV3/InceptionV3/Mixed_7c/Branch_1/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0b_1x3/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/Conv2d_0c_3x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/concat/axis
# 751 InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/weights Const
# 752 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/concat
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/weights
# 753 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const Const
# 754 InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta Const
# 755 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1 Const
# 756 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2 Const
# 757 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/Const_2
# 758 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/BatchNorm/FusedBatchNorm
# 759 InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/weights Const
# 760 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/weights
# 761 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const Const
# 762 InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/beta Const
# 763 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1 Const
# 764 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2 Const
# 765 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/Const_2
# 766 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/BatchNorm/FusedBatchNorm
# 767 InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/weights Const
# 768 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/weights
# 769 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const Const
# 770 InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/beta Const
# 771 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_1 Const
# 772 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_2 Const
# 773 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/Const_2
# 774 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/BatchNorm/FusedBatchNorm
# 775 InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/weights Const
# 776 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0b_3x3/Relu
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/weights
# 777 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const Const
# 778 InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/beta Const
# 779 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_1 Const
# 780 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_2 Const
# 781 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/Const_2
# 782 InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/BatchNorm/FusedBatchNorm
# 783 InceptionV3/InceptionV3/Mixed_7c/Branch_2/concat/axis Const
# 784 InceptionV3/InceptionV3/Mixed_7c/Branch_2/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0c_1x3/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/Conv2d_0d_3x1/Relu
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/concat/axis
# 785 InceptionV3/InceptionV3/Mixed_7c/Branch_3/AvgPool_0a_3x3/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7b/concat
# 786 InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/weights Const
# 787 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/AvgPool_0a_3x3/AvgPool
# └─── 1 ─ InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/weights
# 788 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const Const
# 789 InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta Const
# 790 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1 Const
# 791 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2 Const
# 792 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm FusedBatchNorm
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/Conv2D
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const
# └─── 2 ─ InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/beta
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_1
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/Const_2
# 793 InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/Relu Relu
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/FusedBatchNorm
# 794 InceptionV3/InceptionV3/Mixed_7c/concat/axis Const
# 795 InceptionV3/InceptionV3/Mixed_7c/concat ConcatV2
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_0/Conv2d_0a_1x1/Relu
# └─── 1 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_1/concat
# └─── 2 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_2/concat
# └─── 3 ─ InceptionV3/InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/Relu
# └─── 4 ─ InceptionV3/InceptionV3/Mixed_7c/concat/axis
# 796 InceptionV3/Logits/AvgPool_1a_8x8/AvgPool AvgPool
# └─── 0 ─ InceptionV3/InceptionV3/Mixed_7c/concat
# 797 InceptionV3/Logits/Dropout_1b/dropout/rate Const
# 798 InceptionV3/Logits/Dropout_1b/dropout/Shape Shape
# └─── 0 ─ InceptionV3/Logits/AvgPool_1a_8x8/AvgPool
# 799 InceptionV3/Logits/Dropout_1b/dropout/random_uniform/min Const
# 800 InceptionV3/Logits/Dropout_1b/dropout/random_uniform/max Const
# 801 InceptionV3/Logits/Dropout_1b/dropout/random_uniform/RandomUniform RandomUniform
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/Shape
# 802 InceptionV3/Logits/Dropout_1b/dropout/random_uniform/sub Sub
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/max
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/min
# 803 InceptionV3/Logits/Dropout_1b/dropout/random_uniform/mul Mul
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/RandomUniform
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/sub
# 804 InceptionV3/Logits/Dropout_1b/dropout/random_uniform Add
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/mul
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform/min
# 805 InceptionV3/Logits/Dropout_1b/dropout/sub/x Const
# 806 InceptionV3/Logits/Dropout_1b/dropout/sub Sub
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/sub/x
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/rate
# 807 InceptionV3/Logits/Dropout_1b/dropout/truediv/x Const
# 808 InceptionV3/Logits/Dropout_1b/dropout/truediv RealDiv
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/truediv/x
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/sub
# 809 InceptionV3/Logits/Dropout_1b/dropout/GreaterEqual GreaterEqual
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/random_uniform
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/rate
# 810 InceptionV3/Logits/Dropout_1b/dropout/mul Mul
# └─── 0 ─ InceptionV3/Logits/AvgPool_1a_8x8/AvgPool
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/truediv
# 811 InceptionV3/Logits/Dropout_1b/dropout/Cast Cast
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/GreaterEqual
# 812 InceptionV3/Logits/Dropout_1b/dropout/mul_1 Mul
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/mul
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/Cast
# 813 InceptionV3/Logits/Conv2d_1c_1x1/weights Const
# 814 InceptionV3/Logits/Conv2d_1c_1x1/biases Const
# 815 InceptionV3/Logits/Conv2d_1c_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/mul_1
# └─── 1 ─ InceptionV3/Logits/Conv2d_1c_1x1/weights
# 816 InceptionV3/Logits/Conv2d_1c_1x1/BiasAdd BiasAdd
# └─── 0 ─ InceptionV3/Logits/Conv2d_1c_1x1/Conv2D
# └─── 1 ─ InceptionV3/Logits/Conv2d_1c_1x1/biases
# 817 InceptionV3/Logits/SpatialSqueeze Squeeze
# └─── 0 ─ InceptionV3/Logits/Conv2d_1c_1x1/BiasAdd
# 818 InceptionV3/Predictions/Reshape/shape Const
# 819 InceptionV3/Predictions/Reshape Reshape
# └─── 0 ─ InceptionV3/Logits/SpatialSqueeze
# └─── 1 ─ InceptionV3/Predictions/Reshape/shape
# 820 InceptionV3/Predictions/Softmax Softmax
# └─── 0 ─ InceptionV3/Predictions/Reshape
# 821 InceptionV3/Predictions/Shape Shape
# └─── 0 ─ InceptionV3/Logits/SpatialSqueeze
# 822 InceptionV3/Predictions/Reshape_1 Reshape
# └─── 0 ─ InceptionV3/Predictions/Softmax
# └─── 1 ─ InceptionV3/Predictions/Shape