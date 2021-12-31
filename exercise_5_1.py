#Total count and average
num = 0
tot = 0.0
while True :
    sval = input("Enter number: ")
    if sval == "done" :
        break
    try :
        fval = float(sval)
    except :
        print ("Invalid input")
        continue
    # print(fval)
    #counter pattern
    num = num + 1
    #accumuler pattern
    tot = tot + fval

# print("All done!")
print(tot,num,tot/num)
