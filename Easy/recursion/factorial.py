
# Note python default recursive nuumber calls is 100 anything above that raises a recursive limit error

# ---- Iterative method ------
def fact(n):
    if n == 1 or n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(fact(100))


def fact(n):
    if n == 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
print(fact(100))

# --- Recursive method ----
def fact(n):
    if n < 0:
        return -1
    elif n ==1 or n == 0:
        return 1
    else:
        return n * fact(n -1)

print(fact(100))
