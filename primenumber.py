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

prime_is()
