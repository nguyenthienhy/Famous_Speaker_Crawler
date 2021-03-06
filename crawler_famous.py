from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
from download import *
from tqdm import tqdm
import selenium
import config
import time
import urllib
import os
import urllib3

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def get_audio_keyword(keyword):

    driver = wd.Chrome(executable_path=r"tool/chromedriver.exe",chrome_options=options)

    if not os.path.isdir("data/" + "_".join(keyword.split())):
        os.mkdir("data/" + "_".join(keyword.split()))

    keyword_search = urllib.parse.quote(keyword + ' talkshow')
    f_url = config.url + (config.params % keyword_search)

    try:

        driver.get(f_url)

        for _ in range(config.loops_to_scoll):
            driver.execute_script('window.scrollBy(0,1000)')
            time.sleep(config.time_sleep)
        
        sections = driver.find_elements_by_tag_name("ytd-item-section-renderer")

        print("Number of sections: " + str(len(sections)))

        for section in sections:
            videos = section.find_elements_by_tag_name('ytd-video-renderer')
            for v in videos:
                try:
                    video_title = v.find_element_by_id('video-title').text
                    if video_title.lower().__contains__(keyword.lower()):
                        url = v.find_element_by_id('thumbnail').get_attribute('href')
                        download(url=url, keyname="data/" + "_".join(keyword.split()))
                except selenium.common.exceptions.NoSuchElementException as e:
                    continue
        
        driver.close()
        driver.quit()

    except urllib3.exceptions.MaxRetryError as e:
        print(e)
        driver.close()
        driver.quit()

    driver.close()
    driver.quit()

if __name__ == "__main__":

    f = open("dv.txt", "r", encoding="utf8")
    dvs = [dv.replace("\n", "") for dv in f.readlines()]

    with Pool(processes=6) as p:
        list(tqdm(p.imap(get_audio_keyword, dvs), total=len(dvs)))