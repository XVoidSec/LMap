from geoip import geolite2  
import webbrowser
import socket
import time


print ('''\033[94m
        _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
        |/               `^ .\033[0m''')


print ('[!] [LMap Built By Lord0x]')    


target = input ('\033[92mEnter The Target\033[0m: ')
print ('')
ip = socket.gethostbyname(target)

print ('[!] Searching...')

time.sleep(3.5)
print ('')
location = geolite2.lookup(target)
#map = f'https://www.google.com/search?q={location.location}'
print (f"[+] Was Found {target} in > {location.location}")
#webbrowser.open (map)
