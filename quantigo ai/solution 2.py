import glob
import json
files = glob.glob(r'C:\Users\sshuv\Desktop\quantigo ai\original files\*')
target_files = files[2:5]

data_list = []

for file in target_files:
    file_name = file.split("\\")[-1]
    
    with open(file, 'r') as f:
        data = json.load(f)
        
    objects = data.get('objects')
    
    if objects:
        for obj in objects:
            classTitle = obj.get("classTitle")
            if classTitle == "Vehicle":
                obj['classTitle'] = "Car"
            elif classTitle == "License Plate":
                obj['classTitle'] = "Number"
            else:
                print("There is no classTitle in {file_name}")
    
    # data['objects'] = objects
    data_list.append(data)

with open('all_files.json', 'w') as f:
    json.dump(data_list, f, indent=4)