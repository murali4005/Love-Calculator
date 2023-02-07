print('Welcome to the Love Calculator!')
# Take the inputs from the users about the names
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

# combine those two names and make it one
combined_string = name1 + name2

# make everything lower so that we don't miss out on few
combined_string_lower = combined_string.lower()

t = combined_string_lower.count('t')
r = combined_string_lower.count('r')
u = combined_string_lower.count('u')
e = combined_string_lower.count('e')

true_value = t + r + u + e

l = combined_string_lower.count('l')
o = combined_string_lower.count('o')
v = combined_string_lower.count('v')
e = combined_string_lower.count('e')

love_value = l + o + v + e

love_score = int(str(true_value) + str(love_value))

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50 :
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}.')