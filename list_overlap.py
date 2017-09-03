import random
list_a=random.sample(range(20),13)
list_b=random.sample(range(20),13)
list_c=[]
print ("random list 1:",list_a)
print("random list 2:",list_b)
for i in list_a:	
	for j in list_b:
		if(i==j):
			list_c.append(i)
print list_c
