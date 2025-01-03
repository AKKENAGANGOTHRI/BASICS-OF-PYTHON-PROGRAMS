def muu_tables(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"x",j,"=",(i*j))
n=int(input("enter the number:"))    
muu_tables(n)