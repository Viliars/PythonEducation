# -*- coding: utf-8 -*-
import io



s=''
i=0
keys=[u"Канал",u"канал",u"Сериал",u"сериал",u"Новости",u"новости",u"Телепередача",u"телепередача",
u"Шоу",u"шоу",u"кино ",u"Кино ",u"Эфир",u"эфир",u"программа на сегодня",u"Телепрограмма",u"телепрограмма",
u"Передача",u"передача",u"ТНТ",u"СТС",u"тнт",u"стс",u"дом два",u"дом",u"мультики",u"Мультики",
u"Мульфильм",u"мульфильм",u"Репортаж",u"репортаж",u"НТВ",u"нтв",u"Карусель",u"карусель",u"культура",u"Культура"]
request_number=[0 for i in range(len(keys))]
name_file = "Log"
res=0
all=0
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
                    res+=1
                i+=1
            all+=i
        except:
            pass
print("Всего запросов = %d" % all)
print("Запросы по нужной тематике = %0.7f" % (100*res/all))
print("Ключевые слова:")
for i in range(len(keys)):
    print(keys[i])
    print("%0.3f" % (100*request_number[i]/res))
    print("---------------------")





 
