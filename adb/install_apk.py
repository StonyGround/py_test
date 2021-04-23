import json
import os

import requests


def download_apk(type):
  url = "https://api.beicaizs.com/compliance/app-release/get-current-version?isApp=" + str(
      type)
  ret = requests.get(url)
  if ret.status_code == 200:
    data = json.loads(ret.text)
    print(data['data']['link'])
    f = requests.get(data['data']['link'])
    with open("daemon.apk", "wb") as code:
      code.write(f.content)




download_apk(0)
