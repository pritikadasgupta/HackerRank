#Score is (200 - # of characters in source code)/100

# #Initial solution in Hacker Rank
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

# 9.70 points
[print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i) for i in range(1,101)]