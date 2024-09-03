def prime_is():    
    prime=[]
    nmax=int(input("NEnter"))
    for i in range(2, (nmax+1)):
        is_prime=0
        if len(prime)==0:
            prime.append(i)
        elif len(prime)!=0:
            for j in prime:
                if i%j==0:
                    is_prime+=1  
                elif i%j!=0:
                    pass
            if is_prime==0:
                prime.append(i)
    print(prime)
def is_prime():
    count=0
    n=int(input("Enter starting range: "))
    m=int(input("Enter the ending range"))
    for i in range(n,m):
        for j in range(2,i):
            if i%j==0:
                count +=1
            if count ==2:
                print(i,"is not a prime number")

prime_is(   )

