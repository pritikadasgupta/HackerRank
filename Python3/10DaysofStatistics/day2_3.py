# There are  urns labeled X, Y, and Z. 


# Urn X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 4 red balls and 4 black balls. 

# One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?


def drawOneFromUrn(numRed,numBlack,color):
	if color == "Red":
		pRed = numRed/(numRed+numBlack)
		return pRed
	elif color == "Black":
		pBlack = numBlack/(numRed+numBlack)
		return pBlack

# p(R,R,B) can happen in many diff ways from Urn X,Y, and Z

# p(RRB) = p(Rx)*P(Ry)*P(Bz) + P(Rx)*P(By)*P(Rz) + P(Bx)*P(Ry)*P(Rz)

p_Rx = drawOneFromUrn(4,3,"Red")
p_Bx = drawOneFromUrn(4,3,"Black")

p_Ry = drawOneFromUrn(5,4,"Red")
p_By = drawOneFromUrn(5,4,"Black")

p_Rz = drawOneFromUrn(4,4,"Red")
p_Bz = drawOneFromUrn(4,4,"Black")

p_RRB = p_Rx*p_Ry*p_Bz + p_Rx*p_By*p_Rz + p_Bx*p_Ry*p_Rz
p_RRB