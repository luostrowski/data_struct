fname = input("Enter file name: ")
fh = open(fname)
lst = list()                            # list for the desired output
for line in fh:                         # to read every line of file romeo.txt
    fline = line.rstrip()               # to eliminate the unwanted blanks
    pieces = fline.split()              # turn the line into a list of words
    for element in pieces :             # check every element
        if element in lst :             # if element is repeated
            continue                    # do nothing
        else :                          # else if element is not in the list
            lst.append(element)         # append
lst.sort()                              # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)                              # print the list
