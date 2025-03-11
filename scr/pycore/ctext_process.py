import re
import os
import sys

import units as u

#has assigment
re_assigment = re.compile('(\S+) *:=([^=;]+)')
#has equation
re_equation = re.compile('([^:=]+)=([^;=:]*)')
#has units [unit]
re_units = re.compile('\[(\w+)\]')



print(re_units.sub(r'u.\1', '2*[m] - 10*[cm]'), '<<<<')

ok_sign = ' ✓'
fail_sign = ' ✗ (!!!!!!)'
float_precision = 3

def set_float_precision(precission=3):
    global float_precision
    float_precision = precission
    u.__Unum.VALUE_FORMAT =  f'%5.{precission}f'

def format_form_to_python(form):
    form = form.replace('^','**')
    form = re_units.sub(r'u.\1', form)
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
                if type(RES) is float:
                    RES = round(RES, float_precision)
                RES = str(RES).replace(' ', '') #!!!!!!!!!!!!
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
a := 1*[m] = ;asdsds
b := 1
a + 1*u.m = ;sadsad
a/3 = 0.4
ans =
'''
    print(process(test_text)[0])