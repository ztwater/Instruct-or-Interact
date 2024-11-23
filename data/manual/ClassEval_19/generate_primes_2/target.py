class ChandrasekharSieve:
    def generate_primes(self):
        primes = []
        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False
    
        for num in range(2, int(self.n ** 0.5) + 1):
            if sieve[num]:
                primes.append(num)
                for multiple in range(num * num, self.n + 1, num):
                    sieve[multiple] = False
    
        for num in range(int(self.n ** 0.5) + 1, self.n + 1):
            if sieve[num]:
                primes.append(num)
    
        return primes