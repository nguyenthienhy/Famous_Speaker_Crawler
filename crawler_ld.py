from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from download import *
import selenium

options = Options()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(executable_path=r"tool/chromedriver.exe", options=options)

def get_name(url):
    
    driver.get(url)

    names = driver.find_elements_by_tag_name('div')

    print(len(names))

    with open("nguoi_noi_tieng.txt", "a", encoding="utf8") as f:
        for n in names:
            try:
                tag = n.find_element_by_class_name('tennnt').text
                f.write(tag + "\n")
            except selenium.common.exceptions.NoSuchElementException as e:
                continue
    driver.quit()

if __name__ == "__main__":
    get_name("https://nguoinoitieng.tv/nghe-nghiep/nghe-si-hai/page3")