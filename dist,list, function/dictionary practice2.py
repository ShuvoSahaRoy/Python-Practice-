
user_info ={
    'name' : input("Your name: "),
    'age' : input("Your age: "),
    'fav_movie' : input("Your fav movies : ").split(","),
    'fav_songs' : input("Your fav songs: ").split(",")
}

# for i in user_info.items():
#     print(i)

for key, value in user_info.items():
    print("{} : {}".format(key,value))