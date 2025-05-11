# %%
import numpy as np

a = np.array([[1,2],[3,4]])

expanded = np.expand_dims(a, 0)
print(expanded)
print(expanded.shape)

# %%
np_ones = np.ones((1,2,1,3))
print(np_ones)
print(np_ones.shape)

# %%
sq = np.squeeze(np_ones)
print(sq)
print(sq.shape)

# %%
a = [1,2,2,3,3,4,3,2,4,1]

u_a, counts = np.unique(a, return_counts = True)
print(u_a)
print(counts)

# %%
a = [1,2,2,3,3,4,3,2,4,1]

u_a, indexs = np.unique(a, return_index = True)
print(u_a)
print(indexs)

# %%
a = [1,2,2,3,3,4,3,2,4,1]
# unique(index를 먼저 쓰던 count를 먼저 쓰던 출력은 index부터)
u_a, indexs, counts = np.unique(a, return_index = True, return_counts = True)
print(u_a)
print(indexs)
print(counts)

# %%
a = np.array([1,4,2,3])
b = np.sort(a) # a[np.argsort(a)]
print(f'a {a}')
print(f'b {b}')
c = np.argsort(a)
print(f'c {c}')
print(f'cc {a[c]}')
a.sort()
print(f'a {a}')

# %%
a = np.array([1,4,2,3])
np.mean(a)

# %%
np.std(a)

# %%
np.var(a)

# %%
np.max(a)

# %%
np.min(a)

# %%
np.median(a)

# %%
a = [1,1,2,3,4,5,5,5,5,7,8,9,10,11,24,100]
# 1번
uq = np.unique(a)
print(uq)

# %%
# 2번
print(np.max(uq))
print(np.min(uq))
print(np.mean(uq))

# %%
# 3번, 4번
print(np.sum(uq))
print(np.median(a))

# %%
x = np.arange(15, dtype= np.int64).reshape(3,5)
x[1:, ::2] = -99

print(x)

# %%
print(np.max(x[:,0]))
# np.max(x,axis=0)[0]
print(np.min(x[:,0]))
print(np.mean(x[:,0]))

# %%
print(np.sum(x[1]))
# print(np.sum(x, axis=1)[1])

# %%
a = np.array([1,1,2,3,4,5,5,5,5,7,8,9,10,11,24,100])
b = np.argsort(a)[::-1]
print(a[b])


