from fileinput import filename

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

file_path=r'C:\Users\Administrator\Desktop\大二\python学习\text1\hello.txt'
with open(file_path) as file_object_1:
    print(file_object_1.read())

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

filename1 = 'pi_digits.txt'
with open(filename1) as file_object3:
    lines = file_object3.readlines()

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

pi_string = ''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))

pi_string = ''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))

print(pi_string[:10])

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

file_path_1=r'C:\Users\Administrator\Desktop\大二\python学习\text1\love.txt'
with open(file_path_1,'w') as file_object_3:
    file_object_3.write('I love python!')