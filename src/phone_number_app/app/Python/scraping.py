from selenium import webdriver
from time import sleep
import pandas
import random
from selenium.webdriver.common.by import By
import urllib.parse
import sys
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3112.113 Safari/537.36'\
    ] 
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--headless')
options.add_argument("--no-sandbox")

chromedriver_autoinstaller.install(True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

print("Good Luck!!")
box_search_what = "イタリアン"#sys.argv[1]
box_search_what_url = urllib.parse.quote(box_search_what)
box_search_where = "大阪府"#sys.argv[2]
box_search_where_url = urllib.parse.quote(box_search_where)

csv_file_name = '/var/www/html/phone_number_app/storage/app/public/python/result/' + box_search_what + '_' + box_search_where + '.csv'
csv_file_name1 = '/var/www/html/phone_number_app/storage/app/public/python/log/' + box_search_what + '_' + box_search_where + '.csv'
cols = ['社名','番号']
df = pandas.DataFrame(index=[], columns=cols)
lista = []
if True:
    number_p = 0
    while True:
        data_num=0
        url = "https://itp.ne.jp/keyword?keyword=" + box_search_what_url + "&areaword=" + box_search_where_url + "&sort=01&sbmap=false&area=13&from=" + str(number_p)
        driver.get(url)
        print(url)
        sleep(5)
        #print(driver.page_source)
        for i in range(4):
            try:
                row = ['','']
                print(i+1)
                xpath="/html/body/div/div/div[2]/div/div/div/div[2]/div/main/section[1]/div[2]/div[2]/div[2]/div[2]/div/div[" + str(i+1) + "]/div[3]/div[2]/div[2]/div[4]/p[@class='font_8']/a"
                
                company_name = driver.find_element(by=By.XPATH, value=xpath)
                print('yes')            
                row[0]=company_name.text
                xpath="/html/body/div/div/div[2]/div/div/div/div[2]/div/main/section[1]/div[2]/div[2]/div[2]/div[2]/div/div[" + str(i+1) + "]/div[4]/div[3]/div[3]/p/span[@class='wixui-rich-text__text']"
                company_phone = driver.find_element(by=By.XPATH, value=xpath)
                
                phone_number=company_phone.text.replace('(代)','')
                phone_number=phone_number.replace('-','')
                phone_number=phone_number.replace(' ','')
                row[1]=phone_number
                print(phone_number)
                data_num=data_num+1
                if phone_number not in lista:
                    lista.append(phone_number)
                    df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
            except:
                print('err')

        for i in range(16):
            try:
                row = ['','']
                xpath="//div[4]/div/div[" + str(i+1) + "]/div[3]/div[2]/div[2]/div[4]/p/a"
                company_name = driver.find_element(by=By.XPATH, value=xpath)                
                row[0]=company_name.text
                
                xpath="//div[" + str(i+1) + "]/div[4]/div[3]/div[3]/p/span"
                company_phone = driver.find_element(by=By.XPATH, value=xpath)
                
                phone_number=company_phone.text.replace('(代)','')
                phone_number=phone_number.replace('-','')
                phone_number=phone_number.replace(' ','')
                row[1]=phone_number
                print(phone_number)
                data_num=data_num+1
                if phone_number not in lista:
                    lista.append(phone_number)
                    df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
            except:
                print('errrr')
        number_p = number_p + 20
        df.to_csv(csv_file_name1,index=False,encoding="cp932",errors="ignore")
        print("oh")
        print(number_p)
        print('food')
        if number_p>50:
            break
        if data_num == 0:
            break
    driver.quit()
print("succeed")
df.to_csv(csv_file_name,index=False,encoding="cp932",errors="ignore")