#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    
    primelist = [2]
    yield primelist[0]
    guess = 3
    while True:
        if all(guess%primes != 0 for primes in primelist):
            primelist.append(guess)
        if guess == primelist[-1]:
            yield primelist[-1]
        guess += 1
        


                