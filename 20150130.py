#-*- coding: utf-8 -*-
num = ['零','壹','貳','叄','肆','伍','陸','柒','捌','玖'] 
string = ['乘','等於']
for i in range(1,10):
	for j in range(1,10):
		#print num[i],string[0],num[j],string[1],num[i*j]
		print num[i],string[0],num[j],string[1],
		AA = (i*j)
		for S in str(AA):
			print num[int(S)],
		print
	print '\n'
