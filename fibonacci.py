def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()

counter = 0
for x in f:
    if (x > 10): break
    print x,

print