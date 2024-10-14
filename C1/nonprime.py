lower=int(input("Enter a lower limit"));
upper=int(input("Enter an upper limit"));

for n in range (lower, upper+1):
    if ( n > 1):
        for i in range (2,n):
            if (n % i == 0):
                print(n)
                break
