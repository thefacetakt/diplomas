#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import hashlib
import time
from subprocess import call
import csv
import sys
import re

def process_school_name(school):
  if school[0:6] == 'школа ':
    school = 'школы ' + school[6:]
  elif school[0:6] == 'Школа ':
    school = 'Школы ' + school[6:]
  elif school[0:6] == 'школа,':
    school = 'школы,' + school[6:]
  elif school[0:14] == 'частная школа ':
    school = 'частной школы ' + school[14:]
  elif school[0:6] == 'лицей ':
    school = 'лицея ' + school[6:]
  elif school[0:6] == 'Лицей ':
    school = 'Лицея ' + school[6:]
  elif school[0:9] == 'гимназия ':
    school = 'гимназии ' + school[9:]
  elif school[0:12] == 'прогимназия ':
    school = 'прогимназии ' + school[12:]
  elif school[0:22] == 'классическая гимназия ':
    school = 'классической гимназии ' + school[22:]
  elif school[0:9] == 'Гимназия ':
    school = 'Гимназии ' + school[9:]
  elif school[0:6] == 'центр ':
    school = 'центра ' + school[6:]
  elif school[0:14] == 'учебный центр ':
    school = 'учебного центра ' + school[14:]
  elif school == 'Пятьдесят седьмая школа':
    school = 'Пятьдесят седьмой школы'
  elif school[0:15] == 'школа-интернат ':
    school = 'школы-интерната ' + school[15:]
  elif school == 'sch500469':
    school = 'гимназии г. Видное'
  elif school == 'sch503445':
    school = 'школы № 6 г. Мытищи'
  elif school == 'sch121200':
    school = 'школы № 108'
  elif school == 'Государственная cтоличная гимназия':
    school = 'Государственной cтоличной гимназии'
  elif school == 'Свято-Петровская Школа':
    school = 'Свято-Петровской Школы'
  elif school == 'МЦНМО г. ХЗ':
    school = 'МЦНМО г. ХЗ'
  elif school == 'Филипповская школа':
    school = 'Филипповской школы'
  elif school == 'Захаровская школа пос. Летний отдых':
    school = 'Захаровской школы пос. Летний отдых'
  elif school == 'Елизаветинская гимназия':
    school = 'Елизаветинской гимназии'
  elif school == 'Британская международная школа':
    school = 'Британской международной школы'
  elif school == 'Троицкая Православная школа':
    school = 'Троицкой Православной школы'
  elif school == 'Кадетская школа-интернат № 11':
    school = 'Кадетской школы-интерната № 11'
  elif school == 'Московская международная гимназия':
    school = 'Московской международной гимназии'
  elif school == 'православная школа-пансион <<Плесково>>':
    school = 'православной школы-пансиона <<Плесково>>'
  elif school == 'образовательный центр <<Солнечный ветер>>':
    school = 'образовательного центра <<Солнечный ветер>>'
  #elif school == 'лицей №2 им. М.В. Ломоносова г. Брянск':
  #  school = 'лицея №2 им. М.В. Ломоносова г. Брянск'
  elif school == 'Ломоносовская школа':
    school = 'Ломоносовской школы'
  elif school == 'Физтех-лицей имени П.Л. Капицы г. Долгопрудный':
    school = 'Физтех-лицея имени П.Л. Капицы г. Долгопрудный'
  elif school == 'Хибинская гимназия г. Кировск':
    school = 'Хибинской гимназии г. Кировск'
  elif school == 'еврейская школа <<Мир интеллекта>>':
    school = 'еврейской школы <<Мир интеллекта>>'
  elif school == 'Московский государственный техникум технологий и права':
    school = 'Московского государственного техникума технологий и права'
  elif school == 'Пироговская школа':
    school = 'Пироговской школы'
  elif school == 'Костромской кадетский корпус':
    school = 'Костромского кадетского корпуса'
  elif school == 'семейное образование':
    school = 'семейное образование'
  elif school == 'Раменская № 2 г. Раменское':
    school = 'Раменской № 2 г. Раменское'
  elif school == 'Славяно-англо-американская <<Марина>> школа':
    school = 'Славяно-англо-американской школы <<Марина>>'
  elif school == 'Многопрофильный № 1799':
    school = 'многопрофильного лицея № 1799'
  elif school == 'средняя общеобразовательная школа, д. Кузмищи, Костромская обл.':
    school = 'СОШ, д. Кузмищи, Костромская обл.'
  elif school == 'Университетская школа МГПУ':
    school = 'Университетской школы МГПУ'
  elif school == 'лесная школа, г. Лесная Чаща':
    school = 'лесной школы, г. Лесная Чаща'
  elif school == 'sch333333':
    school = 'школы Юного Песца'
  else:
    print (str (i) + ' school: ' + school)
  return school
  
