import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from executor.executors import ExecutorHost
def handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = None
        return result
    return wrapper

class ChromeRemote:
    def __init__(self, url=ExecutorHost.CHROME_REMOTE):
        self.url = url
        self.driver = None
    
    def handler(self, func):
        """Error handle"""
        def wrapper(*args, **kwargs):
            try:
                if self.driver:
                    return func(*args, **kwargs)
            except Exception as e:
                self.close()
            return self
        return wrapper

    def execute_cdp_cmd(self, cmd, params={}):
        resource = "/session/%s/chromium/send_command_and_get_result" % self.driver.session_id
        url = self.driver.command_executor._url + resource
        body = json.dumps({'cmd': cmd, 'params': params})
        response = self.driver.command_executor._request('POST', url, body)
        return response.get('value')
        
    def init(self):
        """Initial remote webdriver"""
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Remote(self.url, options=webdriver.ChromeOptions(), desired_capabilities=caps)
        print(f'View in VNC {ExecutorHost.CHROME_VNC}')
        return self
    
    def close(self):
        """Delete remote session if exists"""
        if self.driver:
            self.driver.quit()
            self.driver = None
        return self
    
    @handler
    def open_tab(self):
        """Open new tab and active this tab"""
        if self.driver:
            self.driver.execute_script("window.open('');")
            self.__driver.switch_to.window(self.__driver.window_handles[-1])
        return self
    
    @handler
    def add_cookie(self, cookie):
        """Add cookie for this session"""
        self.driver.delete_all_cookies()
        cookieList = cookie['cookies']
        for cookie in cookieList:
            cookie['sameSite'] = 'Strict'
            self.driver.add_cookie(cookie)
        return self
    
