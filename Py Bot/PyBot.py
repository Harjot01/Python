from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sqlite3
import re
import schedule
from audio import speak
import pywhatkit as kit
from datetime import datetime


class Bot:
    # Setting up the URL
    __URL = "https://cuchd.blackboard.com"

    '''
    Function to start Chrome
    '''

    def start_browser(self):

        self.login_details()

        # Starts the Broswer
        print("Opening Google Chrome!")
        speak("Opening Google Chrome!")
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        opt.add_argument("--start-maximized")
        opt.add_argument("--use-fake-ui-for-media-stream")
        opt.add_argument("use-fake-ui-for-media-stream")

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(options=opt)

        # Maximizes the window
        self.browser.maximize_window()

        # Opens up the specified URL
        self.browser.get(Bot.__URL)

        WebDriverWait(self.browser, 10000).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'body')))

        # If the URL is appropriate then logins
        if("https://cuchd.blackboard.com" in self.browser.current_url):
            self.login()
    '''
    A function to take input of login details from the user
    '''

    def login_details(self):
        time.sleep(2)
        print("Hi my name is Botezzz and I will attend your online class")
        speak("Hi my name is Botezzz and I will attend your online class")
        time.sleep(1)

        # Checks if login_details.txt file is created or not
        if(not os.path.exists("login_details.txt")):
            with open("login_details.txt", "w") as details:
                print("So let's start by asking your name")
                speak("So let's start by asking your name")
                self.name = input("Enter your name: ")

                print("Cool {}, now please enter your login details and please do not worry your login details will be saved on your computer in this directory itself\n".format(self.name))

                speak("Cool {}, now please enter your login details and please do not worry your login details will be saved on your computer in this directory itself\n".format(self.name))

                self.__UID = input("Enter your UID: ")
                self.__PASSWD = input("Enter your PASSWD: ")
                self.__ph_no = input("Enter your contact number: ")

                details.write(self.name + "\n")
                details.write(self.__UID + "\n")
                details.write(self.__PASSWD + "\n")
                details.write(self.__ph_no)
        else:
            list = []
            with open("login_details.txt", "rt") as details:
                for detail in details:
                    list.append(detail)
            self.__UID = list[1]
            self.__PASSWD = list[2]
            self.__ph_no = list[3]
            
    '''
    A function to insert the login details that the user has entered
    '''

    def login(self):
        while True:
            try:
                # Accepting cookies
                self.browser.find_element(
                    By.XPATH, "//*[@id='agree_button']").click()

                # Entering the login details entered by the user
                # Log in UID
                self.browser.find_element(
                    By.XPATH, "//*[@id='user_id']").send_keys("21BCS7438")

                # Log in PASSWORD
                self.browser.find_element(
                    By.XPATH, "//*[@id='password']").send_keys("Waheguru@3958")

                # Signing In
                self.browser.find_element(
                    By.CLASS_NAME, "button").click()
                print("Login successfull!")
                speak("Login successfull!")
                break
            except:
                continue

    '''
    The function to create database
    '''

    def create_Database(self):
        self.conn = sqlite3.connect('TimeTable.db')
        cursor = self.conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS TimeTable(class text, start_time text, end_time text, day text)''')
        self.conn.commit()
        self.conn.close()
        print("Created TimeTable Database successfully")

    '''
    Validating time entered by the user
    '''

    def validating_input(self, regex, input):
        if not re.match(regex, input):
            return False
        else:
            return True

    '''
    Validating the day entered by the user
    '''

    def validating_day(self, input):
        self.days_list = ["monday", "tuesday", "wednesday",
                          "thursday", "friday", "saturday", "sunday"]

        if input.lower() in self.days_list:
            return True
        else:
            return False

    '''
    The function to add Time Table to our database
    '''

    def add_TimeTable(self):
        if(not(os.path.exists("TimeTable.db"))):
            self.create_Database()
        self.option = int(input("Press 1. Add class\nPress 2. Done Adding\n"))
        while(self.option == 1):
            self.class_name = input("Enter name of the class: ")
            self.start_time = input(
                "Enter class start time in 24 hours format :(HH:MM) ")
            while(not self.validating_input("\d\d:\d\d", self.start_time)):
                print("Invalid input, please try again")
                self.start_time = input(
                    "Enter class start time in 24 hours format :(HH:MM) ")

            self.end_time = input(
                "Enter class end time in 24 hours format :(HH:MM) ")
            while(not self.validating_input("\d\d:\d\d", self.end_time)):
                print("Invalid input, please try again")
                self.end_time = input(
                    "Enter class end time in 24 hours format :(HH:MM) ")

            self.day = input(
                "Enter the day (Monday/Tuesday/Wednesday/Thursay/Friday... : ")
            while(not self.validating_day(self.day.strip())):
                print("Invalid input, please try again")
                self.day = input(
                    "Enter the day (Monday/Tuesday/Wednesday/Thursay/Friday... : ")

            self.conn = sqlite3.connect('TimeTable.db')
            self.cursor = self.conn.cursor()

            self.conn.execute("INSERT INTO timetable VALUES ('%s','%s','%s','%s')" %
                              (self.class_name, self.start_time, self.end_time, self.day))

            self.conn.commit()
            self.conn.close()

            print("Your class has been added to the database\n")

            self.option = int(
                input("Press 1. Add class\nPress 2. Done Adding\n"))

    '''
    This function shows time table to the user
    '''

    def show_TimeTable(self):
        self.conn = sqlite3.connect('TimeTable.db')
        self.cursor = self.conn.cursor()
        for row in self.cursor.execute('SELECT * FROM TimeTable'):
            print(row)
        print("\n")
        self.conn.close()

    '''
    This function joins the class
    '''

    def join_class(self, class_name, start_time, end_time):

        try_time = []
        try_time.append(int(start_time.split(":")[0]))
        try_time.append(int(start_time.split(":")[1]))

        class_search = self.browser.find_element(
            By.XPATH, "//*[@id='main-content-inner']/div/div[1]/div[1]/div/div/div[1]/div/header/bb-search-box/div/input")
        class_search.click()
        class_search.send_keys(class_name)

        time.sleep(3)

        classbtn = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, class_name)
        classbtn.click()

        time.sleep(5)

        try:
            sessionlist = self.browser.find_element(
                By.XPATH, "//*[@id='sessions-list-dropdown']/span")
            courseRoomText = self.browser.find_element(By.XPATH,
                                                       '//*[@id="sessions-list"]/li[1]/a/span').get_attribute("innerText")
            print('str(courseRoomText): ' + str(courseRoomText))

            if str(courseRoomText) == "Course Room":
                sessionlist.click()
                clickRoom = self.browser.find_element(By.XPATH,
                                                      '//*[@id="sessions-list"]/li[2]/a')
                clickRoom.click()
                print("join button clicked!")
                print('Joining: ' + str(self.browser.find_element(By.XPATH,
                                                                  '//*[@id="sessions-list"]/li[2]/a/span')))

                # options
                skipaudio = self.browser.find_element(By.XPATH,
                                                      """//*[@id="dialog-description-audio"]/div[3]/button""")
                skipaudio.click()
                skipvideo = self.browser.find_element(By.XPATH,
                                                      """//*[@id="techcheck-modal"]/button""")
                skipvideo.click()
                skiptutorial = self.browser.find_element(By.XPATH,
                                                         """//*[@id="announcement-modal-page-wrap"]/div/div[4]/button""")
                skiptutorial.click()

            elif str(courseRoomText) != "Course Room":
                sessionlist.click()
                clickRoom = self.browser.find_element(By.XPATH,
                                                      '//*[@id="sessions-list"]/li[1]/a')
                clickRoom.click()
                print('Joining: ' + str(self.browser.find_element(By.XPATH,
                                                                  "//*[@id='sessions-list']/li/a")))
                # options
                skipaudio = self.browser.find_element(By.XPATH,
                                                      """//*[@id="dialog-description-audio"]/div[3]/button""")
                skipaudio.click()
                skipvideo = self.browser.find_element(By.XPATH,
                                                      """//*[@id="techcheck-modal"]/button""")
                skipvideo.click()
                skiptutorial = self.browser.find_element(By.XPATH,
                                                         """//*[@id="announcement-modal-page-wrap"]/div/div[4]/button""")
                skiptutorial.click()
        except:
            # join button not found
            # refresh every minute until found
            k = 1
            while(k <= 2):
                print("Join button not found, trying again")
                time.sleep(10)
                self.browser.refresh()
                self.join_class(class_name, start_time, end_time)
                schedule.every(1).minutes.do(
                    self.joinclass, class_name, start_time, end_time)
                k += 1
            print("Seems like there is no class today.")
            kit.sendwhatmsg("+91" + str(self.__ph_no),
                            f"*Class Name*\n{class_name}\n*Status*\nNo Class\n*Start Time*\n{start_time}\n*End Time*\n{end_time}", int(try_time[0]), int(try_time[1]) + 1)

        kit.sendwhatmsg("+91" + str(self.__ph_no),
                        f"*Class Name*\n{class_name}\n*Status*\nJoined\n*Start Time*\n{start_time}\n*End Time*\n{end_time}", int(try_time[0]), int(try_time[1]) + 1)

        # scheduling to leave the class
        tmp = "%H:%M"

        class_running_time = datetime.strptime(
            end_time, tmp) - datetime.strptime(start_time, tmp)

        time.sleep(class_running_time.seconds)
        self.browser.close()
        print("Class Left")

        kit.sendwhatmsg("+91" + str(self.__ph_no),
                        f"*Class Name*\n{class_name}\n*Status*\nLeft\n*Start Time*\n{start_time}\n*End Time*\n{end_time}", int(try_time[0]), int(try_time[1]) + 1)

    '''
    This function schedules the classes according to the time table stored
    in the database
    '''

    def sched(self):

        conn = sqlite3.connect('timetable.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM timetable'):
            # schedule all classes
            name = row[0]
            start_time = row[1]
            end_time = row[2]
            day = row[3]

            if day.lower() == "monday":
                schedule.every().monday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "tuesday":
                schedule.every().tuesday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "wednesday":
                schedule.every().wednesday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "thursday":
                schedule.every().thursday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "friday":
                schedule.every().friday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "saturday":
                schedule.every().saturday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))
            if day.lower() == "sunday":
                schedule.every().sunday.at(start_time).do(
                    self.join_class, name, start_time, end_time)
                print("Scheduled class '%s' on %s at %s" %
                      (name, day, start_time))

        self.start_browser()
        while True:
            schedule.run_pending()
            time.sleep(1)


'''
You cannot import this python file somewhere else
'''
if __name__ == "__main__":

    # instantiation of Bot class
    obj = Bot()

    # Asks the user
    option = int(input(
        "Press 1. Modify the Time Table\nPress 2. View the Time Table\nPress 3. Start Botezzz\nEnter Option: "))
    if(option == 1):
        obj.add_TimeTable()
    if(option == 2):
        obj.show_TimeTable()
    if(option == 3):
        obj.sched()
