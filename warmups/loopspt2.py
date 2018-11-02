arr = [11,1,10,3,4,5,3,3,22,3]
# create a var to hold answer
repeat = 0
# start a nested loop for comparing
for outter in arr:

    for inner in arr:
        if outter == inner:
            repeat = repeat + 1
print(repeat)
