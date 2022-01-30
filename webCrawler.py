import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import json
from urllib.parse import urlparse
import bs4
import requests
# import result as result

endpoint = " "
serviceKey = " "

cl = "ARGUMENT_DAIL"
bgng_ymd ="20210101"
end_ymd ="20210331"
numOfRows ="100000"
pageNo ="1"

paramset = "serviceKey=" + serviceKey + "&" + "cl=" + cl + "&" + "bgng_ymd=" \
           + bgng_ymd + "&" + "end_ymd=" + end_ymd + "&" + "numOfRows=" + numOfRows + "&" + "pageNo=" + pageNo

url = endpoint + paramset
print(url)

result = requests.get(urlparse(url).geturl())
jason_obj = result.json()

for item in jason_obj["items"]:
    print(item["cn"])