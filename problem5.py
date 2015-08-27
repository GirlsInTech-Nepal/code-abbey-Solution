def getMinArray():

	listArray= [[100,15,1945],[8,254,85],[34,56,87]]
	res=[]
	length= len(listArray)
	print(length)
	i=0
	res=[]
	while i<length:
		minimumList=min(listArray[i])
		res.append(minimumList)
		i+=1
	return res

print(getMinArray())

	


