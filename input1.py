name=raw_input("enter the name\n")
age=int(raw_input("enter age\n"))
print "Name of the person is: " ,name
print "and age is: ", age
y=100-age
import datetime
now=datetime.datetime.now()
year=now.year+y
#print year
print 'By the year ', year,' ' ,name, "turned to 100 years"
