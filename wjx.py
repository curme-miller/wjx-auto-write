from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random,time,pretty_errors

class WJX(object):
    def __init__(self,radio,input_number,single_number,multiple_number, web_driver):
        self.single_radio = radio[:single_number]
        self.multiple_radio = radio[single_number:]
        self.number = input_number
        self.single_number = single_number
        self.multiple_number = multiple_number
        self.driver = web_driver
        self.single = []
        self.multiple = []

    def single_choice_question(self):
        for number in range(self.single_number):
            element = self.driver.find_element(By.ID,'div{}'.format(str(number+1)))
            self.single.append(element)
    
    def choose_single(self):
        for number in range(single_number):
            time.sleep(1)                    #加入延时主要是为了规避问卷星的验证
            elements = self.single[number].find_elements(By.CLASS_NAME,'jqradio')
            question_choice = [i for i in range(len(self.single_radio[number]))]
            selected_number = random.choices(question_choice, self.single_radio[number], k=1)[0]
            elements[selected_number].click()
    
    def multiple_choice_question(self):
        for number in range(multiple_number):
            element = self.driver.find_element(By.ID,'div{}'.format(str(number+1+self.single_number)))
            self.multiple.append(element)

    def choose_multiple(self):
        for number in range(self.multiple_number):
                time.sleep(1)                   #加入延时主要是为了规避问卷星的验证
                elements = self.multiple[number].find_elements(By.CLASS_NAME,'jqcheck')
                choose_number = random.randint(3,len(elements))
                question_choice = [i for i in range(len(elements))]
                selected_numbers = random.choices(question_choice, self.multiple_radio[number], k=choose_number)
                selected_numbers = list(set(selected_numbers))
                for i in range(len(selected_numbers)):
                    elements[selected_numbers[i]].click()

    def submitdata(self):
        element = self.driver.find_element(By.ID,'ctlNext')
        element.click()

    def change(self):
        try:
            element = self.driver.find_element(By.ID,'captchaWrap')
            element.click()
        except:
            pass

    def exit(self):
        self.driver.close()


if __name__ == '__main__':
    question_radio = [
        [0.4,0.6],#q1
        [0.2,0.1,0.2,0.25,0.1,0.05,0.05,0.05],#q2
        [0.46,0.32,0.11,0.11],#q3
        [0.41,0.1,0.34,0.15],#q4
        [0.2,0.12,0.24,0.13,0.31],#q5
        [0.71,0.29],#q6
        [0.65,0.35],#q7
        [0.34,0.11,0.55],#q8
        [0.35,0.12,0.36,0.17],#q9
        [0.2,0.8],#q10
        [0.85,0.15],#q11
        [0.76,0.24],#q12
        [0.06,0.15,0.34,0.25,0.1],#q13
        [0.78,0.22],#q14
        [0.12,0.88],#q15
        [0.3,0.2,0.13,0.12,0.1,0.15],#q16
        [0.11,0.13,0.05,0.22,0.08,0.41],#q17
        [0.5,0.11,0.132,0.15,0.1,0.08],#q18
        [0.31,0.23,0.12,0.3,0.04] #q19
    ] #single:15      multiple:4
    print('请输入各类题目数量\n'+'格式：[单选题数目] [多选题数目] [填空题数目]')
    url = input('请输入网址：')
    input_number = int(input('需要几份:'))
    
    single_number = int(input('single number:'))
    multiple_number = int(input('multiple number:'))

    for num in range(input_number):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        wjx = WJX(question_radio,input_number,single_number,multiple_number,driver)
        wjx.single_choice_question()
        wjx.choose_single()
        wjx.multiple_choice_question()
        wjx.choose_multiple()
        time.sleep(1)                     #加入延时主要是为了规避问卷星的验证
        wjx.submitdata()
        time.sleep(2)                     #加入延时主要是为了规避问卷星的验证
        wjx.change()
        time.sleep(3)                     #加入延时主要是为了规避问卷星的验证
        wjx.exit()
        time.sleep(3)                     #加入延时主要是为了规避问卷星的验证
        print('No.{}'.format(num+1))

    print('The task is end!')
    