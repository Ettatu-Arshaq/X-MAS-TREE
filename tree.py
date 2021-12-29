n=eval(input("ENTER THE SIZE OF X'MAS TREE :: "))
sp=10+n
p=1
print('')
print('')
print('')

print(' '*sp+'X'*p+' '*sp)

for i in range(n):
    print(' '*sp+'^'*p+' '*sp)
    sp-=1
    p+=2
else:
    p1=p-7
    p2=p1/2
    sp+=int(p2+2)
    for i in range(6):
        print(' '*sp+'|'*3,' '*sp)
   
