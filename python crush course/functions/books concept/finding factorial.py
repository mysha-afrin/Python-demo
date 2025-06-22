def fact(n):
    if(n == 0 or n == 1):
        return 1
    
    return fact(n-1) * n
print(fact(int(input("Enter a number that you have in your mind : "))))
