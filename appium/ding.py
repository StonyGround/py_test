"""
钉钉自动打卡
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'deviceName': 'VTR_AL00',
                'appPackage': 'com.alibaba.android.rimet',
                'appActivity': '.biz.LaunchHomeActivity'}


def permission_allow():
    # time.sleep(3)
    for i in range(5):
        loc = (By.XPATH, "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1).until(expected_conditions.presence_of_element_located(loc))
            e.click()
        except:
            pass


if __name__ == '__main__':
    # 延迟执行
    # delay = random.randint(0, 5 * 60)
    # print(delay)
    # time.sleep(delay)
    print('开始执行...')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 获取当前分辨率
    el_x = driver.get_window_size()['width']
    el_y = driver.get_window_size()['height']

    # 权限处理
    permission_allow()
    # 点击登录
    driver.find_element_by_id('com.alibaba.android.rimet:id/login_slide_btn').click()

    # 输入账号密码
    driver.find_element_by_id('com.alibaba.android.rimet:id/et_phone_input').send_keys(
        '13221833392')
    driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login').send_keys('!cheng12')

    # 登录
    driver.find_element_by_id('com.alibaba.android.rimet:id/tv').click()
    print('登录成功...')

    # 协议
    agree = (MobileBy.ACCESSIBILITY_ID, '同意')
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(agree)).click()

    # 等待首页初始化
    # print('等待首页加载20s...')
    # time.sleep(20)

    # 点击考勤打卡
    punch = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.be/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View')
    p = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(punch))
    print('自动滑动...')
    driver.swipe(1 / 2 * el_x, 1 / 2 * el_y, 1 / 2 * el_x, 1 / 2 * el_y - 600 * el_y / 1920)
    p.click()
    # 权限处理
    permission_allow()
