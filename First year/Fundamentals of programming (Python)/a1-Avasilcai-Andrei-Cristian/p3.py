# Solve the problem from the third set here
def yearstodays(y1: int, y2: int) ->int:
    s = int(0)
    if y1 < y2:
        for i in range(y1 + 1, y2):
            s = s + 365
            if i % 4 == 0:
                s = s + 1
    return s


def monthstodays(d1: int, d2: int, m1: int, m2: int, y1: int, y2: int) ->int:
    l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = int(0)
    if y1 < y2:
        for i in range(m1 + 1, 13):
            s = s + l[i]
        for i in range(1, m2):
            s = s + l[i]
        s = s + (l[m1] - d1) + d2
        if y1 % 4 == 0:
            if m1 > 2:
                s = s + 1
        if y2 % 4 == 0:
            if m2 > 2:
                s = s + 1
    else:
        if y1 % 4 == 0:
            l[2] = 29
        if m1 < m2:
            for i in range(m1 + 1, m2):
                s = s + l[i]
            s = s + (l[m1] - d1) + d2
        else:
            s = s + (d2 - d1)
    return s


def dayslived(d1: int, d2: int, m1: int, m2: int, y1: int, y2: int) ->int:
    s = int(0)
    s = s + yearstodays(y1, y2)
    s = s + monthstodays(d1, d2, m1, m2, y1, y2)
    return s


y1 = int(input("Please insert your birthday -year: "))
m1 = int(input("                            -month: "))
d1 = int(input("                            -day: "))
y2 = int(input("and the current date -year: "))
m2 = int(input("                     -month: "))
d2 = int(input("                     -day: "))
d=dayslived(d1, d2, m1, m2, y1, y2)
if d>=0:
    print("You have lived ", d, " days")
else:
    print("The data you inserted was inaccurate")