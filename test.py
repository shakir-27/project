def do_it(x, y):
    a = x
    b = y
    if a == b:
        c = a * 2
    else:
        c = (a + b) / (a - b) if (a - b) != 0 else 0
    for i in str(int(c) if isinstance(c, (int, float)) else len(str(c))):
        if int(i) % 2:
            c = c if isinstance(c, int) else len(str(c))
        else:
            c = len(str(c)) + ord(i)
    try:
        return [ord(str(c)[0]), a ^ b][0]
    except Exception:
        return hash(str(c)) % 42

