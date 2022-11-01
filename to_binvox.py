import os
import numpy as np
import binvox_rw

import shutil

def voxels_from_file(_file, voxsize=32):
    label = os.path.basename(os.path.dirname(_file))
    out_file = _file.split('.')[0] + '.binvox'


    os.mkdir("chair_as_binvox\\" + _file.split('.')[0].split('\\')[1])
    print(out_file)
    _file = _file.replace(' ', '\ ')
    cmd = f'binvox -d {voxsize} -cb -e "{_file}"'
    print(cmd)

    
    if os.path.exists(out_file):
        os.remove(out_file)

    t = os.system(cmd)
    
    if t == 0:
        new_file = "chair_as_binvox\\" + "\\".join(_file.split('.')[0].split('\\')[1:]) + '.binvox'
        shutil.copyfile(out_file, new_file)

        with open(out_file, 'rb') as f:
            d = binvox_rw.read_as_3d_array(f).data
        
        # os.remove(out_file)
        return 1, d, label
    else:
        return 0, None, label

if __name__ == "__main__":

    folder = '03001627'
    paths = [os.path.join(folder, f) for f in os.listdir(folder) if f != 'All Models']
    files = [os.path.join(i,j) for i in paths for j in os.listdir(i) if j[-4:] == '.obj']


    one_file = np.random.choice(files)


    voxels = voxels_from_file(one_file, 32)
    print('\nPlotting:', one_file)


    print(voxels[0])
    print(voxels[2])
    print(voxels[1])