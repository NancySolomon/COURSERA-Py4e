








s="+-*/()"
s=list(s)
alpha=[]
op=[]
b=[]
for i in range(len(s)):
    if s[i].isalpha():
        alpha.append(s[i])
    elif s[i]=="(" or ")":
        b.append(s[i])
    else:
        op.append(s[i])
op.sort()
for i in s
