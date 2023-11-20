letters =['a','b','c','d','e','f']
characters =['@','$','^','&']
numbers= ['1','2','3','4','5','6']
import random
n_letters=int(input("how many letters do you want?"))
n_numbers=int(input("how many numbers do you want?"))
n_characters=int(input("how many characters do you want?"))

# pw=""
# for n in range (1, n_letters+1):
#     random_letters=random.choice(letters)
#     pw+=random_letters
# for n in range (1, n_numbers+1):
#     random_numbers=random.choice(numbers)
#     pw+=random_numbers
# for n in range (1, n_letters+1):
#     random_characters=random.choice(characters)
#     pw+=random_characters
# print(pw)

pw=[]
for n in range (1, n_letters+1):
    random_letters=random.choice(letters)
    pw.append(random_letters)
for n in range (1, n_numbers+1):
    random_numbers=random.choice(numbers)
    pw.append(random_numbers)
for n in range (1, n_characters+1):
    random_characters=random.choice(characters)
    pw.append(random_characters)
    

random.shuffle(pw)


password=""
for char in pw:
    password+=char
print(f"your pw is {password}")
    
    

