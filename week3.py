from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
url = "http://www.letskorail.com/"
driver.get(url)

# 필요 없는 창 끄기
windows = driver.window_handles

if 1 < len(windows):
    main = True
    for window in windows:
        if main:
            main = False
            continue
        else:
            driver.switch_to.window(window)
            driver.close()
driver.switch_to.window(driver.window_handles[0])

start = "부산"  # 출발역
xpath = "//input[@id = 'txtGoStart']"
driver.find_element_by_xpath(xpath).clear()
driver.find_element_by_xpath(xpath).send_keys(f"{start}\n")

end = "서울"  # 도착역
xpath1 = "//input[@id = 'txtGoEnd']"
driver.find_element_by_xpath(xpath1).clear()
driver.find_element_by_xpath(xpath1).send_keys(f"{end}\n")


xpath2 = "//img[@alt='달력']"
driver.find_element_by_xpath(xpath2).click()

driver.switch_to.window(driver.window_handles[1])

day = "d20201116"  # 출발 날짜 입력
xpath3 = f"//span[@id='{day}']"
driver.find_element_by_xpath(xpath3).click()
driver.switch_to.window(driver.window_handles[0])

xpath4 = "//select[@id='time']"
driver.find_element_by_xpath(xpath4).click()
t = '19\n'  # 시간 입력
driver.find_element_by_xpath(xpath4).send_keys(f"{t}")

xpath5 = "//img[@alt='승차권예매']"
driver.find_element_by_xpath(xpath5).click()

xpath6 = "//span[@class='point02']"
not_found = driver.find_elements_by_xpath(xpath6)
if not_found:
    print("해당 시간에는 열차가 없습니다.")
    driver.close()
else:
    xpath7 = "//input[@id='selGoTrainRa00']"
    driver.find_element_by_xpath(xpath7).click()
    xpath8 = "//img[@alt='조회하기']"
    driver.find_element_by_xpath(xpath8).click()

time.sleep(3)
xpath9 = "//tbody/tr[1]/td[6]/a[1]/img"
driver.find_element_by_xpath(xpath9).click()
time.sleep(1)
# login
id = "00000000"  # id
xpath10 = "//input[@id='txtMember']"
driver.find_element_by_xpath(xpath10).send_keys(f"{id}")
password = "********"  # password
xpath11 = "//input[@id='txtPwd']"
driver.find_element_by_xpath(xpath11).send_keys(f"{password}")
time.sleep(1)
xpath12 = "//img[@alt='확인']"
driver.find_element_by_xpath(xpath12).click()

# 필요 업는 창 끄기
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()
xpath14 = '//*[@id="btn_next"]'
driver.find_element_by_xpath(xpath14).click()
