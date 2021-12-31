counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
        words = line.split(" ")
        email = words[1]
        #print(emails)
        if email not in counts:     #se o e-mail não tiver no dicionário
            counts[email] = 1       #adicionar
        else:
            counts[email] = counts[email] + 1       #contar
#print(counts)
bigcount = None     #maior número de vezes
bigemail = None     #e-mail mais frequente
for email, counts in counts.items():    #dentro de counts (dict), checando key and value e se for maior é o novo maior.
    if bigcount is None or counts > bigcount:
        bigemail = email
        bigcount = counts
print (bigemail, bigcount) #printar o e-mail mais frequente e o número de vezes que aparece
