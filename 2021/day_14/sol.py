import numpy as np
import collections


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = [[x for x in y.split(" -> ")] for y in data]
inp = data[0][0]
data = {k : v for k,v in data[2:]}


# Part 1
inp_1 = inp
for s in range(10):
    new_inp = ""
    for i in range(len(inp_1)):
        new_inp += inp_1[i]
        if inp_1[i:i+2] in data:
            new_inp += data[inp_1[i:i+2]]
    inp_1 = new_inp

cnt = collections.Counter(new_inp).most_common()
print(cnt[0][1] - cnt[-1][1])


# Part 2
dic = collections.defaultdict(int)
for j in range(len(inp)-1):
    cs = inp[j:j+2]
    dic[cs] = 1 + dic.get(cs, 0)

    
new_dic = dic.copy()
for s in range(40):
    for c, r in data.items():
        if c in dic.keys():
            new_dic[c[0] + r] += dic[c]
            new_dic[r + c[1]] += dic[c]
            new_dic[c] -= dic[c]
    dic = new_dic.copy()

dic_1 = {}
for k, v in dic.items():
    dic_1[k[0]] = dic_1.get(k[0], 0) + v
dic_1[inp[-1]] = dic_1.get(inp[-1], 0) + 1

c = collections.Counter(dic_1).most_common()
print(c[0][1] - c[-1][1])