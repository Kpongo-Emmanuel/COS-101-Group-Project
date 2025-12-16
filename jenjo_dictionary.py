jenjo_dict = {'tree':'booksh', 'chair':'morio', 'cat':'nak', 'dog':'mush', 'air':'blik', 'man':'gorio', 'girl':'morin', 'phone':'cammil', 'pig':'binnyma', 'goat':'ion', 'water':'mio', 'sand':'viv', 'shoe':'qilly', 'bag':'denn', 'fan':'likj', 'watch':'effi', 'basket':'selli', 'bottle':'crin', 'board':'csisi', 'mat':'billu', 'tiger':'gondy'}
jenjo_words = 'tree\nchair\ncat\ndog\nair\nman\ngirl\nphone\npig\ngoat\nwater\nsand\nshoe\nbag\nfan\nwatch\nbasket\nbottle\nboard\nmat\ntiger'

print('you have chosen jenjo dictionary, please choose from the list of available words')
print(jenjo_words)

word = input("what word would you like to interpret?")
if word in jenjo_dict:
   print(word, 'is', jenjo_dict[word], 'in Jenjo')
else:
   print("please choose from the list of available words")