file_name = sys.argv[2]
tex1 = open (file_name + '-d1.tex', mode = 'w', encoding = 'utf-8')
tex1.write ('\\documentclass[a4paper,landscape]{article}\n\n')
tex1.write ('\\usepackage[utf8]{inputenc}\n')
tex1.write ('\\usepackage[T2A]{fontenc}\n')
tex1.write ('\\usepackage[top=0.69in,bottom=0.69in,left=1in,right=1in]{geometry}\n')
tex1.write ('\\usepackage{graphicx}\n\n')
tex1.write ('\\pagestyle{empty}\n\n')
tex1.write ('\\begin{document}\n')
tex2 = open (file_name + '-d2.tex', mode = 'w', encoding = 'utf-8')
tex2.write ('\\documentclass[a4paper,landscape]{article}\n\n')
tex2.write ('\\usepackage[utf8]{inputenc}\n')
tex2.write ('\\usepackage[T2A]{fontenc}\n')
tex2.write ('\\usepackage[top=0.69in,bottom=0.69in,left=1in,right=1in]{geometry}\n')
tex2.write ('\\usepackage{graphicx}\n\n')
tex2.write ('\\pagestyle{empty}\n\n')
tex2.write ('\\begin{document}\n')
tex3 = open (file_name + '-d3.tex', mode = 'w', encoding = 'utf-8')
tex3.write ('\\documentclass[a4paper,landscape]{article}\n\n')
tex3.write ('\\usepackage[utf8]{inputenc}\n')
tex3.write ('\\usepackage[T2A]{fontenc}\n')
tex3.write ('\\usepackage[top=0.69in,bottom=0.69in,left=1in,right=1in]{geometry}\n')
tex3.write ('\\usepackage{graphicx}\n\n')
tex3.write ('\\pagestyle{empty}\n\n')
tex3.write ('\\begin{document}\n')
tex4 = open (file_name + '-pg.tex', mode = 'w', encoding = 'utf-8')
tex4.write ('\\documentclass[a4paper,landscape]{article}\n\n')
tex4.write ('\\usepackage[utf8]{inputenc}\n')
tex4.write ('\\usepackage[T2A]{fontenc}\n')
tex4.write ('\\usepackage[top=0.69in,bottom=0.69in,left=1in,right=1in]{geometry}\n')
tex4.write ('\\usepackage{graphicx}\n\n')
tex4.write ('\\pagestyle{empty}\n\n')
tex4.write ('\\begin{document}\n')
users = csv.reader (open (sys.argv[1]))
i = 0
for row in users:
  first_name, last_name, school, grade, gender, degree = row[3], row[4], row[7], row[6], row[5], row[8]
  i += 1
  if i == 1:
    continue
  
  if gender == 'м' or gender == 'М':
    gender = 'ученик'
  elif gender == 'ж' or gender == 'Ж':
    gender = 'ученица'

  if degree == 'None':
    tex = tex4
    degree = 'НЕТ'
    continue
  elif int (degree) >= 30:
    degree = 'первой степени'
    tex = tex1
  elif int (degree) >= 24:
    degree = 'второй степени'
    tex = tex2
  elif int (degree) >= 19:
    degree = 'третьей степени'
    tex = tex3
  elif int (degree) >= 14:
    degree = ''
    tex = tex4
  else:
    continue

  school = re.sub ('"(.*)"', '<<\\1>>', school)
  school = re.sub ('«', '<<', school)
  school = re.sub ('“', '<<', school)
  school = re.sub ('»', '>>', school)
  school = re.sub ('”', '>>', school)
  school = re.sub (' ', ' ', school)
  school = re.sub (' ', ' ', school)
  print (school)
  tex.write ('\\flushleft{\n')
  tex.write ('\\noindent\n')
  tex.write ('Московское математическое общество\\\\\n')
  tex.write ('Департамент образования города Москвы\\\\\n')
  tex.write ('Московский государственный университет им.~М.~В.~Ломоносова\\\\\n')
  tex.write ('\\hskip 2cm Механико-математический факультет\\\\\n')
  tex.write ('Центр педагогического мастерства\\\\\n')
  tex.write ('Московский центр непрерывного математического образования\\\\\n')
  tex.write ('}\n\n')
  tex.write ('\\vskip 2.5cm\n\n')
  if degree == '':
    tex.write ('\\vskip 0.5cm\n\n')
  else:
    tex.write ('\\hskip 15cm \\resizebox{!}{0.5cm}{\\textit{\\textbf{' + degree +'}}}\n\n')
  tex.write ('\\vskip 1.5cm\n')
  tex.write ('\\center{\\resizebox{!}{1.2cm}{\\textit{' + first_name + ' ' + last_name + '}}}\n')
  tex.write ('\\center{\\huge ' + gender + ' ' + grade + ' класса \\\\\n')
  tex.write ('' + school + ' \\\\\n')
  tex.write ('за успешное выступление \\\\\n')
  tex.write ('на XXVI Математическом празднике \\\\\n')
  tex.write ('15 февраля 2015 года\n\n}\n\n')
  tex.write ('\\vskip 0.2cm\n\n')
  tex.write ('\\begin{tabular}{p{6cm}p{6cm}p{6cm}p{6cm}}\n')
  tex.write ('  \\flushleft{\\large Заместитель председателя оргкомитета Математического~праздника, зам.~директора МЦНМО} & & \\flushleft{\\large Председатель~жюри Математического~праздника, директор МЦНМО и ЦПМ} &  \\\\\n')
  tex.write ('   & \\center{\\large В.~Д.~Арнольд} & & \\center{\\large И.~В.~Ященко} \\\\\n')
  tex.write ('\\end{tabular}\n')
  tex.write ('\\newpage\n')

tex1.write ('\\end{document}\n')
tex1.close ()
tex2.write ('\\end{document}\n')
tex2.close ()
tex3.write ('\\end{document}\n')
tex3.close ()
tex4.write ('\\end{document}\n')
tex4.close ()

call (['pdflatex', file_name + '-d1.tex'])
call (['pdf2ps', file_name + '-d1.pdf'])
call (['pdflatex', file_name + '-d2.tex'])
call (['pdf2ps', file_name + '-d2.pdf'])
call (['pdflatex', file_name + '-d3.tex'])
call (['pdf2ps', file_name + '-d3.pdf'])
call (['pdflatex', file_name + '-pg.tex'])
call (['pdf2ps', file_name + '-pg.pdf'])
