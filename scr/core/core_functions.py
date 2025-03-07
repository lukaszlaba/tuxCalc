import re

text = '''
1+1=
'''


#------------- regular expresion for '2+2 // Comment'----------
re_text = re.compile('(.*)= *(\d*) *(;*)(.*)')




'''
2+2 = 4 ; comment EQ1

a := 12 ; comment EQ2
a := 12 + 10 ; comment EQ3
a := 12 +10 = 22 ; comment EQ4

'''


def process(script):
    lines = script.split('\n')
    out_script = ''
    for line in lines:
        #print(line)
        if re_text.findall(line):

            data = re_text.findall(line)[0]
            print(data)
            equ = data[0]
            equ = equ.replace('^', '**')
            comment = data[3]
            comma = data[2]
            if comma: comma = ' ;'
            exec(equ)
            res = eval(equ)
            ans = res
            out_script += equ + '= ' + str(res) + comma + comment + '\n'
        else:
            out_script += line + '\n'
    print(out_script)
    return out_script


#print(re_text.findall('2+1 = 10 '))


#test if main
if __name__ == '__main__':
    script='''
Comment
1+1  =2 ; sadsad
ans - 1 = 12
3 * 6 =
4^0.5 =
ans*5 = ; sdsd
'''
    process(script)










