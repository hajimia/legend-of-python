# fizz buzz thingy

# my first rendition vvvvv
#for multiples of 3 -> print fizz
for number in range(1, 100):
  if number % 3 == 0:
    print(f'Fizz')
#for multiples of 5 -> print buzz
for number in range(1, 100):
  if number % 5 == 0:
    print(f'Buzz')
#for multiples of 3 AND 5 -> print fizzbuzz
for number in range(1, 100):
  if number % 3 == 0 and number % 5 == 0:
    print(f'FizzBuzz')

# 2nd rendition vvvvv
#ok after making the above im realizing i could make it under the same loop
for number in range(1, 100):
  if number % 3 == 0 and number % 5 == 0:
     print(f'FizzBuzz')
  elif number % 3 == 0:
    print(f'Fizz')
  elif number % 5 == 0:
     print(f'Buzz')
else:
  print(number)
