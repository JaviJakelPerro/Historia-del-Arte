def fibonacci (n):
    if n <= 0:
        return "El numero deebe ser positivo"
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range (2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence
            
print(fibonacci(10))