#amstrong
n = int(input("Enter a number: "))
for num in range(1,n):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        print(num)
