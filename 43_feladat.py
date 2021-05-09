def s_lista(s):
    ls=[]
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            ls+=[s[i:j]]
    ls.sort(key=len)
    return ls

def benne(ls,t):
    tartalmaz=True
    for i in ls:
        for k in t:
            if k not in i:
                tartalmaz=False
        if tartalmaz==True:
            return i
        tartalmaz=True
    return ""

s=input("s=")
t=input("t=")
ls=s_lista(s)
print(ls)
print(benne(ls,t))