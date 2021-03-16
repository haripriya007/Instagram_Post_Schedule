# __author__ = 'Harimsv007'

import time # pip install time
from apscheduler.scheduler import Scheduler #pip install APScheduler==2.1.2
#import os
from selenium import webdriver #pip install selenium
import autoit #pip install autotit
#import pyautogui # pip install PyAutoGUI
from selenium.webdriver.common import action_chains
from win32api import Sleep # need to import windows api sleep time
# Start the scheduler
sched = Scheduler()
sched.start()
def post_text():
    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    #it is usde for Mobile view user agent instagram,there is no desktop post upload,so need to change mobile perspective view
    profile = webdriver.FirefoxProfile() 
    profile.set_preference("general.useragent.override", user_agent)
    driver = webdriver.Firefox(profile)
    driver.set_window_size(360,640)
    # CHROME/CHROMIUM
    #from selenium.webdriver.chrome.options import Options
    #mobile_emulation = {
    #    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    #    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
    #chrome_options = Options()
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #driver = webdriver.Chrome(chrome_options = chrome_options)
    url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    driver.get(url)
    time.sleep(10)
    field = driver.find_element_by_css_selector("input[type='text']")
    field.send_keys('')#Enter Your Username ''
    field = driver.find_element_by_css_selector("input[type='password']")
    field.send_keys('')#Enter your Password ''
    time.sleep(2)
    button=driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
    button[0].click() #Login
    time.sleep(5)
    button=driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
    if len(button) > 0:
        button[0].click()
    time.sleep(5)
    button=driver.find_elements_by_xpath("//*[contains(text(), 'Cancel')]")
    if len(button) > 0:
        button[0].click()
    time.sleep(2)
    button = driver.find_elements_by_css_selector('[aria-label="New Post"]')
    button[0].click()
    #lement = driver.find_element_by_id('[aria-label="New Post"]')
    #autoit.win_active("Open")
    #autoit.control_send("Open","Edit1",r"C:/Users/admin/Desktop/Reliving.jpg")
    #autoit.control_send("Open","Edit1","{ENTER}")
    def file_upload(filename):
        autoit.win_wait_active("File Upload",5)
        if autoit.win_exists("File Upload"):
            autoit.control_send("File Upload","Edit1",filename+"{ENTER}")
    Sleep(2)
    filename= " " #Enter Your Filename without their extension like photo.jpg need to give photo
    file_upload(filename)
    Sleep(20)
    #driver.send_keys("C:/Users/admin/Desktop/Reliving.jpg")
    #os.system('autokey-run -s select_image')
    time.sleep(10)
    button=driver.find_elements_by_xpath("//*[contains(text(), 'Expand')]")
    if len(button) > 0:
        button[0].click()
    time.sleep(20)
    button=driver.find_elements_by_xpath("//*[contains(text(), 'Next')]") #/html/body/div[1]/section/div[1]/header/div/div[2]/button
    if len(button) > 0:
        button[0].click()
    #button.click()
    #button=driver.find_elements_by_xpath("//*[contains(text(), 'Next')]")
    time.sleep(10)
    #field = driver.find_elements_by_tag_name('textarea')
    #if len(field) > 0:
    #    field[0].click()
    Caption_Click3 = driver.find_element_by_css_selector('[aria-label="Write a caption…"]')
    Caption_Click3.click()
    myPost = ["Enter Your Text Content"]
    #postContent = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]')
    Caption_Click3.send_keys(myPost) #Click my post
    #button = driver.find_elements_by_css_selector('[aria-label="New Post"]')
    #time.sleep(3._472V_ /html/body/div[1]/section/div[2]/section[1]/div[1]/textarea
    time.sleep(15)
    button = driver.find_elements_by_xpath("//*[contains(text(), 'Share')]")[1] #share
    driver.execute_script("arguments[0].scrollIntoView();", button);
    action = action_chains.ActionChains(driver)
    action.move_to_element(button)
    action.click()
    action.perform()
    time.sleep(15)
    driver.quit()
sched.add_cron_job(post_text, month='3', day='3rd mon', hour='15', minute="26") # this is for scheduling post time you can give scheduling time like this sample format given
#month You can add numbers for example if jan month you can give 1,if march month you can give 3
#day you need to calculate which weeks day if 3rd week monday or 2nd week monday
#hour need to write 24 hrs format

