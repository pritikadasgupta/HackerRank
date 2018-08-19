# In a single toss of 2 fair (evenly-weighted) six-sided dice, 
# find the probability that the values rolled by each die will be different 
# AND the two dice have a sum of 6.

# # https://codereview.stackexchange.com/questions/114584/printing-all-possible-sums-of-two-n-sided-dice-rolls
def sumsFromTwoRolls(sides):
    return sorted(a + b for a in range(1, sides + 1) for b in range(1, sides + 1))

# #probability that the sum will have a sum of 6
l = sumsFromTwoRolls(6)
denominator = len(l)


count = 0
for r1 in range(1,7):
	for r2 in range(1,7):
		if r1+r2==6 and r1 != r2:
			count+=1


from fractions import Fraction
Fraction(count, denominator)

print(count/denominator)

#METHOD TWO
sides = 6
dice = 2
l = sumsFromTwoRolls(6)

denominator = sides**dice

n_dieDifferent = 0
for r1 in range(1,7):
	for r2 in range(1,7):
		if r1 != r2:
			n_dieDifferent+=1

#p(A and B) when it's dependent events
# p(equal to 6 AND die are different) = p(die different)*p(equal to 6 | die different)

p_dieDifferent = n_dieDifferent/denominator

p_equalTo6_given_dieDifferent = count/n_dieDifferent

p_result = (p_dieDifferent*p_equalTo6_given_dieDifferent)
p_result



