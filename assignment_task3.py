numbers = (55, 22, 33, 2, 3, 6, 9, 19, 8, 3, 1, 4, 27, 31, 16, 18, 15, 32)
count_odd = 0
count_even = 0
for x in numbers :
    if not x % 2 :
             count_even+=1
    else:
        count_odd+=1
print("NUMBER OF EVEN NUMBERS -",count_even)
print("NUMBER OF ODD NUMBERS _", count_odd)