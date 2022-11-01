import os
import os.path

source_folder = r'G:\Other\New folder'

for dirpath, dirnames, filenames in os.walk(source_folder):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print(len(filenames))
    # print("\n\n\n\n")
    for filename in [f for f in filenames if f.endswith(".webp") or f.endswith(".jfif")]:
        final_path_file = (os.path.join(dirpath, filename))
        # print(filename)
        pre, ext = os.path.splitext(final_path_file)
        # print(f"{pre} and {ext}")
        try:
            os.rename(final_path_file, pre + '.jpg')
        except:
            existing_file_name = pre + '.jpg'
            # print(existing_file_name)
            if os.path.exists(existing_file_name):
                # print("exist")
                existing_size = os.path.getsize(existing_file_name)
                selected_file_size = os.path.getsize(final_path_file)
                if existing_size > selected_file_size:
                    os.remove(final_path_file)
                else:
                    print("error in except")
            else:
                print("file doesn't exist")
print("Operation successful")