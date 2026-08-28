guest_list = []

while True:
    guest_name = input("Enter a guest name (or '0' to finish): ")

    if guest_name == "0":
        break

    guest_list.append(guest_name)

print("===================================================================")

for guest in guest_list:
    print(f"Guest: {guest}")