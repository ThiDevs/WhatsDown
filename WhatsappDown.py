from selenium import webdriver
import time
from pytube import YouTube 
last = 0
def main():
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\thiago\\AppData\\Local\\Google\\Chrome\\User Data\Default") #Path to your chrome profile
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]').click()
    time.sleep(1)
    element =  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    element.click()
    element.send_keys("Ola, eu sou o Bot do Thiago, me diz o que quer fazer?\n /Falar \n /'(Url do video)'")
    print("oie")
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    time.sleep(10)


    Check_New_Message(driver)
    Check_New_Command(driver,last)

def Check_New_Message(driver):
    global last
    for i in range(10,100,1):
        try:
            driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div[2]/div/span')            
            last = i    
        except Exception:
            pass   
            
    

def Check_New_Command(driver,i):
    text = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div[2]/div/span').text
    print(text)
    if text == "/Falar":
        name = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div[1]/span')

        element =  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        element.click()
        element.send_keys("Ola, "+name.text+" eu so sei falar isso por enquanto KKK")
        element.send_keys("\n você disse "+text)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    if "https" in text:
        element =  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        element.click()
        element.send_keys("Seu video está sendo processado... \n")
        yt = YouTube(text)
        print(yt.title)
        element.send_keys("O seu video é o: "+ yt.title)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

        videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(videos.default_filename)
        dir = "C:\\Users\\Thiago\\Desktop\\"
        videos.download(dir)
        dir = dir+videos.default_filename

        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div').click()
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input')
        element.send_keys(dir)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span').click()
        time.sleep(5000)


            
main()