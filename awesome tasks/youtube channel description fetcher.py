from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,csv

option = Options()

with open("channel list.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        url = line.split()
        link = url[0]
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(2)
        driver.get(link)
        time.sleep(2)
        try:
            name = driver.find_elements_by_class_name("style-scope ytd-channel-name")
            channel = name[0].text

            subs = driver.find_elements_by_xpath('//*[@id="subscriber-count"]')
            sn = (subs[0].text).split(" ")
            snn = sn[0]

            joined = driver.find_elements_by_xpath('//*[@id="right-column"]/yt-formatted-string[2]/span[2]')
            join_date = joined[0].text

            views = driver.find_elements_by_xpath('//*[@id="right-column"]/yt-formatted-string[3]')
            t = (views[0].text).split(" ")
            totalView = t[0]

            print(f"{channel} | {join_date} | {totalView} | {snn}")
            with open("channel list.csv", 'a', newline='') as csvFile:
                cf = csv.writer(csvFile)
                cf.writerow([channel,link,join_date,totalView,snn])
                driver.close()
                time.sleep(3)
        except:
            with open("channel list.csv", 'a', newline='') as csvFile:
                cf = csv.writer(csvFile)
                cf.writerow(["not available",link,"not available","not available"])
                driver.close()
                time.sleep(3)