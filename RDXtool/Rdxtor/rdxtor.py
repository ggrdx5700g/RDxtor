import pyfiglet
import subprocess

text = pyfiglet.figlet_format('RDx-Tor')
print(text)

print('---------------------')

options = [
    'Entering to tor browser...'
]
print(options)
print('- - - - - -  - - - - - - -- - - -- --')

o = input('continue [Y/y]: ')
if o.lower() == 'y':
    subprocess.call('sudo nano /etc/proxychains4.conf', shell=True)
    subprocess.call('sudo service tor start', shell=True)
    subprocess.call('proxychains firefox', shell=True)

        
    
        
