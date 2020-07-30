from selenium import webdriver
import os, re, time, requests

#定义webdriver
webdriver_path =  'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
#无头模式
option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=webdriver_path, options=option)
#目标网站
epio_url = 'https://ulquiorra69.epio.app/article'


def get_all_img():
    driver.get(url=epio_url)
    driver.implicitly_wait(20)
    # driver.fullscreen_window()

#数组，保存图集的名称和URL
    imgs_name_src = []
#前三组图集
    for count in range(1,4): #(1,4)
        imgs_xpath = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div[{0}]/div/div[2]/a'.format(str(count)))
        imgs_src = imgs_xpath.get_attribute('href')
        imgs_name = imgs_xpath.text
        imgs_name_src.append((imgs_name,imgs_src))

#剩下的图集
    driver.get(url=epio_url)
    for i in range(0,10):
        driver.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight')
        time.sleep(0.5)
    for count in range(4,98): #(4,98)
        imgs_xpath = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div[{0}]/div/div[2]/a'.format(str(count)))
        imgs_src = imgs_xpath.get_attribute('href')
        imgs_name = imgs_xpath.text
        imgs_name_src.append((imgs_name, imgs_src))

    print(len(imgs_name_src))

#下载图片
    for j in range(len(imgs_name_src)):
        download_img(name=imgs_name_src[j][0] ,url=imgs_name_src[j][1])

#保存函数
def download_img(name, url):
    img_folder = 'img/'
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    path = 'img/{0}/'.format(name)
    if not os.path.exists(path):
        os.mkdir(path)
        print("--------Downloading : " + name + "--------")
        driver.get(url)
        driver.implicitly_wait(5)
        img_maxnum = int(re.findall(r"\d+",name)[-1])
        for img_num in range(1, img_maxnum+1):
            img_src = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/article/div[1]/p/img[{0}]'.format(str(img_num))).get_attribute('src')
            img = requests.get(url=img_src, headers=header).content
            f = open(path + str(img_num) + ".jpeg", mode='wb')
            print("Downloading : " + str(img_num) + ".jpeg")
            f.write(img)

if __name__ == '__main__':
    get_all_img()
