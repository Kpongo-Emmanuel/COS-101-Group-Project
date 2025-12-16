while True:
    print('Welcome to the Band Name Generator.')
    city_name = input(str('What is the name of the city you grew up in? '))
    pet_name = input(str("What is your pet's name "))
    if type(city_name) and type(pet_name) == str:
       print('Do you like the name', city_name, pet_name, '?')
    elif type(city_name) or type(pet_name) != str :
        print('Hm weird but alright, do you like the name', city_name, pet_name, '?')
    else:
        print('Hm, weird but alright, do you like the name', city_name, pet_name, '?')
    print('you dont actually get to answer')
#calmm down, this is the feedback section 👇
    feedback = input('Alright fine, do you like it though?| input 1- for "yes", and 2- for "No" ')
    if feedback == '1':
      print('Alright, Thank you so much for your time, GOD BLESS YOU AND YOUR FAMILY RICHLY IN THE MIGHTY WONDERFUL, BLESSED NAME OF JESUS CHRIST OUR LORD AND SAVIOUR AMENNNNNN!!!!')
    elif feedback == '2':
      Honest_review = input('Sorry for the inconveniences, please may we get your Honest review of why you did not like it?')
      print('your review has been recorded successfully, Thank You so much for your time, and GOD BLESS YOU IN JESUS MIGHTY, HOLY, WONDERFUL, MARVELOUS NAME AMENNNNN!!!!')
    else:
        print("sorry, please choose from the options '1' or '2'")