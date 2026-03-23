import pyfiglet
import subprocess

text = pyfiglet.figlet_format('RDx-Tor')
print(text)

print('---------------------')

options = [
    '1. enter to tor browser'
]
print(options)

print('comment beside strict_chain and comment out beside dynamic_chain and comment out proxy_dns.. then scroll down and you will find a proxylist and use socks5 under socks4 and everything should similiar , then do ctrl-x , y and enter and If it give error run {sudo apt install tor}')
print('- - - - - -  - - - - - - -- - - -- --')

o = input('continue Y: ')
if o.lower() == 'y':
    subprocess.call('sudo nano /etc/proxychains4.conf', shell=True)
    subprocess.call('sudo service tor start', shell=True)
    subprocess.call('proxychains firefox', shell=True)

        
    
        
