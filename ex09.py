def eh_primo(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def primos_ate(n):
    return [x for x in range(2, n + 1) if eh_primo(x)]

print(primos_ate(50))