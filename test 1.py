import time

def factorial(N) :
    fac = 1
    for i in range(1,N+1) :
        fac*=i
    return fac
    




def main() :
    n = 50000
    k = 50000
    j = 50000

    
    start = time.time()
    results = [factorial(n),factorial(j),factorial(k)]
    print ("time 1 = %s"%(time.time()-start))

if __name__ == '__main__':
    main()