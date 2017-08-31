num=int(raw_input(' enter a number\n'))
check=int(raw_input("enter diviser\n"))
if num==0:
	print 'is not a valid entry'
else:
	if num%2 == 0:
		print "num is even"
	else:
		print "num is odd"
	if num%4 == 0:
		print "num is multiple of 4"
	else:
		print "num is not multiple of 4"
	y=num % check
	if (y == 0):
		print 'num %s is evenly divided by check %s'%(num,check)
	else:
		print 'num %s is not evenly divided by check %s'%(num,check)
