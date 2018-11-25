l = [[[(30, 25), 5], 10], [[(31, 25), 5], 10], [[(32, 25), 5], 10], [[(33, 25), 5], 10], [[(34, 25), 5], 10], [[(50, 25), 5], 10], [[(51, 25), 5], 10], [[(52, 25), 5], 10], [[(53, 25), 5], 10], [[(54, 25), 5], 10]]

x = 0
listaza = []
for n in l:
    if x ==0:
        listo =[]
        x =  (list((n[0])[0])[0])
        listo.append(n)
    elif (list((n[0])[0])[0]) == x+1:
        print (n)
        listo.append(n)
        x =  (list((n[0])[0])[0])
    elif (list((n[0])[0])[0]) != x+1:
        listaza.append(listo)
        listo =[]
        listo.append(n)
        x =  (list((n[0])[0])[0])
if listo not in listaza:listaza.append(listo)

for l in (listaza):
    print (l)