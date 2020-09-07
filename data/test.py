import numpy as np

aaa = np.load('features/COCO_val2014_000000006005.npz')
bbb = np.load('features_old/COCO_val2014_000000006005.npz')
print(aaa['num_bbox'])
print(bbb['num_bbox'])