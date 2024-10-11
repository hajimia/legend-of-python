# let's make a sorting hat!

# starting house points
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# question 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

question_1 = int(input("Enter your answer (1-2): "))
if question_1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question_1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# question 2
print("Q2) When I'm dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

question_2 = int(input("Enter your answer (1-4): "))
if question_2 == 1:
    hufflepuff += 2
elif question_2 == 2:
    slytherin += 2
elif question_2 == 3:
    ravenclaw += 2
elif question_2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# question 3
print("Q3) What kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

question_3 = int(input("Enter your answer (1-4): "))
if question_3 == 1:
    slytherin += 4
elif question_3 == 2:
    hufflepuff += 4
elif question_3 == 3:
    ravenclaw += 4
elif question_3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Print the points for each house
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# Print the house with the most points
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('Ravenclaw!')
elif hufflepuff >= slytherin:
    print('Hufflepuff!')
else:
    print('Slytherin!')
