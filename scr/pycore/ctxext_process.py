import re

#has assigment
re_assigment = re.compile('(\S+) *:=([^=;]+)')
#has equation
re_equation = re.compile('([^:=]+)=([^;=:]*)')

ok_sign = ' ✓'
fail_sign = ' ✗ (!!!!!!)'

def format_form_to_python(form):
    form = form.replace('^','**')
    return form

def remove_debug_notyfications(ctext):
    ctext = ctext.replace(ok_sign,'')
    ctext = ctext.replace(fail_sign,'')
    return ctext

def process(ctext):
    ctext = remove_debug_notyfications(ctext)
    lines = ctext.split('\n')
    out_script = ''
    has_no_bugs = True
    for line in lines:
        success = False
        if re_assigment.findall(line):
            data = re_assigment.findall(line)[0]
            VAR = data[0]
            FORM = data[1]
            FORM = format_form_to_python(FORM)
            try:
                exec(f'{VAR}={FORM}')
                ans = eval(FORM)
                line = line + ok_sign
            except:
                line = line + fail_sign
                has_no_bugs = False
        if re_equation.findall(line):
            data = re_equation.findall(line)[0]
            FORM = data[0]
            FORM = format_form_to_python(FORM)
            try:
                RES = eval(FORM)
                line = re_equation.sub(r'\1= %s '%(RES), line)
                ans = RES
                line = line + ok_sign
            except:
                line = line + fail_sign
                has_no_bugs = False
        out_script += line + '\n'
    #there is one \n to much at the end so remove it
    out_script = out_script[:-1]
    return out_script, has_no_bugs

#test if main
if __name__ == '__main__':
    test_text='''
Tests script
Comment
a := 1 ;asdsds
b := 1
a + 1 = ;sadsad
a/5 = 0.4
ans =
'''
    print(process(test_text)[0])