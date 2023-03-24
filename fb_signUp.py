from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import random

browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# Truy cập Facebook
browser.get("http://facebook.com")
sleep(3)

# Click vào nút Tạo tài khoản mới
button_register = browser.find_element(By.XPATH, '//a[@data-testid="open-registration-form-button"]')
button_register.click()
sleep(2)

# Nhập họ, tên
txtLastName = browser.find_element(By.XPATH, '//input[@name="lastname"]')
txtLastName.send_keys("Lê Công")

txtFirstName = browser.find_element(By.XPATH, '//input[@name="firstname"]')
txtFirstName.send_keys("Thành")

# Nhập sđt/email
txtPhoneEmail = browser.find_element(By.XPATH, '//form[@id="reg"]/div[1]/div[2]/div/div[1]/input')
txtPhoneEmail.send_keys("abcxyz@ggg.com")
sleep(1)
retype_txtPhoneEmail = browser.find_element(By.XPATH, '//form[@id="reg"]/div[1]/div[3]/div/div/div[1]/input')
retype_txtPhoneEmail.send_keys("abcxyz@ggg.com")

# Nhập mật khẩu
txtPassword = browser.find_element(By.XPATH, '//input[@id="password_step_input"]')
txtPassword.send_keys("0159753")

# Chọn birthday
# Chọn năm
selectBirthday = Select(browser.find_element(By.XPATH, '//select[@name="birthday_year"]'))
year = random.randint(1990, 2002)
selectBirthday.select_by_visible_text(str(year))
# Chọn tháng
selectBirthday = Select(browser.find_element(By.XPATH, '//select[@name="birthday_month"]'))
month = random.randint(0, 11)
selectBirthday.select_by_index(month)
# Chọn ngày
selectBirthday = Select(browser.find_element(By.XPATH, '//select[@name="birthday_day"]'))
x = random.randint(1, 29)
selectBirthday.select_by_visible_text(str(x))

# Chọn giới tính
if random.randint(0, 1) == 0:
    selectGender = browser.find_element(By.XPATH, '//span[@data-name="gender_wrapper"]/span[1]/input')
    selectGender.click()
else:
    selectGender = browser.find_element(By.XPATH, '//span[@data-name="gender_wrapper"]/span[2]/input')
    selectGender.click()

# Submit
button_submit = browser.find_element(By.XPATH, '//button[@name="websubmit"]')
button_submit.click()

sleep(10)
