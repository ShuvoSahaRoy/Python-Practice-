with open("channel list.txt", 'r+', newline='') as file:
    lines = file.readlines()

    for line in lines:
        temp = line.split()
        newLine = "https://www.youtube.com/channel/" + temp[0] + "/about"
        rline = temp[0].replace(temp[0],newLine)
        print(rline)
