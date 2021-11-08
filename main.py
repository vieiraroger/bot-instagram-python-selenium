from selenium import webdriver
import time




class BotInstagram():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def entrar_link(self, link):
        self.driver.get(link)

    def pegar_link_das_fotos(self):
        os_links = self.driver.find_elements_by_tag_name('a')
        
        todos_os_links = []
        for os_link in os_links:
            href = os_link.get_attribute("href")
            if(href.startswith("https://www.instagram.com/p/")):
                todos_os_links.append(href)
        
        return todos_os_links

    def dar_like(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

    def comentar(self, comentario):
        textarea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        time.sleep(1)
        textarea.click()
        time.sleep(1)
        textarea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        time.sleep(1)
        textarea.clear()
        time.sleep(1)
        textarea.send_keys(comentario)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]').click()

bot = BotInstagram()
bot.entrar_link("https://www.instagram.com/")
time.sleep(15)
bot.entrar_link("https://www.instagram.com/")
time.sleep(2)
links_fotos = bot.pegar_link_das_fotos()
print(links_fotos)

for link_foto in links_fotos:
    bot.entrar_link(link_foto)
    time.sleep(3)
    bot.dar_like()
    time.sleep(3)
    bot.comentar("Teste 123")
    time.sleep(3)
