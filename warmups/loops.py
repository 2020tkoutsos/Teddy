
arr = [1,2,3,4,5]
i_highest = 0
o_highest = 0
for outter in arr:
    if i_highest > o_highest:
        o_highest = i_highest
        print("i am o_highest", o_highest)
    print('I am outter', outter)
    for inner in arr:
        if inner > outter:
            highest = inner
            print('I am highest', i_highest)
