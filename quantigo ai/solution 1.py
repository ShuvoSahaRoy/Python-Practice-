import os
import json

# Opening JSON file
file_path = r'C:/Users/sshuv/Desktop/quantigo ai/original files/pos_10492.png.json'
file_name = os.path.basename(file_path)

with open(file_path) as f:
    # returns JSON object as a dictionary
    data = json.load(f)

# print(data)
# print(data.keys())
# print(data.values())

# declear variables. list and dictionaries to store information from json
presence_vehicle = 0
presence_plate = 0
vehicle_box = []
plate_box = []
vehicle_attributes = {}
plate_attributes = {}

# type of data is dict and objects is list data type
objects = data['objects']


# extract information from objects and store it to decleared variable 
if objects:
    for obj in objects:

        if obj.get('classTitle') == 'Vehicle':
            presence_vehicle += 1

            if obj.get('points'):
                for ex_in in obj['points']:
                    ex_in_points = obj['points'].get(ex_in)
                    for ex_in_point in ex_in_points:
                        vehicle_box.extend(ex_in_point)

            if obj.get('tags'):
                for tag in obj['tags']:
                    vehicle_attributes.update({
                        tag.get('name'): tag.get('value')
                    })

        elif obj.get('classTitle') == 'License Plate':
            presence_plate += 1

            if obj.get('points'):
                for ex_in in obj['points']:
                    ex_in_points = obj['points'].get(ex_in)
                    for ex_in_point in ex_in_points:
                        plate_box.extend(ex_in_point)

            if obj.get('tags'):
                for tag in obj['tags']:
                    plate_attributes.update({
                        tag.get('name'): tag.get('value')
                    })


# check annotation
annotation = file_name.split('.')[-2]
image = ['jpge', 'jpg', 'png', 'JPGE', 'JPG', 'PNG']
if annotation in image:
    annotation_type = "image"
else:
    annotation_type = "Unknown"

if len(vehicle_attributes) == 0:
    vehicle_attributes.update({
            "Type": None,
            "Pose": None,
            "Model": None,
            "Make": None,
            "Color": None
        })

if len(plate_attributes) == 0:
    plate_attributes.update({
        "Difficulty Score": None,
        "Value": None,
        "Occlusion": None
    })


formatted_data_list = [{
    "dataset_name": file_name,
    "image_link": "",
    "annotation_type": annotation_type,
    "annotation_objects": {
        "vehicle": {
            "presence": presence_vehicle,
            "bbox": vehicle_box
        },
        "license_plate": {
            "presence": presence_plate,
            "bbox": plate_box
        }
    },
    "annotation_attributes": {
        "vehicle": vehicle_attributes,
        "license_plate": plate_attributes
    }
}]

formatted_file_name = "SSRoy_Formatted_solve1_" + file_name
print(f"file_name: {formatted_file_name} Created successfully" )
with open(formatted_file_name, 'w') as f:
    json.dump(formatted_data_list, f, indent=4)
