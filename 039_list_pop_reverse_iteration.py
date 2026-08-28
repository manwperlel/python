list1 = [12, "hello", "cristhian" ]
print(list1)
for i in range(len(list1)-1, -1, -1):
    if list1[i] == "hello":
        print(list1.pop(i))

print(list1)