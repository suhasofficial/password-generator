import random
lower = "abcdefghijklmnopqrstuvwxyz"
# y = lower.lower()
# print(y)
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# x = upper.upper()
# print(x) 
numbers = "0 1 2 3 4 5 6 7 8 9"
symbols = "{ } [ ] ( ) * & ; . , _ - = + & % # @ %"

all = lower + upper + numbers + symbols
length = 16
password =  "".join(random.sample (all,length))
print(password)