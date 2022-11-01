import os
import shutil

directories = os.listdir('C:/Users/sshuv/Downloads/Compressed/archive/IDC_regular_ps50_idx5')

# print(directories)

source_folder = 'C:/Users/sshuv/Downloads/Compressed/archive/IDC_regular_ps50_idx5/'
destination_folder0 = 'C:/Users/sshuv/Downloads/Compressed/breast_cancer/0/'
destination_folder1 = 'C:/Users/sshuv/Downloads/Compressed/breast_cancer/1/'

for path, dirs, files in os.walk(source_folder):
    for file in files:
        src = path + '\\'+ file
        print(src)
        if file.endswith('class0.png'):
            shutil.move(src, destination_folder0)
        else:
            shutil.move(src, destination_folder1)


