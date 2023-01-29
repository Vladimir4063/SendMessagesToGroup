import pywhatkit
import time


id_group = "D9EczidydUn2REEi7wLiOx"

#pywhatkit.sendwhatmsg_to_group(id_group,"Hola grupo",11,59)

lectura = "Hola Andresito!!"
print(type(lectura))

lecturaTxt = open("bereshit.txt")
lecturaConvert=str(lecturaTxt)

print(lecturaConvert)
print("Espero 15s")


time.sleep(10)

pywhatkit.sendwhatmsg_to_group_instantly(id_group,lectura)
