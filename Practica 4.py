import datetime
import ntplib
import os
from time import ctime

t1 = datetime.datetime.now()
print ("Tiempo 1 :  = %s" % t1)
servidor= "time-e-g.nist.gov"
cliente_ntp = ntplib.NTPClient()
resp = cliente_ntp.request(servidor)
hora_act= datetime.datetime.strptime(ctime(resp.tx_time), "%a %b %d %H:%M:%S %Y")
t2 = datetime.datetime.now()
print ("Tiempo 1 :  = %s" % t2)
print("Respuesta de " + servidor +  ": " + str(hora_act) + "\n")
print("Ajuste: "+str(((t2-t1)/2)))
newtime = hora_act + (t2-t1)/2
print("Nueva Hora = %s" % hora_act)
os.system('date --set "%s"' %newtime)