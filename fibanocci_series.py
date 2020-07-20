def fibanocci(n):
    if n <= 1:
        return n
    else:
        return (fibanocci(n-1) + fibanocci(n - 2))
n = int(input("enter the number: "))
if n <= 0:
    print("Enter a number greater than zero")
else:
    print("The Fibanocci series is :")
    for i in range(n):
        print(fibanocci(i))
    
    
