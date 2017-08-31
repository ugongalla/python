def fun(aa):
	print "this is function definition"
a=[1,2,-3,4,9,8,10,3,-1,7]
new=[]
fun(a)
for i in a:	
	if (i<5):
		new.append(i)
	
print ("list containing numbers less than 5:",new)
 
