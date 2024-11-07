import sys

n = int(sys.stdin.readline().rstrip("\n"))
a = [int(x) for x in sys.stdin.readline().rstrip("\n").split(" ")]
#a[i]: shortcut from i to a[i]

#n=3
#a=[2,2,3]

#n=5
#a=[1,2,3,4,5]

#n=7
#a=[4,4,4,4,7,7,7]

a=[x-1 for x in a] # start from 0 instead of 1
m=[0 for x in range(n)] #m[i]: minimum energy required to go from 1 to i

#b[i]: smallest j such that a[j]>=i
#b=[n-1 for x in range(n)]
#for j in range(n):
#    for i in range(a[j]+1):
#        b[i]=min(b[i],j)



for i in range(1,n):
    m[i] = m[i-1] +1 # go to i-1 and then move to i. Other options might be better
    for j in range(0,i):
        m2= m[j]+1+abs(a[j]-i) # go to j, then shortcut to a[j], then finish without shortcuts.
        m[i] = min(m2,m[i])
        

print(" ".join([str(x) for x in m]),flush=True)





