import math

def crossOff(flags, prime):
    """
    Cross off remaining multiples of prime. Start with (prime*prime),
    because if we have a k * prime, where k < prime, this value would have
    already been crossed off in a prior iteration. */
    """
    for i in range(prime*prime, len(flags), prime):
        flags[i] = False

def getNextPrime(flags, prime):
    """
    Returns next array index with value of True above `prime` index.
    """
    next = prime + 1
    while next < len(flags) and flags[next] == False:
        next += 1
    return next

def sieveOfEratosthenes(max):
    """
    Returns a list of all prime numbers between 1 and max (inclusive).
    """
    # Initialize flags array.
    flags = [True] * max
    flags[0] = flags[1] = False

    prime = 2
    while prime <= math.isqrt(max):
        # Cross off remaining multiples of prime.
        crossOff(flags, prime)

        # Find next value which is True.
        prime = getNextPrime(flags, prime)

    # Return the index of each flag set to True.
    return [idx for idx, val in enumerate(flags) if val]

print(sieveOfEratosthenes(1000000))
