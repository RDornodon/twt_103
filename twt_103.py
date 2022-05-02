def find_all(text, part):
    value = 0
    plen = len(part)
    while len(text) >= plen:
        if text[:plen] == part:
            value += 1
        text = text[1:]
    return value


for _ in range(int(input())):
    print(find_all(input(), input()))
