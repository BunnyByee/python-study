# %%
# %pip install pandas

# %%
import pandas as pd

# %%
growth = pd.Series([143,150,157,160], index=['2018','2019','2020','2020'])
growth

# %%
growth['2020']

# %%
print(growth.values)
print(growth.values[0])

# %%
print(growth.index)
print(growth.index[0])

# %%
growth = pd.Series([143,150,157,160], name='신청')
growth

# %%
growth[0]

# %%
index = ['2018','2019','2020','2021']
Y = pd.Series([143,150,157,160], index=index)
C = pd.Series([165,172,175,180], index=index)
growth = pd.DataFrame({
    '영희' : Y,
    '철수' : C
})
growth

# %%
index = ['2018','2019','2020','2021']
data = {
    '영희' : [143,150,157,160],
    '철수' : [165,172,175,180]
}
growth = pd.DataFrame(data, index=index)
growth

# %%
index = ['2018','2019','2020','2021']
data = {
    '영희' : [143,150,157,160],
    '철수' : [165,172,175,180]
}
growth = pd.DataFrame(data, index=index)

growth['영희'].idxmax()
growth['철수'].idxmin()

# %%
print(growth.dtypes)

# %%
growth.astype('float')

# %%
growth.astype({'영희':'float'})

# %%
pd.read_csv('1.csv')

# %%
pd.read_csv("1.csv", index_col=0) # 0번 컬럼을 인덱스로 쓴다

# %%
growth.to_csv('output.csv')

# %%
index = ['영희', '철수', '영철']
data = {
    '2018' : [143,150,157],
    '2019' : [165,172,175],
    '2020' : [175,125,160]
}
growth = pd.DataFrame(data, index=index)

print(growth)


