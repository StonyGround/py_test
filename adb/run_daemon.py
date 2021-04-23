import json
import os

import requests


def getDevicesAll():
  devices = []

  try:
    for dName_ in os.popen("adb devices"):
      if "\t" in dName_:
        if dName_.find("emulator") < 0:
          devices.append(dName_.split("\t")[0])
    devices.sort(cmp=None, key=None, reverse=False)
  except:
    pass

  print(u"\n设备名称: %s \n总数量:%s台" % (devices, len(devices)))

  return devices


def runDaemon(dName):
  # 打开
  try:
    os.popen(
        "adb -s " + dName + " shell am start -n com.bc.daemon/.MainActivity ")
  except:
    print(dName + "打开失败")


def checkDaemon(devices):
  # 打开
  for dName in devices:
    try:
      os.popen(
          "adb -s " + dName + " shell pidof com.bc.daemon ")
    except:
      print(dName + "打开失败")


# 0后台进程
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


if __name__ == "__main__":
  download_apk(0)
  devices = getDevicesAll()
  for dName in devices:
    for dName_ in os.popen("adb -s " + dName + " install daemon.apk "):
      if 'Success' in dName_.strip():
        runDaemon(dName)
