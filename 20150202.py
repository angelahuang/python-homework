#-*- coding: utf-8 -*-
num = ['零','壹','貳','叄','肆','伍','陸','柒','捌','玖'] 
string = ['乘','等於','拾']
for i in range(1,10):
	for j in range(1,10):
		print num[i],string[0],num[j],string[1],
		AA = str(i*j)
		lenAA = len(AA)
		if AA >= 10:
			temp = 0
			for S in AA:
				print num[int(S)],
				temp += 1
				if temp != lenAA:
					print string[2],
		else:
			for S in AA:
				print num[int(S)],
		print
	print '\n'
