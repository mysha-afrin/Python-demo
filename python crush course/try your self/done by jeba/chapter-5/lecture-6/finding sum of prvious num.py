#Writ a recursive function to calculate the sum of first n natural numbers.
def sum_num(n):
    if(n == 0):
        return 0
    return (n - 1) + n
print(sum_num(int(input("Enter a number : "))))
