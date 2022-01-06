def a():
    return('{:>8}'.format('A'))


def b():
    return('{0:>7}{0:>2}'.format('B'))


def c():
    return('{0:>6}{0:>4}'.format('C'))


def d():
    return('{0:>5}{0:>6}'.format('D'))


def e():
    return('{0:>4}{0:>8}'.format('E'))

print(a())
print(b())
print(c())
print(d())
print(e())
print(d())
print(c())
print(b())
print(a())
