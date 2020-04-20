#a = [('u','n'),('g','a'),('r','y'),('h','u'),('n','g'),('a','r')]
a = [("R","U"),("A","R"),("U","N")]
d={}
for i in a:
    d[i[0]] = i[1]

print(d)

i=0
while len(d)!=1:
    m = list(d.keys())[i]
    n = d[m]
    while n in d:
        d[m]+=d[n]
        del d[n]
        n=d[m][-1]
    i+=1
out = ''.join(map(''.join, d.items()))
print(out)


