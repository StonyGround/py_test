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


def checkDaemon(devices):
    # 打开
    for dName in devices:
        try:
            for status in os.popen("adb -s " + dName + " shell pidof com.bc.daemon"):
                if len(status) < 0:
                    print(dName + "激活失败")
                else:
                    print(dName + "激活成功 pid=" + status)
        except:
            print(dName + "打开失败")


if __name__ == "__main__":
    try:
        devices = getDevicesAll()
    except:
        print("获取设备出错")
    try:
        checkDaemon(devices)
    except:
        print("启动错误")
