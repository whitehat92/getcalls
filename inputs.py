import requests
import sys
from urllib3.exceptions import InsecureRequestWarning
import re

requests.urllib3.disable_warnings()



#regex for hidden forms

hiddenregex = "<input type=\"hidden\" name=\"\w*\" value=\"\w*\""
inputregex = "<input type=\"\w*\" name=\"\w*\" value=\"\w*\""
allinputregex = "<(?:input)|(type=\"\w*\")|(value=\"\w*\")|(name=\"\w*\")"
#hiddenfind = re.findall(hiddenregex,getcontent,re.DOTALL)

url = sys.argv[1]
if not "https://" in url:
	url = "https://" + url
headers={'User-agent':'Mozilla//5.0',}
r = requests.get(url=url, verify=False,headers=headers)
getcontent = r.content.decode("ISO-8859-1") #get the entire content of website if successful
hiddenfind = re.findall(hiddenregex,getcontent,re.IGNORECASE)
inputfind = re.findall(allinputregex,getcontent,re.IGNORECASE)

print("found hidden parameters: ","\n", url, " ", "=>", hiddenfind)
print("Forms found: ", "\n", url, " ", "=>", inputfind)

#iteration like.. for x i $(cat <domains.txt>); do python3 inputs.py $x; done
#or simply python3 inputs.py <somedomain>
