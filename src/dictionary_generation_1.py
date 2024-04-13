n=5
# dic = dict.fromkeys(range(5), i*i for i in range(n+1))
dic={i:i*i for i in range(5)}

print(dic)
d=dict()

for i in range(5):
    d[i]=i*i
print(d)