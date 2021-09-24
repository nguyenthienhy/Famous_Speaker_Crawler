from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from download import *
import selenium
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(executable_path=r"tool/chromedriver.exe",chrome_options=options)

def get_name(url):
    
    driver.get(url)

    names = driver.find_elements_by_tag_name('div')

    print(len(names))

    with open("nguoi_noi_tieng.txt", "w", encoding="utf8") as f:
        for n in names:
            try:
                tag = n.find_element_by_class_name('tennnt').text
                # name = n.find_element_by_tag_name('h3').text
                f.write(tag + "\n")
            except selenium.common.exceptions.NoSuchElementException as e:
                continue

if __name__ == "__main__":
    get_name("https://nguoinoitieng.tv/nghe-nghiep/nghe-si-hai")