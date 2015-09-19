#simple noip HTTPS updater by lucaszanella.com

import time
from http.client import HTTPSConnection
from base64 import b64encode

#User customizable part *********
interval = 15 #in seconds
noIpDomain = 'something.no-ip.org'
user = 'username'
password = 'password'
#end ****************************


UserAndPasswordInBytes = (user+":"+password).encode("ascii")#convert to bytes

userAndPassEncoded = b64encode(UserAndPasswordInBytes).decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPassEncoded }

while True:
    try:
        c = HTTPSConnection("dynupdate.no-ip.com")
        c.request('GET', '/nic/update?hostname='+noIpDomain, headers=headers)
        res = c.getresponse()
        data = res.read()  
        print(data)
    except:
        print('error')
    time.sleep(interval)
