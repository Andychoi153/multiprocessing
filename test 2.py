import time
import multiprocessing as mp

def factorial(N) :
    fac = 1
    for i in range(1,N+1) :
        fac*=i
    return fac


def cube(x) :
    return x**3

def main() :
    pool = mp.Pool(processes=4)
    start = time.time()
    results = pool.map(factorial, [50000,50000,50000])
    print ("time 1 = %s"%(time.time()-start))

if __name__ == '__main__':
    main()