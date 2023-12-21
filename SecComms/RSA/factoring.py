from primefac import primefac

numbertofactorize = 510143758735509025530880200653196460532653147

# Using primefac to factorize number
factors = list(primefac(numbertofactorize))

# Display factors
print("Factors:", factors)


smallest_prime = min(factors)
print("Smallest Prime:", smallest_prime)
