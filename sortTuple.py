mdata = [(222,[30,4]), (333,[50,2]), (120,[20,8]), (10,[10,7]), (20, [9,9])]

print(mdata)
res = sorted(mdata, key=lambda e: e[1][1], reverse=False)
print(res)
