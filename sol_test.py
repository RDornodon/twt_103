_,*A=open(0)
while A:a,b,*A=A;b=b[:-1];print(sum(a[_:_+len(b)]==b for _ in range(len(a))))