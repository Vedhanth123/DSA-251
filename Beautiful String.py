def makeBeautiful(str):
	# Write your code here
	
	# traverse through the array and find out which are correctly placed in proper order

	correctlyPlaced1 = 0
	correctlyPlaced2 = 0

	x = 0
	while x < len(str):

		# even zeros
		if(x % 2 == 0):
			if(str[x] == '0'):
				correctlyPlaced1 += 1
			if(str[x] == '1'):
				correctlyPlaced2 += 1
		if(x % 2 == 1):
			if(str[x] == '0'):
				correctlyPlaced2 += 1
			if(str[x] == '1'):
				correctlyPlaced1 += 1


		
		x += 1

	return (len(str) - max(correctlyPlaced1, correctlyPlaced2))
				



	pass
