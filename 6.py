word = str(input())
glas = 0
soglas = 0
for i in word:
    letter=i.lower()

    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        glas += 1
    else:
        soglas += 1
s1=word.count('a')
s2=word.count('e')
s3=word.count('y')
s4=word.count('i')
s5=word.count('o')
s6=word.count('u')
if s1==0 or s2==0 or s3==0 \
or s4==0 or s5==0 or s6 ==0:
    print('False')

print('гласных',glas,'согласных',soglas)
