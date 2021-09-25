i=int(input("How many hours you worked:"))
if(i>=40):
    if(i>60):
        y=i-60
        sal=(10*40)+(10*20*1.5)+(10*2*y)
        print("Your salary is:",sal)
    else:
        x=i-40
        sal=(10*40)+(15*x)
        print("Your salary is:",sal)
else:
    print("The salary cannot be generated\a")

