# Solve the problem from the first set here
def determinezeros(n: int) -> int:
    zeros = int(0)
    while n > 0:
        if n % 10 == 0:
            zeros = zeros + 1
        n = int(n / 10)
    return zeros


def detminnumber(n: int) -> int:
    l = []
    cn = n
    while n > 0:
        if n % 10 != 0:
            l.append(n % 10)
        n = int(n / 10)
    l.sort()
    m = l[0]
    l.pop(0)
    zeros = determinezeros(cn)
    while zeros > 0:
        m = m * 10
        zeros = zeros - 1
    length = len(l)
    for i in range(length):
        m = m * 10 + l[i]
    return m


n = int(input("What should the 'n' number be? "))
if n == 0:
    print("The minimal number made out of n's digits is: 0")
else:
    m = detminnumber(n)
    print("The minimal number made out of n's digits is: ", m)
