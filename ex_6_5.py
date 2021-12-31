text = "X-DSPAM-Confidence:    0.8475"
prenum = text.find("0")
#print(prenum)
posnum = text.find("5")
#print(posnum)
num = float(text[prenum:posnum+1])
print(num)

#another way
text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(":")
print(ipos)
piece = text[ipos+2:]
print(piece)
value = float(piece)
print(value)
