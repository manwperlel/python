friends = []

while True:
    new_friend = input("Insert new friend (or '0' to stop): ")

    if new_friend == "0":
        break

    position = int(input("Insert target index position: "))
    friends.insert(position, new_friend)

print("===================================================================")

for friend in friends:
    print(friend)