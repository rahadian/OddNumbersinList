numberz=0,1,3,5,8,10
#numberz=0,2,4,6,8,10
a=0
list=[]
list2=[]
list.extend(numberz)
print list
print "Ganjil:"
#Ganjil = list[a]%2==1
#if Ganjil == True:
for i in list:
	if list[a]%2==1:
		list2.append(i)
		print list2
	else:
		print "-1(Tidak ada bil.Ganjil"
	a+=1
print "Bilangan Ganjil = ",list2
def sum(list2):
	sum=0
	for i in list2:
		sum=sum+i
	return sum
print "Jadi penjunmlahan index bil.ganjil adalah",sum(list2)