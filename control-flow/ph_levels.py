# ph level thingy

ph = int(input('Enter a pH value (0-14): '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
