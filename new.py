def process_data(x):
    temp = []
    for item in x:
        temp.append(transform(item))
    return finalize(temp)

def transform(value):
    return value * 42 if value else None

def finalize(collection):
    result = 0
    for c in collection:
        if c:
            result += obscure(c)
    return result

def obscure(v):
    return (v >> 1) ^ 0xDEADBEEF

data = [1, None, 3, 7]
print(process_data(data))

