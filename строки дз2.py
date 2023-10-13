str1=input('введите строку:')
while '  ' in str1:
    str1=str1.replace('  ','')
print(str1)
