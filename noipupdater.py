#simple noip HTTPS updater by lucaszanella.com

import time
from http.client import HTTPSConnection
from base64 import b64encode

#User customizable part *********
interval = 5 #in seconds
noIpDomain = 'mydomain.no-ip.org'
user = 'myusername@email.com'
password = 'myPassword'
n = 3 # number of update tries
printSuccess = False #makes it print the success message in every try
#end ****************************


UserAndPasswordInBytes = (user+":"+password).encode("ascii")#convert to bytes

userAndPassEncoded = b64encode(UserAndPasswordInBytes).decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPassEncoded }

for x in range(0,n):
    try:
        c = HTTPSConnection("dynupdate.no-ip.com")
        c.request('GET', '/nic/update?hostname='+noIpDomain, headers=headers)
        res = c.getresponse()
        data = res.read()
        if "nochg" in data.decode("utf-8"):
            if printSuccess:
                print(data)
            break;
    except:
        print('error')
    time.sleep(interval)

