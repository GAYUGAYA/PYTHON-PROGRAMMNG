st=int(raw_input())
if(st%4==0):
	if(st%100==0):
		if(st%400==0):
			print('leap year')
		else:
			print('not a leap year')
	else:
		print('leap year')
else:
	print('not a leap year')
