from math import sqrt
N=7*10**6
prime=[0]*N
phi=[0]*N
vst=[0]*N
phi[0],phi[1]=0,1
p=10**9+7
num=0

for i in range(2,N):
    if(not vst[i]):
        prime[num]=i
        phi[i]=i-1
        num+=1
    j=0
    while(prime[j]*i<N and j<num):
        vst[prime[j]*i]=1
        if(i%prime[j]):
            phi[i*prime[j]]=phi[i]*(prime[j]-1)%p
        else:
            phi[i*prime[j]]=phi[i]*prime[j]%p
            break
        j=j+1

sphi=[0]*N   
sphi[1]=1
for i in range(1,N):
    sphi[i]=sphi[i-1]+phi[i]*i*i
    sphi[i]%=p
cache={}
def g(n):    
    if n<N:
        return sphi[n]
    elif n in cache:
        return cache[n]
    else:
        v=int(sqrt(n))
        s1=0
        for x in range(1,v+1):
            a=n//x
            b=n//(x+1)+1
            s1=s1+g(x)*(1+a-b)*(a+2*a*a-b+2*b*a+2*b*b)//6%p
        s2=0
        for i in range(2,n//(v+1)+1):
            s2=s2+i*i*g(n//i)
        t=(n*(n+1)//2)**2-s1-s2
        cache[n]=t
    return t

def sum1(x):
    return x*(x+1)//2

n=int(input())
s=0
i,j=1,0
while j<n:
    j=n//(n//i)
    s=s+g(n//i)*(sum1(j)-sum1(i-1))
    s=s%p
    i=j+1
print(s)
