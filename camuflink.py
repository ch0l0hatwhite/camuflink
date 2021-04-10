import time
from requests import get
import webbrowser
import requests as zy
print("""
                                ___  __  __         __    
.----..---.-..--------..--.--..'  _||  ||__|.-----.|  |--.
|  __||  _  ||        ||  |  ||   _||  ||  ||     ||    < 
|____||___._||__|__|__||_____||__|  |__||__||__|__||__|__|
        
 [0] enlace acortado en TinYurl

autor: https://github.com/ch0l0hatwhite

 """)

s=input('enlace a acortar > \n\n')

a='http://tinyurl.com/api-create.php?url='+s


x=zy.get(a)
if x.status_code==200:
    print('sitio disponible para acortamiento\n\n')
    x=get(a).text
    print("\033[31msu enlace es :\t"+x)
    time.sleep(8)
else:
    print("a ocurrido un problema reinicie el script")
    exit()







