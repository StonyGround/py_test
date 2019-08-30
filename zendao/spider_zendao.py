import hashlib

import requests
from lxml import html

LOGIN_URL = 'http://192.168.1.188:88/zentao/user-login.html'
PASSWORD = 'cl12345678'
LOGIN_NAME = 'chenglong'

TASK_URL = 'http://192.168.1.188:88/zentao/my-task.html'


class ZendaoContent:
    login_cookies = dict

    def __init__(self):
        login_page = requests.get(LOGIN_URL)
        login_page.encoding = 'utf-8'
        sid = login_page.cookies['zentaosid']
        print('SID = ' + sid)
        login_tree = html.fromstring(login_page.text)
        verify_rand = login_tree.xpath('//*[@id="verifyRand"]')
        if verify_rand:
            verify_rand = verify_rand[0].attrib['value']
        print("verify_rand=" + verify_rand)
        hl = hashlib.md5()
        hl.update(PASSWORD.encode(encoding='utf-8'))
        print('Md5 第一次加密结果 = ' + hl.hexdigest())
        psd_result = hl.hexdigest() + verify_rand
        print(psd_result)
        hl_last = hashlib.md5()
        hl_last.update(psd_result.encode(encoding='utf-8'))
        print('Md5 第二次加密结果 = ' + hl_last.hexdigest())
        login_body = {"account": LOGIN_NAME, "password": hl_last.hexdigest(), "keepLogin[]": "on"}
        get_cookies = dict(zentaosid=sid, lang='zh-cn', keepLogin='on')
        print(get_cookies)
        requests.post(LOGIN_URL, data=login_body, cookies=get_cookies)
        self.login_cookies = get_cookies

    # 获取任务id
    def get_last_task_id(self):
        task_list_page = requests.get(TASK_URL, cookies=self.login_cookies)
        task_tree = html.fromstring(task_list_page.text)
        task_list = task_tree.xpath('//table[@id="tasktable"]/tbody/tr[1]/td[1]/text()')
        print("task_id=" + task_list[1].strip())
        return task_list[1].strip()

    # 根据任务id获取任务描述
    def get_task_content(self, task_id):
        url = 'http://192.168.1.188:88/zentao/task-view-' + task_id + '.html'
        task_page = requests.get(url, cookies=self.login_cookies)
        task_tree = html.fromstring(task_page.text)
        task_list = task_tree.xpath('//div[@class="detail-content article-content"]/p')
        for task in task_list:
            print(task.text.strip())
        return task_list

    # 根据任务id获取所属模块
    def get_project_name(self, task_id):
        url = 'http://192.168.1.188:88/zentao/task-view-' + task_id + '.html'
        task_page = requests.get(url, cookies=self.login_cookies)
        task_tree = html.fromstring(task_page.text)
        task = task_tree.xpath('//table[@class="table table-data"]/tbody/tr[2]/td/a')
        print("所属模块" + task[0].text.strip())
        return task[0].text.strip()
