def srz(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum/len(args))
print(srz(1,2,3,4,5))

