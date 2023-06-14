import subprocess
import time


serialNumber = 'RX8NA033W1A' #Utilizado Celular pessoal, com as coordenadas utilizadas do celular.
email = 'email_teste@gmail.com'
senha = 'testeteste'
senha1 = 'testeteste'

#Abrindo app
subprocess.check_output(['adb', 'shell', 'am start -n io.ionic.starter/io.ionic.starter.MainActivity'])
time.sleep(5)

#Crie uma conta
adb_command = f'adb shell input tap 700 2270'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Clica no campo email
adb_command = f'adb shell input tap 150 1100'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Insere o E-mail
adb_command = f'adb shell input text "{email}"'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Clica Fora
adb_command = f'adb shell input tap 200 800'
subprocess.run(adb_command, shell=True)



#Clica no campo de Senha
adb_command = f'adb shell input tap 130 1260'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Insere a senha
adb_command = f'adb shell input text "{senha}"'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Clica Fora
adb_command = f'adb shell input tap 200 800'
subprocess.run(adb_command, shell=True)
time.sleep(3)


#Clica no campo de repetir Senha
adb_command = f'adb shell input tap 160 1400'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Insere a senha novamente
adb_command = f'adb shell input text "{senha1}"'
subprocess.run(adb_command, shell=True)
time.sleep(3)

#Clica Fora
adb_command = f'adb shell input tap 200 800'
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input tap 500 1600' # Clica no Botão login
subprocess.run(adb_command, shell=True)