import requests
import bs4
import json
from urllib.parse import urlparse

import result as result

endpoint = "http://apis.data.go.kr/1250000/trend/getTrend?"
serviceKey = ""

cl = "ARGUMENT_DAIL"
bgng_ymd ="20210101"
end_ymd ="20210425"
numOfRows ="1000000"
pageNo ="1"

paramset = "serviceKey=" + serviceKey + "&" + "cl=" + cl + "&" + "bgng_ymd=" \
           + bgng_ymd + "&" + "end_ymd=" + end_ymd + "&" + "numOfRows=" + numOfRows + "&" + "pageNo=" + pageNo

url = endpoint + paramset
print(url)

result = requests.get(urlparse(url).geturl())
jason_obj = result.json()

for item in jason_obj["items"]:
    print(item["cn"])