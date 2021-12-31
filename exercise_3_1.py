hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40 :
    print(h * r)
elif h > 40 :
    print(40 * r + ((h-40) * 1.5) * r)

#The right way
    sh = input("Enter hours:")
    sr = input("Enter rate:")
    fh = float(sh)
    fr = float(sr)
    #print(fh, fr)
    if fh > 40 :
        #print("Overtime")
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        #print(reg,otp)
        xp = reg + otp
    else :
        #print("Regular")
        xp = fh * fr
    print("Pay:", xp)
