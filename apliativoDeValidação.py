#-----------------------------------------------------------------------------------------------------
# LOGICA E PROGRAMACAO DE COMPUTADORES
# ATIVIDADE AVALIATIVA
# Aluno: Cristiano César Conceição Barbosa
# ----------------------------------------------------------------------------------------------------
m1 = int(input("Insira numero do mês "))
while (m1>12):
   m1 = int(input("Mês errado, Tente novamente "))

t1 = float(input("Insira a temperatura "))
while (t1>60) or (t1<-90):
   t1 = float(input("Não exite essa temperatura, tente novamente "))

m2 = int(input("Insira numero do mês "))
while (m2>12):
   m2 = int(input("Mês errado, Tente novamente "))

t2 = float(input("Insira a temperatura "))
while (t2>60) or (t2<-90):
   t2 = float(input("Não exite essa temperatura, tente novamente "))

m3 = int(input("Insira numero do mês "))
while (m3>12):
   m3 = int(input("Mês errado, Tente novamente "))

t3 = float(input("Insira a temperatura "))
while (t3>60) or (t3<-90):
   t3 = float(input("Não exite essa temperatura, tente novamente "))

m4 = int(input("Insira numero do mês "))
while (m4>12):
   m4 = int(input("Mês errado, Tente novamente "))

t4 = float(input("Insira a temperatura "))
while (t4>60) or (t4<-90):
   t4 = float(input("Não exite essa temperatura, tente novamente "))

m5 = int(input("Insira numero do mês "))
while (m5>12):
   m5 = int(input("Mês errado, Tente novamente "))

t5 = float(input("Insira a temperatura "))
while (t5>60) or (t5<-90):
   t5 = float(input("Não exite essa temperatura, tente novamente "))

m6 = int(input("Insira numero do mês "))
while (m6>12):
   m6 = int(input("Mês errado, Tente novamente "))

t6 = float(input("Insira a temperatura "))
while (t6>60) or (t6<-90):
   t6 = float(input("Não exite essa temperatura, tente novamente "))

m7 = int(input("Insira numero do mês "))
while (m7>12):
   m7 = int(input("Mês errado, Tente novamente "))

t7 = float(input("Insira a temperatura "))
while (t7>60) or (t7<-90):
   t7 = float(input("Não exite essa temperatura, tente novamente "))

m8 = int(input("Insira numero do mês "))
while (m8>12):
   m8 = int(input("Mês errado, Tente novamente "))

t8 = float(input("Insira a temperatura "))
while (t8>60) or (t8<-90):
   t8 = float(input("Não exite essa temperatura, tente novamente "))

m9 = int(input("Insira numero do mês "))
while (m9>12):
   m9 = int(input("Mês errado, Tente novamente "))

t9 = float(input("Insira a temperatura "))
while (t9>60) or (t9<-90):
   t9 = float(input("Não exite essa temperatura, tente novamente "))

m10 = int(input("Insira numero do mês "))
while (m10>12):
   m10 = int(input("Mês errado, Tente novamente "))

t10 = float(input("Insira a temperatura "))
while (t10>60) or (t10<-90):
   t10 = float(input("Não exite essa temperatura, tente novamente "))

m11 = int(input("Insira numero do mês "))
while (m11>12):
   m11 = int(input("Mês errado, Tente novamente "))

t11 = float(input("Insira a temperatura "))
while (t11>60) or (t11<-90):
   t11 = float(input("Não exite essa temperatura, tente novamente "))

m12 = int(input("Insira numero do mês "))
while (m12>12):
   m12 = int(input("Mês errado, Tente novamente "))

t12 = float(input("Insira a temperatura "))
while (t12>60) or (t12<-90):
   t12 = float(input("Não exite essa temperatura, tente novamente "))


if t1 > t2 and t1 > t3 and t1 > t4 and t1 >t5 and t1 > t6 and t1 > t7 and t1 > t8 and t1 > t9 and t1 >t10 and t1 > t11 and t1 > t12:
  print(f"O Mês mais escaltante é {m1}")
elif t2 > t3 and t2 > t4 and t2 >t5 and t2 > t6 and t2 > t7 and t2 > t8 and t2 > t9 and t2 >t10 and t2 > t11 and t2 > t12:
  print(f"O Mês mais escaldante é {m2}")
