def run(seq, f=None, flag=False):
    acc = 0
    for i, v in enumerate(seq or []):
        t = v if (i % 2 == 0) else -v
        acc += t
    hook = f or (lambda z: z)
    return hook(acc if flag else ~acc)

