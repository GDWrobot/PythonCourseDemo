# 单行输出1000以内的斐波那契数列：
a, b = 0, 1  # 定义前两个数
while a < 1000:  # 循环
    print(a, end=' ')  # 输出a的值，空格结尾不换行
    a, b = b, a + b  # 计算后一个数，更新a和b的值
