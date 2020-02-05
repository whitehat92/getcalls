#python3 getcall_endpoints.py <anyurl>
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning
import re

requests.urllib3.disable_warnings()



endpointsregex = "(\/\w*)?(\w+\/)"
newendpointsregex = "(\/\w*)+(\d*)"
url = sys.argv[1]
if not "https://" in url:
        url = "https://" + url
headers={'User-agent':'Mozilla//5.0',}
r = requests.get(url=url, verify=False,headers=headers,timeout=2)
getcontent = r.content.decode("utf-8", "ignore") #get the entire content of website if successful, has to be ISO-8859-1 to decode the content
#decodedcontent = getcontent.decode("uft-8") if utf-8 it doesn't work as it can't decode an unspecified character
endpointsfind = re.findall(endpointsregex,getcontent,re.DOTALL) #this is to get a list

for endpointspresent in re.finditer(newendpointsregex, getcontent): #this already prints as an iteration like the usual
        print(endpointspresent.group())




