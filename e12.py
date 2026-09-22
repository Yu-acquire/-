cnt = [0] * 26
for _ in range(4):
    line = input()
    for ch in line:
        if 'A' <= ch <= 'Z':
            idx = ord(ch) - ord('A')
            cnt[idx] += 1
max_h = max(cnt)
for height in range(max_h, 0, -1):
    row = []
    for num in cnt:
        if num >= height:
            row.append('*')
        else:
            row.append(' ')
    print(' '.join(row))
letters = [chr(ord('A') + i) for i in range(26)]
print(' '.join(letters))