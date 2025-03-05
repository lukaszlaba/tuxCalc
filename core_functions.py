import re

text = '''
1+1=
'''


#------------- regular expresion for '2+2 // Comment'----------
re_text = re.compile('(.*)= *(.*) *')




'''
2+2 = 4 ; comment EQ1

a := 12 ; comment EQ2
a := 12 + 10 ; comment EQ3
a := 12 +10 = 22 ; comment EQ4

'''







def calc(text):
    pass

print(re_text.findall('2+1 = 10 '))



