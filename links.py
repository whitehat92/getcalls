import requests
import sys
from urllib3.exceptions import InsecureRequestWarning
import re
requests.urllib3.disable_warnings()

linksregex = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
url = sys.argv[1]
if not "https://" in url:
        url = "https://" + url
headers={'User-agent':'Mozilla//5.0',}
r = requests.get(url=url, verify=False,headers=headers,timeout=2)
getcontent = r.content.decode("utf-8", "ignore") #get the entire content of website if successful, has to be ISO-8859-1 to decode the content
linksall = re.findall(linksregex, getcontent, re.IGNORECASE)
for links in linksall: #print as an iteration
        print(links)
