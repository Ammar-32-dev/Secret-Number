secret_number=6
count=0
trials=3

while count<trials:
    user=int(input("Enter any number: "))
    count +=1
    if user==secret_number:
        print("U Won")
        break
else:
    print("Sorry you lost")
