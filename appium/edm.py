from appium import webdriver

ACTIVITY_SPLASH = 'com.module.main.ui.splash.SplashActivity'
ACTIVITY_MAIN = 'com.module.main.ui.main.MainActivity'

desired_caps = {'platformName': 'Android', 'deviceName': 'VTR_AL00',
                'appPackage': 'com.hoolink.edm',
                'appActivity': ACTIVITY_SPLASH}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.wait_activity('com.module.main.ui.main.MainActivity', 5)
driver.find_element_by_id('com.hoolink.edm:id/tv_login_confirm').click()

