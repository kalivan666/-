to_monitor = {}
def main(to_monitor, k = 0, w = 0, K = 1):
    Kod = input()
    res = ''.join(format(ord(i), 'b') for i in Kod)
    if check(Kod):
        kod = Kod
    else:
        kod = str(res)
    Len_kod = len(kod)
    c = number(to_monitor, Len_kod)
    LenFull = Len_kod + c
    while k <= (LenFull - 1):
        k = k + 1
        I = to_monitor.get(k)
        if I == None:
            a = kod[w]
            to_monitor[k] = int(a)
            w = w + 1
    print(to_monitor)
    n = treatment(c, Len_kod, to_monitor)
    print(n)
    for i in range(c):
        to_monitor[K] = n[K]
        i = i + 1
        K = 2**i
    print(to_monitor)
def treatment(c, Len_kod, to_monitor, i = 1, x = 1, n = None):
    first = {}
    Score = {}
    while i <= c:
        z = 1
        v = 1
        l = 0
        while z <= c + Len_kod:
            if z % x == 0:
                b = z
                while z < x + b:
                    if z <= c + Len_kod:
                        first[v] = to_monitor[z]
                    z = z + 1
                    v = v + 1
            z = z + 1
        len_kod = len(first)
        for m in range(len_kod):
            m = m + 1
            n = first[m]
            if n % 2 != 0:
                l = l + 1
        if l % 2 == 0:
            Score[x] = 0
        else:
            Score[x] = 1
        x = 2**i
        i = i + 1
        first.clear()
    return Score

def number(to_monitor, Len_kod, k = 1, c = 0):
    while k <= Len_kod:
        i = k
        if i <= Len_kod:
            while i <= Len_kod - k + 2:
                to_monitor[i] = None
                i = i + 1
        to_monitor[k] = 0
        k = k * 2
        c = c + 1
    return c

def check(b):
    try:
        int(b)
        return True
    except ValueError:
        return False



if __name__ == '__main__':
    main(to_monitor)
