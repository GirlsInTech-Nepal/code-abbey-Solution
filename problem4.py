def arrayDifferenceLoop():

	a= [100,15,1945]
	b=[8,254,85]
	length = len(a)
	print(length)
	i=0
	res=[]
	while i<length:

		c=a[i]-b[i]
		res.append(c)
		i+=1
	return res


print(arrayDifferenceLoop())




