from math import sqrt

def is_prime(nb):
    if nb == 2 and nb == 3:
        return True
    elif nb % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(nb)), 2):
            if nb % i == 0:
                return False
        return True

def main():
    primes = []
    notPrimes = []

    for i in range(50):
        if is_prime(i):
            primes.append(i)
        else:
            notPrimes.append(i)
    
    print(f"Nombre premiers : {primes}")
    print(f"Nombres non premiers : {notPrimes}")

main()