#-*- coding: utf-8 -*-
num = ['零','壹','貳','叄','肆','伍','陸','柒','捌','玖'] 
string = ['乘','等於','拾']
for i in range(1,10):
	for j in range(1,10):
		print num[i],string[0],num[j],string[1],
		lenAA = len(str(i*j))
		temp = 0
		for S in str(i*j):
			print num[int(S)],
			temp += 1
			if temp != lenAA:
				print string[2],
		print
	print '\n'
	
	
	
	
	#============================== Kent 做法 =================================
num = ['零','壹','貳','叄','肆','伍','陸','柒','捌','玖'] 
string = ['乘','等於','拾']
for i in range(1,10):
	for j in range(1,10):
		print num[i],string[0],num[j],string[1],
		AA = str(i*j)
		if i*j >= 10:
			print num[int(AA[0])],
			print string[2],
			print num[int(AA[1])],
		else:
			print num[int(AA[0])],
		print
	print '\n'
