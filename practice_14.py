#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return filter(pde,n)
def pde(n):
    return str(n)==str(n)[-1::-1]
print(list(is_palindrome(range(1,1000))))