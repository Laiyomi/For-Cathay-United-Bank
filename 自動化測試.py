from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#以手機模式開啟 chrome
mobile_emulation = {"deviceName":"iPhone 12 Pro"}
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)

#開啟國泰網頁
url = 'https://www.cathaybk.com.tw/cathaybk/'
driver.get(url)
time.sleep(2)
driver.save_screenshot('OpenURL.png')

#開啟漢堡列表
get_burger = driver.find_element(By.CSS_SELECTOR,'.cubre-o-header__burger')
get_burger.click()
#點按產品介紹
get_product_intro = driver.find_elements(By.CSS_SELECTOR,'.cubre-o-menu__btn')[1]
get_product_intro.click()
#點按信用卡
get_creditcard_list = driver.find_element(By.CSS_SELECTOR,'.cubre-o-menuLinkList__btn')
get_creditcard_list.click()
time.sleep(2)
driver.save_screenshot('OpenCreditCardList.png')
#取信用卡下表單數目
count_creditcard = driver.find_elements(By.CSS_SELECTOR,'div.cubre-o-menuLinkList__item.is-L2open  [id="lnk_Link"]')
print('列表長度為 : ',len(count_creditcard))

#進入卡片介紹
count_creditcard[0].click()
#點按停用卡類別
get_tab_of_deactive_card = driver.find_element(By.CSS_SELECTOR,'[data-anchor-btn = "blockname06"]')
ActionChains(driver).move_to_element(get_tab_of_deactive_card).perform()
get_tab_of_deactive_card.click()
#取停用卡數目
get_deactive_card_count = driver.find_elements(By.CSS_SELECTOR,"[data-anchor-block='blockname06'] .swiper-pagination-bullet")
for i in range(len(get_deactive_card_count)):
    ActionChains(driver).move_to_element(get_deactive_card_count[i]).click().perform()
    time.sleep(2)
    screenshot_name = f"screenshot{i+1}.png"
    driver.save_screenshot(screenshot_name)

print('停發信用卡張數為 : ',len(get_deactive_card_count))