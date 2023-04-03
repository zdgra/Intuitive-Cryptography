# written by zachariah abueg
# cis 3362, fall 2021
# homework 5, question 7
# 10/16/21



# we first get our input

n = int(input("Enter an integer from 2 to 300,000,000.\n"))

# this is the number, k, that will minimize ϕ(k)/k for all k between 2 and n
# we initialize it to 1 because we will have k multiply itself by successive primes

k = 1

# this will hold the prime factors of k
# it will be used to calculate ϕ(k)

kPrimeFactors = []

# this will hold the primes that multiply all the way up to the greatest possible input
# since the greatest possible input in our case is 3 * 10^8, we find the greatest product
# that is less than or equal to 3 * 10^8, which is 2 x 3 x 5 x 7 x 11 x 13 x 17 x 19 x 23
# we add 29 just to be safe

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]



def phi(primeFactors):

    """input: the prime factors of a number whose prime factorization only has exponents of 1, in a list
       output: euler's totient function of that number, as an integer
       method: given a number, A, whose prime factorization is A = p_1 x p_2 x ... x p_m, we use the
               multiplicativity of the euler totient function and the fact that ϕ(p) = p - 1 for primes p to get
               ϕ(A) = ϕ(p_1 x p_2 x ... x p_m) = ϕ(p_1) x ϕ(p_2) x ... x ϕ(p_m) = (p_1 - 1) x (p_2 - 1) x ... x (p_m - 1)
               thus, for k, we start with 1 and successively multiply it by (p - 1) for each prime factor p of k"""
               
    val = 1
    for factor in primeFactors:
        val *= (factor - 1)
    return val
    
    

def gcd(a, b):

    """input: two positive integers, 'a' and 'b'
       output: the greatest common divisor, or factor, of 'a' and 'b'
       method: euclidean algoritm, using recursion"""
       
    if a == 0:
        return b
    return gcd(b % a, a)
    
    

# k will multiply itself by successive primes until it is greater than n,
# at which point we return ϕ(k)/k in lowest terms
# phi() is used to calculate ϕ(k)
# gcd() is used to reduce the fraction
# if k times the next prime is still less than or equal to n,
# then carry on with that product and add the prime to k's list of prime factors

for prime in primes:
    if k * prime > n:
        phi = phi(kPrimeFactors)
        gcd = gcd(k, phi)
        print("f(" + str(n) + ") = " + "ϕ(" + str(k) + ")/" + str(k) + " = " + str(phi) + "/" + str(k) + " = " + str(int(phi / gcd)) + "/" + str(int(k / gcd)))
        break
    k *= prime
    kPrimeFactors.append(prime)

