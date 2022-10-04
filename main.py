def factorial(n) :
    S=1
    for i in range(1,n+1) :
        S*=i
    return S
print(factorial(4))