count = 0  # 计数器，控制每行输出个数
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1
        # 满10个换行
        if count % 10 == 0:
            print()