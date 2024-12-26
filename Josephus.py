def find_last_remaining(n, m):
    if n == 0:
        return 0

    # 创建一个列表来表示环中的元素
    circle = list(range(1, n + 1))

    index = 0  # 开始报数的位置

    while len(circle) > 1:
        # 计算当前要移除的元素的索引
        index = (index + m - 1) % len(circle)
        # 移除该元素
        circle.pop(index)

    # 返回最后剩下的元素
    return circle[0]


# 示例调用
n = 7  # 环中的人数
m = 3  # 报数的步长
last = find_last_remaining(n, m)
print(f"最后剩下的人的编号是: {last}")