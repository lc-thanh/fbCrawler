from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
try:
    # 2. Mở URL của post
    browser.get(
        "https://www.facebook.com/fitmediahaui/posts"
        "/pfbid02v29drN51UmqVB8uosQJd5TqVYZy1Yea8J3xyj9BfNYs7N9A9n7wjiAs8HDSjccncl?")
    sleep(5)

    # 3. Mở link hiện comments
    showComments_link = browser.find_element(By.XPATH,
                                             '//form[@class="commentable_item collapsed_comments"]/div[2]/div[2]/div['
                                             '1]/div/div[3]/span[1]/a')
    showComments_link.click()
    sleep(5)
    browser.execute_script('window.scrollTo( 0,  window.scrollY +200)')
    # 4. Mở link thêm comments
    showMoreComments_link = browser.find_element(By.XPATH,
                                                 '//form[@class="commentable_item collapsed_comments"]/div[2]/div['
                                                 '3]/div[1]/div[1]/a')
    showMoreComments_link.click()
    sleep(5)

    # 5. Crawl comments và ghi vào file 'cmt_crawled.txt'
    outFile = open("./cmt_crawled.txt", "w", encoding='utf-16')
    comment_list = browser.find_elements(By.XPATH,
                                         '//form[@class="commentable_item collapsed_comments"]/div[2]/div[3]/ul/li')
    for comment in comment_list:
        print("text " + str(comment.text))
        outFile.write(str(comment.text).strip())
        outFile.write("\n")
    outFile.close()
    # browser.close()

except Exception as ex:
    print("error " + str(ex))
    sleep(200)
