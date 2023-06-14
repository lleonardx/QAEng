import subprocess

#Usado para tirar o dump da tela
def getXMLdump(device_id, output_file):
    command = f'adb -s {device_id} shell uiautomator dump /sdcard/ui_dump.xml'
    subprocess.run(command, shell=True)

    command = f'adb -s {device_id} pull /sdcard/ui_dump.xml {output_file}'
    subprocess.run(command, shell=True)


device_id = 'RX8NA033W1A'
dump = './/dump.xml'

getXMLdump(device_id, dump)