import re
import os
import sys

import units as u
from constants import *
from functions import *

#has assigment
re_assigment = re.compile('(\S+) *:=([^=;]+)')

#has equation
re_equation = re.compile('([^:=]+)=([^;=:]*)')

#has units [unit]
re_units = re.compile('\[(\w+)\]')

#has units [unit]
re_units_udot = re.compile('u\.(\w+)')

ok_sign = ' ✓'
fail_sign = ' ✗(!!!!!!)'
float_precision = 3

def set_float_precision(precission=3):
    global float_precision
    float_precision = precission
    u.__Unum.VALUE_FORMAT =  f'%5.{precission}f'

def format_form_to_python(form):
    form = form.replace('^','**')
    form = re_units.sub(r'u.\1', form)
    return form

def format_udot(form):
    form = re_units_udot.sub(r'[\1]', form)
    return form

def remove_debug_notyfications(ctext):
    ctext = ctext.replace(ok_sign,'')
    ctext = ctext.replace(fail_sign,'')
    return ctext

def get_unum_unit(umum_value=5*u.m):
    unit = umum_value.strUnit()
    unit = unit.replace('*','')
    unit = format_form_to_python(unit)
    unit = eval(unit)
    return unit

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
            line = remove_debug_notyfications(line) #if added above
            data = re_equation.findall(line)[0]
            FORM = data[0]
            FORM = format_form_to_python(FORM)
            RES = data[1]
            RES = str(RES).replace(' ', '')
            try:
                new_RES = eval(FORM)
                ans = new_RES
                #--------------------------
                if type(new_RES) is float:
                    new_RES = round(new_RES, float_precision)
                #---------------------------
                if type(new_RES) is type(u.m) and re_units.search(RES):
                    try:
                        RES = format_form_to_python(RES)
                        RES = eval(RES)
                        RES_unit = get_unum_unit(RES)
                        new_RES = new_RES.asUnit(RES_unit)
                    except Exception as e:
                        line = line + fail_sign
                        has_no_bugs = False
                        out_script += line + '\n'
                        continue
                #----------------------------
                new_RES = str(new_RES).replace(' ', '')
                line = re_equation.sub(r'\1= %s '%(new_RES), line)
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
a := u.m / 2 = 0.33*[m]

'''
    print(process(test_text)[0])