from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages import page_list
import time
import codecs
import configparser
import os

fp_dir = os.getcwd()
config_path = fp_dir + '/config.ini'
config = configparser.ConfigParser()
config.read(config_path)
today = time.strftime("%Y-%m-%d")
filepath = fp_dir + '/Backstage_check_{}.txt'.format(today)
f = codecs.open(filepath, 'w', 'utf-8')
url = config['backstage']['url']
username = config['backstage']['user']
user_password = config['backstage']['password']
PASS = 0
FAIL = 0
version = ''
start = time.time()
# 取消網頁中的彈出視窗
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_argument("--headless")

driver = webdriver.Chrome('./chromedriver', options=options)
wait = WebDriverWait(driver, 3)


# 等待頁面
def wait_page(PATH, page_name):
    try:
        wait_p = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
        print(page_name + " [PASS]")
        f.write(page_name + " [PASS] \n")
        page_status = "PASS"

    except TimeoutException:
        print(page_name + " [FAIL]")
        f.write(page_name + " [FAIL] \n")
        page_status = "FAIL"
    return page_status


driver.maximize_window()

for key, value in page_list.items():
    if key == '登入':
        driver.get(url)
        status = wait_page(value[1], key)
        user_id = driver.find_element_by_id('user_id')
        password = driver.find_element_by_id('password')
        user_id.send_keys(username)
        password.send_keys(user_password)
        password.submit()
    else:
        if value[2] == 0:
            driver.get(url + value[0])
        else:
            driver.find_element_by_xpath(value[0]).click()
        status = wait_page(value[1], key)
    if status == "PASS":
        PASS += 1
    else:
        FAIL += 1

version = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div').text
print('版本: {}'.format(version))
f.write('版本: {}\n'.format(version))
print("PASS:{} ; FAIL:{} ; total:{}".format(PASS, FAIL, len(page_list)))
f.write("PASS:{} ; FAIL:{} ; total:{} \n".format(PASS, FAIL, len(page_list)))
end = time.time()
print("執行時間：%f 秒" % (end - start))
f.write("執行時間：%f 秒" % (end - start) + '\n')
f.close()
driver.quit()
