#First task
windows_serial_number = "abc-def-ghi-jkl"

#Second task
one = windows_serial_number[0:3]
two = windows_serial_number[4:7]
three = windows_serial_number[8:11]
four = windows_serial_number[12:15]
#print(one + two + three + four)

#Third task
one = one.replace('bc', 'aa')
two = two.replace('def', 'bbb')
three = three.replace('ghi', 'ccc')
four = four.replace('jkl', 'ddd')
#print(one + two + three + four)

#Fourth task
encoded_windows_serial_number = one + '-' + two + '-' + three + '-' + four

#Fifth task
print("Serial number: " + windows_serial_number)
print("New serial number: " + encoded_windows_serial_number)