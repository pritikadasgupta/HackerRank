#Cards of the Same Suit
# You draw 2 cards from a standard 52-card deck without replacing them. 
# What is the probability that both cards are of the same suit?

# first draw
# 52 cards

# second draw:
# 51 cards 

# the possible combinations:
# 52*51

# there are 13 cards per suit, since we picked 1 of them in the first draw, then there are 12 possibilities
# 52*12

p = (52*12)/(52*51)
# p = 12/51