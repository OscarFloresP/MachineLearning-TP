from time import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import os
import numpy as np
from to_binvox import voxels_from_file

folder = '03001627'
paths = [os.path.join(folder, f) for f in os.listdir(folder) if f != 'All Models']
files = [os.path.join(i,j) for i in paths for j in os.listdir(i) if j[-4:] == '.obj']


n_cpu = multiprocessing.cpu_count()


t0 = time()
with ThreadPoolExecutor(max_workers=n_cpu) as executor:
    res = executor.map(voxels_from_file, files)

errors, voxels, labels = zip(*res)
print('%.2fs' % (time() - t0))

# remove the one with errors
errors = np.array(errors)
labels = np.array(labels)[errors == 1]
voxels = np.array([voxels[i] for i in np.where(errors == 1)[0]])

print(voxels.shape, labels.shape)

# save
output = {}
output['train'] = {'labels': labels, 'data': voxels, 'errors': []}
np.save('repo/voxels.npy', output)

# load
# output = np.load('repo/voxels.npy').item()
# labels = output['train']['labels']
# voxels = output['train']['data']

# print(np.unique(labels))