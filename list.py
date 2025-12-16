names = ['Emmanuel', 'Tersoo', 'Favour','Fasola']
#print(names[1:3])
names.pop()
names.append('Terna')

for name in names:
    print(name)
    if name == 'Favour' :
        print('found Favour!')
        break
