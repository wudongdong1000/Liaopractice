'''假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66),
 ('Lisa', 88),('like',87)]
def by_name(t):
    return t[0].lower()
print(sorted(L,key=by_name))
def by_score(t):
    return t[1]
print(sorted(L,key=by_score))
