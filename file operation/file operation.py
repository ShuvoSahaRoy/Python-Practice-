#read
import os.path

# file = open("file.txt", 'r')
# # rdline = file.readline()
#
# count = 0
# for l in file:
#     count += 1
# print(count)
# print(rdline)
# rdlines = file.readlines()
# print(rdlines)
# rdfile = file.read()
# print(rdfile)

# file = open("file2.txt","w")
# for number in range(11):
#     file.write(str(number)+'\n')
    # file.write("\n")


# num_words = 0
# fileref = "file.txt"
#
# with open(fileref, 'r') as file:
#     for line in file:
#         num_words += len(line.split())
#
# print("number of words : ", num_words)
# count = 0
# for line in file:
#     count+=1
# print(count)
# import csv
# with open("../check.txt") as f:
#     l = f.readline()
#     new_list= l.split(" ")
    # print(len(new_list))

with open("name_phn.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["name","number"])
    for i in range(len(new_list)):
        split_name_number = new_list[i].split(",")
        csv_writer.writerow(split_name_number)


