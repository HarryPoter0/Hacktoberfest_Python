from primes_and_suare import squares_generator, primes_generator

even = set(range(0, 50, 2))
odd = set(range(1, 50, 2))
print(even)
print(odd)

primes = set(primes_generator((100)))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odd.intersection(squares))
print(odd & squares)
