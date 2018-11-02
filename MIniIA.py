
#dictionary stores how many minutes should be spend doing homework based on the difficutly level (1-10)
hw_diffuclty_weighting = {
        1: 5,
        2: 7,
        3: 10,
        4: 15,
        5: 20,
        6: 25,
        7: 35,
        8: 45,
        9: 55,
        10: 60
        }

#Array to store user replies
replies = []


#Keep on asking what homework you have
def get_hw ():
    total_time = 0
    while True:
        hw = input("List one piece of homeowork you have tonight? If you have no more, write 'None'\n")
        #If they say they have no homework, stop asking
        if (hw == 'None' or hw == 'none'):
            break
        diffuclty = int(input("what is the diffuclty of that homework (1-10)\n"))
        #Get the corrosponding time value from the dictionary based on the difficulty rating
        time = hw_diffuclty_weighting.get(diffuclty)
        #Create a responce
        reply = "You should spend "+ str(time) + " minutes doing your "+ str(hw)
        #Calulate total homework time
        total_time = total_time + time
        #Add to array
        replies.append(reply)
        return total_time

#Print out the responces
def print_array(arr):
    for a in arr:
        print (a)

print ("That means you have " + str(get_hw()) + " minutes of homeowork today\n")

print_array(replies)
