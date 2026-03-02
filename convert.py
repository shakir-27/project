with open('test1.py', 'r', encoding='utf-8') as f:
    content = f.read()

with open('test1_utf16.py', 'w', encoding='utf-16') as f:
    f.write(content)

print("Converted to test1_utf16.py")

