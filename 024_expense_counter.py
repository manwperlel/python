print("================================================================")
print("==================== { EXPENSE COUNTER } =======================")
print("================================================================\n")

balance = int(input("Enter the opening balance: "))
spent = 0
counter = 0
total = 0
cut = "not"

while cut == "not":
    print("Available balance:", balance)
    spent = int(input("Enter the expense: "))


    balance = balance - spent
    counter = counter + 1
    total = total + spent


    if balance < 0:
        print("The expense is greater than the available balance.")
        balance = balance + spent
        counter = counter - 1
        total = total - spent
    elif spent == 0:
        cut = "yes"
        counter = counter - 1

print("========================{ FINAL LIST }=========================")
print("The total expenses are:", total)
print("The number of expenses performed is:", counter)
print("================================================================")