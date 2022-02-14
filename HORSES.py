def Horses(x,a):
    min=abs(a[0]-a[1])
    for i in range(0,x-1):
        for j in range(i+1,x):
            t=abs(a[i]-a[j])
            if(min>t):
                min=t
    print(min)            



if __name__=="__main__":
    try:
        t=int(input())
        for i in range(t):
            x=int(input())
            a=list(map(int,input().split()))
            Horses(x,a) 


    except:
        pass    