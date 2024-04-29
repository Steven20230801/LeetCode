def check_is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


check_is_prime(2)
check_is_prime(3)
check_is_prime(4)
check_is_prime(5)
check_is_prime(6)
