# 定义元组
t1 = (1, 'tt', True)
t2 = ()
t3 = tuple()

# 定义单个元素元组
# 如果要定义单个元素的元组，后面要加一个 逗号
t4 = ('Tt', )

# 定义嵌套元组
t5 = ((0, 1, 2), (3, 4))

# 根据下标取出元组
res = t5[1][0]  # 3
print(res)
