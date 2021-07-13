from selenium import  webdriver
from selenium.webdriver.support.select import Select
import time,os,re,easygui
easygui.msgbox('在程序同目录下 yuming.txt \n第一行写 用户名\n第二行写 密码\n第三行写 分组\n第四行写 http://落地域名.com  \n第五行写 墙封域名         别加http://和www\n第六行写 墙封域名         别加http://和www','注意事项')
Web_url = "https://admin.gfwvip.com/login"
c = os.getenv("SystemDrive")  # 获取主盘符
path = c + "\chromedriver.exe"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
a = webdriver.Chrome(executable_path=path, desired_capabilities=header)
a.get(Web_url)
time.sleep(1)
with open('yuming.txt','r',encoding='utf-8') as f:
    TEXT=f.readlines()
user=TEXT[0]
pwd=TEXT[1]
yzm=easygui.multenterbox('易捷云最新验证码','注意','')[0]
a.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys(user)
a.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(pwd)
a.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(yzm)
a.find_element_by_xpath("//button[@class='el-button login-submit el-button--primary el-button--small']").click()
time.sleep(2)
a.find_element_by_xpath("//div[@class='el-submenu__title']").click()
time.sleep(0.5)
a.find_element_by_xpath("//li[@cindex='2']").click()
time.sleep(0.5)
def START(fz,tzdz,bqym):
        a.find_element_by_xpath("//div[@class='avue-crud__left']").click()
        time.sleep(0.5)
        a.find_element_by_xpath("//div[@class='el-radio-group']//span[contains(text(),'启用')]").click()
        a.find_element_by_xpath('//input[@placeholder="请选择 所在分组"]').click()
        time.sleep(1)
        a.find_elements_by_xpath('//li[@class="el-select-dropdown__item"]//span[contains(text(),"{}")]'.format(fz))[1].click()
        a.find_element_by_xpath("//div[@class='el-radio-group']//span[contains(text(),'180U')]").click()
        a.find_element_by_xpath("//input[@placeholder='请输入 原域名']").send_keys('*.{}'.format(bqym))
        a.find_element_by_xpath("//input[@placeholder='请输入 新域名']").send_keys(tzdz)
        a.find_element_by_xpath('//button[@class="el-button el-button--primary el-button--small"]/span[contains(text(),"保 存")]/..').click()
        time.sleep(1)
        try:
            a.find_element_by_xpath('//button[@class="el-button el-button--default el-button--small"]//span[contains(text(),"取 消")]').click()
            time.sleep(1)
        except Exception as f:
            pass
if __name__=='__main__':
    fza=TEXT[2]
    fz=fza.strip()
    time.sleep(0.2)
    tzdza=TEXT[3]
    tzdz=tzdza.strip()
    time.sleep(0.2)
    for i in TEXT[4::]:
        ae=i.strip()
        START(fz,tzdz,ae)
