num=int(raw_input("enter the number\n"))
list=range(1,num+1)
a=[]
for i in list:
	if num%i==0:
		a.append(i)
print a

