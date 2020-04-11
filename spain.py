import os
os.system('clear')
print("\x1b[1;31m")
os.system('pkg install bash')
os.system('clear')
os.system('sleep 0.1')
print("\n\n") 
os.system('sleep 0.1')
print("\x1b[1;33m"+"            #########################") 
os.system('sleep 0.1')
print("\x1b[1;33m"+"            #########################")
os.system('sleep 0.1')
print("\x1b[1;31m"+"            #########TERMUX##########")
os.system('sleep 0.1')
print("\x1b[1;31m"+"            #########/SPAIN##########")
os.system('sleep 0.1') 
print("\x1b[1;33m"+"            #########################")
os.system('sleep 0.1')
print("\x1b[1;33m"+"            #########################")
os.system('sleep 0.1')
print("\x1b[1;37m"+"\n\nElige la opción que desea ejecutar ^^")
os.system("sleep 0.1")
print("\x1b[1;31m"+"\n[1] Instalar Comandos")
os.system("sleep 0.1") 
print("\x1b[1;33m"+"[2] Eliminar los comandos")
os.system("sleep 0.1")
print("\x1b[1;32m"+"[3] Que hace? ")
os.system("sleep 0.1")
print("\x1b[1;37m"+"[0] autor")
os.system("sleep 0.1")
vw = input("\x1b[1;31m"+"\nInserte la opción que desea ejecutar:")

for vwroot in vw:

        vwtool = vwroot.upper()

if (vwroot == "1"):
	os.system('unzip vwolfdata.zip') | os.system('cd vwolfdata;mv * /data/data/com.termux/files/usr/bin/') | os.system ('sleep 1') | os.system('chmod 777 /data/data/com.termux/files/usr/bin/*') | os.system('clear;ayuda')
        

if (vwroot == "2"):
        os.system('bash eliminar.sh')

elif (vwroot == "3"):
        print("\nLa función de lang-esp es la posibilidad de utilizar los comandos básicos de termux en español y con mayor facilidad, ej: copiar")

elif (vwroot == "0"):
        print("\n Autor : https://vwolf.site")
