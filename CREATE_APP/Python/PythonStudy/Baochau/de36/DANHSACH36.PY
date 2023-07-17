lines = input('nhập vào dãy kí tự: ')

number = []
chu = []
for line in lines:
    if line.isdigit():
        number.append(line)
    else:
        chu.append(line)
        
number.sort(reverse = True)
chu.sort()
print('nữa đầu giảm dần: ',number)
print('nữa đầu tăng dần: ',chu)
