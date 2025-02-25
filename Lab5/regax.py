import re

with open('row.txt') as file:
    lines=file.readlines()

#ex1
for i in lines:
    if(re.findall("a(b*)",i)):
        print(i)
"""
output:
abbbb

a_b

abb

a

baaaab

asdfasdaf_asdgasdsa

sabbadsfgasdg

sabbbkdjfmgkfgfg

sabbkdsf,mgkdmsabbbbb

natrus

a_z

asfhasd_asdjhmtgk,sd

sdfosjkfmgdf,h_asdfmkg

Система для инфузии Vogt Medical

Naturella прокладки Классик макси №8

Carefree салфетки Алоэвоздухопроницаемые №20

Clear шампунь Актив спорт 2в1мужской  400 мл

WebKassa.Kz

AdasfvgAsdfgfSdasfsasfasdWasdasf
"""
print("Ex2")
#ex2
for i in lines:
    if re.findall("ab{2,3}[^b].*", i):
        print(i)
"""
output:
abb

sabbadsfgasdg

sabbbkdjfmgkfgfg

sabbkdsf,mgkdmsabbbbb
"""

print("Ex3")
#ex3
for i in lines:
    if (re.findall("[a-z]_[a-z]", i)):
        print(i)
"""
output:
a_b

asdfasdaf_asdgasdsa

a_z

asfhasd_asdjhmtgk,sd

sdfosjkfmgdf,h_asdfmkg
"""

print("Ex4")
#ex4
for i in lines:
    if(re.findall("[A-Z][a-z]", i)):
        print(i)
"""
output:
Шприц 2 мл, 3-х комп. (Bioject)

Система для инфузии Vogt Medical

Naturella прокладки Классик макси №8

Carefree салфетки Алоэвоздухопроницаемые №20

Pro Series Шампунь яркий цвет 500мл

Pro Series бальзам-ополаскивательдля длител ухода за окрашеннымиволосами Яркий цвет 500мл

Clear шампунь Актив спорт 2в1мужской  400 мл

Bio World (HYDRO THERAPY)Мицеллярная вода 5в1, 445мл

Bio World (HYDRO THERAPY) Гель-муссдля умывания с гиалуроновойкислотой, 250мл

WebKassa.Kz

AdasfvgAsdfgfSdasfsasfasdWasdasf
"""

print("Ex5")
#ex5
for i in lines:
    if(re.findall("^a.*b$",i)):
        print(i)
"""
output:
abbbb

a_b

abb

"""

print("Ex6")
#ex6
for i in lines:
    print(re.sub(r"[ .,]",":",i))

print("Ex7")
#ex7
for i in lines:
    print(re.sub("_[a-z]",lambda a:a.group(0).upper()[1::],i))


print("Ex8")
#ex8
for i in lines:
    print(re.split("[A-Z]",i))


print("Ex9")
#ex9
for i in lines:
    print(re.sub(r"(\w)([A-Z])",r"\1 \2",i))


print("Ex10")
#ex10
i="AbcAbcsdAbcsdf"
print(re.sub(".[A-Z]",lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}',i))