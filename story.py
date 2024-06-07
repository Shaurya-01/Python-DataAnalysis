kahani = ''
while True:
    line = input('>>>')  #to take the input for multiple lines
    if not line:
        break
    kahani += line + '\n'

print('The kahani is: ')
print(kahani)