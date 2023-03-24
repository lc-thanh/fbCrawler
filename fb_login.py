from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 1. Khai báo biến browser (đại diện cho trình duyệt)
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở 1 trang web
browser.get("http://facebook.com")

# 2.1. Điền thông tin vào ô user và pass
txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("0343689648")

txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("dmfacebook")

# 2.2. Submit form
txtUser.send_keys(Keys.ENTER)

# 3. Tạm dừng chương trình tầm 5s
sleep(10)

# 4. Đóng trình duyệt
browser.close()
