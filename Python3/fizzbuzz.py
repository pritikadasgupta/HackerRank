#Score is (200 - # of characters in source code)/10

# #Initial solution in Hacker Rank
# # 2 points
# i=1
# while i <= 100:
#     if i%3==0:
#         print("Fizz", end="")
#         if i%5==0:
#             print("Buzz", end="")
#     elif i%5==0:
#         print("Buzz", end="")
#     else:
#         print(i, end="")
#     print()
#     i+=1


# # 9.40 points
# for i in range(1,101):
#     print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i)

# # 9.70 points
# [print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i) for i in range(1,101)]

# # 13.4 points
# [print("Fizz"*(i%3==0)+(i%5==0)*"Buzz"or i) for i in range(1,101)]

# 13.6 points
for(i)in range(1,101):print("Fizz"*(i%3==0)+(i%5==0)*"Buzz"or i)

# # 13.5 points
# [print("Fizz"*(i%3==0)+(i%5==0)*"Buzz"or i)for(i)in range(1,101)]