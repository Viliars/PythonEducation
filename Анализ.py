# -*- coding: utf-8 -*-
import io



s=''
i=0
keys=[u"Канал",u"канал",u"Сериал",u"сериал",u"Новости",u"новости",u"Телепередача",u"телепередача",
u"Шоу",u"шоу",u"кино ",u"Кино ",u"Эфир",u"эфир",u"программа на сегодня",u"Телепрограмма",u"телепрограмма",
u"Передача",u"передача",u"ТНТ",u"СТС",u"тнт",u"стс",u"дом два",u"дом 2",u"мультики",u"Мультики",
u"Мульфильм",u"мульфильм",u"Репортаж",u"репортаж"]
request = [[]*len(keys)]
request_number=[]
for i in range(len(keys)):
    request_number.append(0)
name_file = "Log"
res=0
with io.open(name_file,encoding='utf-8') as f:
    while(True):
        try:
            s = f.readline()
            if s=='':
                f.close()
                break
            i=0
            for key in keys:
                if s.find(key)!=-1:
                    request_number[i]+=1
                    request[i].append(s)
                    res+=1
                i+=1
        except:
            pass
print("YEEEES "+str(res))
with io.open('output.txt','w') as f:
    for i in range(len(keys)):
        f.write(keys[i])
        f.write(request_number[i]/res)
        for a in request[i]:
            f.write(a)
        f.close()





 
