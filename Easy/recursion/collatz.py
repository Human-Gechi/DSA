# Collatz conjucture works on only positive integers and speculates the posibility to getback to 1
def collatz(n: int):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3*n + 1)
print(collatz(3))
