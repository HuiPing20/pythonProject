def josephus_math(n, m):
    if n == 0:
        return 0
    # 初始化最后一个人的位置为0（因为我们的索引是从0开始的）
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + m) % i
    # 因为编号是从1开始的，所以需要将结果加1
    return pos + 1

# 示例调用
n = 150  # 环中的人数
m = 130  # 报数的步长
last = josephus_math(n, m)
print(f"最后剩下的人的编号是: {last}")