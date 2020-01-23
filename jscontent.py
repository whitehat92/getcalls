import requests
import sys
from urllib3.exceptions import InsecureRequestWarning
import re

requests.urllib3.disable_warnings()


#regex for javascript files
#<(?:script|SCRIPT).*?(?:src|SRC)=([^\s>]+)

javascriptregex = "<(?:script|SCRIPT).*?(?:src|SRC)=([^\s>]+)"
url = sys.argv[1]
if not "https://" in url:
        url = "https://" + url
headers={'User-agent':'Mozilla//5.0',}
r = requests.get(url=url, verify=False,headers=headers)
getcontent = r.content.decode("ISO-8859-1") #get the entire content of website if successful
jsfind = re.findall(javascriptregex,getcontent,re.IGNORECASE)


hiddenregexnew = "\"hidden\" name=\"\w*\" value=\"\w*\""
endpointsnew = "\/\w*"
if len(jsfind) == 0:
        print("0 javascript files found in ", url)
else:
        print(len(jsfind), "js found:", "\n")
        for x in jsfind:
                print(url, "==>" + x)

print("calling the js files found..")
if ".js" in getcontent:
        jsfindnew = str(jsfind)
        jsanalyzis = url + jsfindnew
        callnewjs = requests.get(url=jsanalyzis,verify=False,headers=headers)
        newjsdecode = callnewjs.content.decode("ISO-8859-1")
        newjsfoundhidden = re.findall(hiddenregexnew,newjsdecode,re.IGNORECASE)
        newjsfoundendpoints = re.findall(endpointsnew, newjsdecode, re.IGNORECASE)
        print("js found in ", jsanalyzis, newjsfoundhidden, newjsfoundendpoints)
