""" Function to return prime numbers between 2 and 100 """


def is_prime(number):
    """ Asserts if number is prime.
    
    Parameter
    ---------

    number: int
        Number to assert

    Return
    ------

    boolean
        True if number is prime

    """
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def get_primes(limit):
    """ Return a list with the primes numbers between 2 and 'limit'.
        
        Parameter
        ---------

        limit: int
            Limit number

        Return
        ------

        list(int)
            List with primes number in given limit.

    """
    primes_list = [number for number in range(2, limit + 1) if is_prime(number)]
    return(primes_list)

print(get_primes(100))