elif t3 > t4 and t3 > t5 and t3 > t6 and t3 > t7 and t3 > t8 and t3 > t9 and t3 >t10 and t3 > t11 and t3 > t12:
  print(f"O Mês mais escaldante é {m3}")
elif t4 >t5 and t4 > t6 and t4 > t7 and t4 > t8 and t4 > t9 and t4 >t10 and t4 > t11 and t4 > t12:
  print(f"O Mês mais escaldante é {m4}")
elif t5 > t6 and t5 > t7 and t5 > t8 and t5 > t9 and t5 >t10 and t5 > t11 and t5 > t12:
  print(f"O Mês mais escaldante é {m5}")
elif t6 > t7 and t6 > t8 and t6 > t9 and t6 >t10 and t6 > t11 and t6 > t12:
  print(f"O Mês mais escaldante é {m6}")
elif t7 > t8 and t7 > t9 and t7 >t10 and t7 > t11 and t7 > t12:
  print(f"O Mês mais escaldante é {m7}")
elif t8 > t9 and t8 >t10 and t8 > t11 and t8 > t12:
  print(f"O Mês mais escaldante é {m8}")
elif t9 >t10 and t9 > t11 and t9 > t12:
  print(f"O Mês mais escaldante é {m9}")
elif t10 > t11 and t10 > t12:
  print(f"O Mês mais escaldante é {m10}")
elif  t11 > t12:
  print(f"O Mês mais escaldante é {m11}")
elif  t11 < t12:
  print(f"O Mês mais escaldante é {m12}")

mFrio = ()

if t1 < t2 and t1 < t3 and t1 < t4 and t1 < t5 and t1 < t6 and t1 < t7 and t1 < t8 and t1 < t9 and t1 < t10 and t1 < t11 and t1 < t12:
  mFrio = 1
elif t2 < t3 and t2 < t4 and t2 < t5 and t2 < t6 and t2 < t7 and t2 < t8 and t2 < t9 and t2 < t10 and t2 < t11 and t2 < t12:
  mFrio = 2
elif t3 < t4 and t3 < t5 and t3 < t6 and t3 < t7 and t3 < t8 and t3 < t9 and t3 < t10 and t3 < t11 and t3 < t12:
  mFrio = 3
elif t4 < t5 and t4 < t6 and t4 < t7 and t4 < t8 and t4 < t9 and t4 < t10 and t4 < t11 and t4 < t12:
  mFrio = 4
elif t5 < t6 and t5 < t7 and t5 < t8 and t5 < t9 and t5 < t10 and t5 < t11 and t5 < t12:
  mFrio = 5
elif t6 < t7 and t6 < t8 and t6 < t9 and t6 < t10 and t6 < t11 and t6 < t12:
  mFrio = 6
elif t7 < t8 and t7 < t9 and t7 < t10 and t7 < t11 and t7 < t12:
  mFrio = 7
elif t8 < t9 and t8 < t10 and t8 < t11 and t8 < t12:
  mFrio = 8
elif t9 < t10 and t9 < t11 and t9 < t12:
  mFrio = 9
elif t10 < t11 and t10 < t12:
  mFrio = 10
elif  t11 < t12:
  mFrio = 11
elif  t11 > t12:
  mFrio = 12

if mFrio == 1:
 print("O mês mais frio é Janeiro")
if mFrio == 2:
 print("O mês mais frio é Fevereiro")
elif mFrio == 3:
 print("O mês mais frio é Março")
if mFrio == 4:
 print("O mês mais frio é Abril")
if mFrio == 5:
 print("O mês mais frio é Maio")
if mFrio == 6:
 print("O mês mais frio é Junho")
if mFrio == 7:
 print("O mês mais frio é Julho")
if mFrio == 8:
 print("O mês mais frio é Agosto")
if mFrio == 9:
 print("O mês mais frio é Setembro")
if mFrio == 10:
 print("O mês mais frio é Outubro")
if mFrio == 11:
 print("O mês mais frio é Novembro")
if mFrio == 12:
 print("O mês mais frio é Dezembro")

media = (t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12)/12

print(f"A Temperatura média máxima anual é {media}ºC")