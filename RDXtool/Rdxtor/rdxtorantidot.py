import pyfiglet
import subprocess

text = pyfiglet.figlet_format('RDx-Tor-antidot')
print(text)

print('---------------------')
print('do this process inverse and save it')

i = input('want to re-enable your network from tor {y o Y}-no option:')

if i == 'y' or 'Y':
	
	subprocess.call('sudo nano /etc/proxychains4.conf',shell=True)
	subprocess.call('sudo service tor stop',shell=True)



