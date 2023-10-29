def look(s):
    result = []
    i = 0
    while i < len(s):
        cont = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            cont += 1
            i += 1
        result.append(str(cont) + s[i])
        i += 1
    return ''.join(result)

s = '1'
n = 10
for i in range(n):
    print(s)
    s = look(s)

   