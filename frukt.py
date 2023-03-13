import random 


def print_fruit(userinput):
   fnr = int(userinput) 
   print("\n" + frukter [fnr-1]+"kommer här!" )

frukter = ("Päron", "äpple", "banan") 

looping = True

while looping:

    print("-------------------\n")
    print ("\n-:fruktautomat.-\n")
   
    i = 1
   
    for frukt in frukter: 
        print (str(i) + ": " +frukt)
        i+=1
   
    fruktnr = input ("\n mata in siffra för vald frukt:")

    print_fruit(fruktnr)
        
    go = input("vill du välja en frukt till j/n? ")

    
    if (go == "n"):
        break


print("\n------------------\n")   

print ("föresten: ")

slumpfrukt = random.randint(1,5)
print_fruit(slumpfrukt)