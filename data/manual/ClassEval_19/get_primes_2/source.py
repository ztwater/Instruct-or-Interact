class ChandrasekharSieve:
    def get_primes(n):
        primes = []
        for num in range(2, n+1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes