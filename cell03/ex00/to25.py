num = int(input("Enter a number less than 25"))
if num > 25:
    print("Error")
else:
    while num <= 25:
        if num > 25:
            break
        print("Inside the loop, my variablr is", num)
        num += 1