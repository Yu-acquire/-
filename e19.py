l, n, m = map(int, input().split())
rock = [0]
for i in range(n):
    a = int(input())
    rock.append(a)
rock.append(l)


def check(mid):
    remove = 0
    last = 0
    for i in range(1, len(rock)):
        if rock[i] - rock[last] < mid:
            remove += 1
        else:
            last = i
    return remove <= m


left = 1
right = l
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
