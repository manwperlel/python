friends_list = ["jojo", "jojo1", "jojo"]

while True:
    new_friend = input("Enter new friend (or '0' to exit): ")
    
    if new_friend == "0":
        break
        
    friends_list.append(new_friend)
    print(friends_list)