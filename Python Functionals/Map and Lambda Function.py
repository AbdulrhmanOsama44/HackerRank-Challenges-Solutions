cube = lambda x: x ** 3

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        
    return fibonacci_sequence[ : n]