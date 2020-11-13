import time
import poplib
from selenium import webdriver

studentNumber = "Insert Bilkent ID"
starsPassword = "Insert srs password"
userMail = 'your.name@ug.bilkent.edu.tr'
mailPassword = 'Insert Bilkent Mail password'
webDriverPath = 'Insert Chrome Webdriver path here'
#note that you can use different drivers but then you should 


def verification():
    pop3server = 'mail.bilkent.edu.tr'
    username =  userMail
    password =  mailPassword
    pop3server = poplib.POP3_SSL(pop3server, port=995)

    pop3server.user(username)
    pop3server.pass_(password)
    pop3info = pop3server.stat() 
    mailcount = pop3info[0]
    x = pop3server.retr(mailcount)[1]

    q = x[-2]
    q = q.decode("utf-8")       
    x = q.find("Code: ")
    q = q[x+6:x+11]
    
    pop3server.quit()
    return q

def test():
    driver = webdriver.Chrome(webDriverPath) #path--Please change it if you are using different webdriver

    driver.get("https://stars.bilkent.edu.tr/srs")
    driver.maximize_window()

    driver.find_element_by_xpath("//*[@id=\"LoginForm_username\"]").send_keys(studentNumber) #number
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/div/div/input").send_keys(starsPassword) #srs password
    driver.find_element_by_xpath("//*[@id=\"login-form\"]/fieldset/div/div[1]/div[3]/button").click()

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input").send_keys(verification())


    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/button").click()

test()
input()
