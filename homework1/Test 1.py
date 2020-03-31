from homework1.Sequence import ArrayList

test =ArrayList(['afhjue', 1, 2, 5.6, 'dd'])
print("count:", test.count('afhjue'))
print("проверка работоспособности__lent__:", len(test))
print("index:", test.index('afhjue'))
print("проверка работоспособности __getitem__:", test[2])
m=test.__contains__(2)
print("проверка работоспособности __contains__ (часть листа):", m)
k=test.__contains__(6)
print("проверка работоспособности __contains__ (не часть листа):", k)
print("проверка работоспособности __inter__:", iter(test))
test1=ArrayList([1,2])
print("проверка работоспособности __reversed__:", list(reversed(test1)))

