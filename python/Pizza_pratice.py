pn,t2,t3,t4=map(int,input().split(" "))
x,y,z=t2,t3,t4
teams=[[2]*t2,[3]*t3,[4]*t4]
pizza=[None]*pn
for i in range (pn):
    pizza[i]=list(map(str,input().split(" ")))
print(pizza)
count=0
diff=(sum(teams[0])+sum(teams[1])+sum(teams[2]))-pn
while (diff>0):
        if (diff>=4 and teams[2]!=None):
            diff-=4
            count+=1
            z-=1
        elif (diff>=3 and teams[1]!=None):
            diff-=3
            count+=1
            y-=1
        elif (diff>=0 and teams[0]!=None):
            diff-=2
            count+=1
            x-=1
        else:
            break
            
  
print((len(teams[0])+len(teams[1])+len(teams[2]))-count)
print(x,y,z)
