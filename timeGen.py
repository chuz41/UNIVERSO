#Función que genera número de tiempo. 


import datetime


def timeGen():
    a = str(datetime.date.today())
    a0=int(a[0])
    a1=int(a[1])
    a2=int(a[2])
    a3=int(a[3])
    a4=int(a[5])
    a5=int(a[6])
    a6=int(a[8])
    a7=int(a[9])
    time = a7 + (a6*10) + (a5*100) + (a4*1000) + (a3*10000) + (a2*100000) + (a1*1000000) + (a0*10000000)
    return time


    



    





#
