# cyclone shtuff

#asks user their heigh and how many credits they have
height = int(input('What is your height(cm)? '))
credits = int(input('How many credits do you have? '))

#rules...
if height >= 137 and credits >= 10:
  print('Enjoy the ride :3!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride D: ')
elif height >= 137 and credits < 10:
  print("You don't have enough credits /: ")
else:
  print("You don't meet any requirement :< ")
