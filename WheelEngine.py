from ArgTools import ArgParser

# WheelEngine
class WheelEngine: 

	#member vars
	layer1=[10, 7, 15, 8, 3, 6,
			11,6,17,7,3,6,11,11,6,
			9,13,9,7,13,21,17,4,5,7,8,
			11,8,16,2,7,9,7,14,
			11,14,11,14,11,14,14,11,14,11,14,11]
	
	layer2=[7,15,14,9,12,4,
			14,1,12,21,6,15,4,9,18,11,26,
			3,8,9,9,20,12,3,6,14,12,
			9,10,11,12,13,14,15,4,5,67,8]

	layer3=[9,5,10,8,22,16,
			3,12,3,26,6,2,13,9,17,19,
			4,6,6,3,3,14,14,21,21,9,9,4]		
	
	layer4=[6,10,10,1,9,12,
			3,4,12,2,5,10,7,16,8,7,8,8]

	layers=[layer1, layer2, layer3, layer4]

	maxIndex=[len(layer1)-1, len(layer2)-1, len(layer3)-1, len(layer4)-1]
	currIndex=[0,0,0,0]
	
	bInitOK = False

	def __init__(self, args): 
		# startupcode 
		if (self.parseArgs(args)):
			self.bInitOK = True
		else:
			print("WheelEngine: Init failed to parse arguments.")
		
		
	def parseArgs(self, args):
		# return true if args are valid 
		bRval = True 		
		ap = ArgParser(args)
		
		# TODO: Add required command line argument tests here. 
		
		return bRval


	def go(self): 
		# run this 
		x=42 
		bDone = False
		maxSteps = len(self.layer1) + len(self.layer2) + len(self.layer3) + len(self.layer4)
		step = 0 

		while (not bDone): 
			step += 1 

			# check the current setting to see if it totals 42.  Output if so.
			currTotal = self.layer1[self.currIndex[0]] + self.layer2[self.currIndex[1]] \
						+ self.layer3[self.currIndex[2]] + self.layer4[self.currIndex[3]]
			if (currTotal == 42):
				print("T%d = %d %d %d %d" % \
					  (step, self.layer1[self.currIndex[0]], self.layer2[self.currIndex[1]], \
					   self.layer3[self.currIndex[2]], self.layer4[self.currIndex[3]]))

			self.updateIndexes()

			if (step == maxSteps):
				bDone = True 


	def testIndexes(self): 
		# walk the indexes to see if they are incrementing correctly 
		print("max indexes: ", end = " ")
		print(self.maxIndex)
		
		for x in range(40): 
			self.showCurrentIndexes() 
			self.updateIndexes() 
		
		
	def showCurrentIndexes(self): 
		# output the current indexes array values 
		print(self.currIndex) 
		
		
	def updateIndexes(self): 
		# increment the indexes like an odometer 

		bUpdateDone = False 

		for x in range(3,-1,-1):
			if(self.currIndex[x] < self.maxIndex[x]):
				self.currIndex[x] += 1 
				bUpdateDone = True 
				break
			else:
				# this rotor is at max, move the one to the left and reset this one
				if (x>0):
					self.currIndex[x-1] += 1
					self.currIndex[x] = 0
				else: 
					#nothing to the left to increment, reset to all zeros
					self.currIndex=[0,0,0,0]
