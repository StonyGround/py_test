import os


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


def runDaemon(devices):
    # 打开
    for dName in devices:
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


if __name__ == "__main__":
    try:
        devices = getDevicesAll()
    except:
        print("获取设备出错")

    res = input("继续请输入1:")
    if int(res) == 1:
        try:
            runDaemon(devices)
        except:
            print("启动错误")
