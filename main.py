from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import Fore
import time
import requests
import os
import ctypes
import sys
import random
import re

THIS_VERSION = "2.3.0"
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX

response = requests.get("https://raw.githubusercontent.com/nyxical420/DeBomber/main/words.txt")
words = response.text.splitlines()
word_list = list(words)
word_dict = {word: word for word in word_list}


def hometitle():
    print(f"""\n\n   
                            ██╗██╗  ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
                            ██║██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                            ██║█████╔╝ ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
                       ██   ██║██╔═██╗ ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                       ╚█████╔╝██║  ██╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
                        ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                                                                               \n""".replace('█',
                                                                                                             f'{b}█{y}'))


def loader():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Cooking... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - made by aspect")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - made by aspect\x07")
    else:
        pass


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n' * 120)
    return


def transition():
    clear()
    loader()
    clear()


def credits():
    print(
        f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}  ub.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://gith\n{y}------------------------------------------------------------------------------------------------------------------------\n""")


string = 'hi'


# hometitle()
# setTitle(string)
# loader()


def main():
    clear()
    setTitle(f"JKCRACK Menu v{THIS_VERSION}")
    hometitle()
    print(f"""      {y}[{b}-{y}]{w} Main Options:           
    \n          {y}[{w}01{y}]{w} Auto Play               
    \n          {y}[{w}02{y}]{w} Word Helper             
    \n          {y}[{w}03{y}]{w} SOON™️             
    \n          {y}[{w}04{y}]{w} SOON™️                                      
    \n          {y}[{w}05{y}]{w} SOON™️                                 
    \n                                                                     
    \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    if choice == '1':
        transition()
        hometitle()
        credits()
        scan()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '2':
        transition()
        hometitle()
        credits()
        helper()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '3':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '4':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '5':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")

def helper():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://jklm.fun/")
    input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Hit enter once you are in a game! ")
    while True:
        try:
            driver.switch_to.frame(
                driver.find_element(By.XPATH,
                                    "//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))
            break
        except:
            print("error while switching to frame")
            pass

    words_printed = False
    while True:
        try:
            playerturn = driver.find_element(By.CLASS_NAME, "selfTurn")
            opponentturn = playerturn.get_attribute("hidden")
            roundStartXPATH = "/html/body/div[2]/div[1]/div/header"
            roundText = driver.find_element(By.XPATH, roundStartXPATH).text
            if opponentturn:
                words_printed = False
            if not opponentturn and not roundText:
                if not words_printed:
                    print(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} It is your turn! Searching for words...")
                    syllable = driver.find_element(By.CLASS_NAME, "syllable").text
                    word = searchandretreive(syllable, 3)
                    print(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Your words are: ", word)
                    words_printed = True

        except Exception as e:
            print(e)


def scan():
    print(f"""      {y}[{b}-{y}]{w} What typing mode would you like (none will ban):           
        \n          {y}[{w}01{y}]{w} Blatant (instant, good playing against bots)               
        \n          {y}[{w}02{y}]{w} Fast Type (types fast but is quite blatant)      
        \n          {y}[{w}03{y}]{w} Legit Type (types ~60 wpm with breaks, undetectable)                                        
        \n                                                                     
        \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    typingChoice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://jklm.fun/")
    input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Hit enter once you see the 'JOIN GAME' button!")
    while True:
        try:
            driver.switch_to.frame(
                driver.find_element(By.XPATH,
                                    "//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))
            break
        except:
            print("error while switching to frame")
            pass

    while True:
        try:
            driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[3]/div[1]/div[1]/button").click()
            break
        except:
            print("error while trying to click start button")
            pass


    while True:
        try:
            playerturn = driver.find_element(By.CLASS_NAME, "selfTurn")
            opponentturn = playerturn.get_attribute("hidden")
            answerXPATH = "/html/body/div[2]/div[3]/div[2]/div[2]/form/input"
            if not opponentturn:
                syllable = driver.find_element(By.CLASS_NAME, "syllable").text
                answerbox = driver.find_element(By.XPATH, answerXPATH)
                answerbox.click()
                word = searchandretreive(syllable, 1)
                checksyllable = driver.find_element(By.CLASS_NAME, "syllable").text
                if checksyllable.lower() in word:
                    if typingChoice == "1":
                        driver.find_element(By.XPATH, answerXPATH).send_keys(word)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    if typingChoice == "2":
                        for char in word:
                            driver.find_element(By.XPATH, answerXPATH).send_keys(char)
                            time.sleep(random.randint(1, 10)/1000)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    if typingChoice == "3":
                        lenWord = len(word)
                        middleOfWord = round(lenWord / 2)
                        time.sleep(random.uniform(1, 2.5))
                        for i in range(lenWord):
                            if i == middleOfWord:
                                time.sleep(1)
                                driver.find_element(By.XPATH, answerXPATH).send_keys(word[i])
                            else:
                                driver.find_element(By.XPATH, answerXPATH).send_keys(word[i])
                                time.sleep(random.randint(80, 100) / 1000)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    else:
                        driver.find_element(By.XPATH, answerXPATH).send_keys(word)
                else:
                    if typingChoice == "1":
                        driver.find_element(By.XPATH, answerXPATH).send_keys(word)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    if typingChoice == "2":
                        for char in word:
                            driver.find_element(By.XPATH, answerXPATH).send_keys(char)
                            time.sleep(random.randint(1, 10)/1000)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    if typingChoice == "3":
                        lenWord = len(word)
                        middleOfWord = round(lenWord / 2)
                        time.sleep(random.uniform(1, 2.5))
                        for i in range(lenWord):
                            if i == middleOfWord:
                                time.sleep(1)
                                driver.find_element(By.XPATH, answerXPATH).send_keys(word[i])
                            else:
                                driver.find_element(By.XPATH, answerXPATH).send_keys(word[i])
                                time.sleep(random.randint(80, 100) / 1000)
                        driver.find_element(By.XPATH, answerXPATH).send_keys(Keys.ENTER)
                    else:
                        driver.find_element(By.XPATH, answerXPATH).send_keys(word)
            else:
                pass
        except:
            pass




def find_words(word_index, letters):
    idx = tuple(sorted(letters))
    return word_index[idx]


def searchandretreive(addon, numOfWords):
    possible_words = []
    loweredaddon = addon.lower()
    found_words = [word for word in word_dict if re.search(loweredaddon, word)]
    if numOfWords == 1:
        word = random.choice(found_words)
        return word
    else:
        for i in range(numOfWords):
            word = random.choice(found_words)
            possible_words.append(word)

    return possible_words

if __name__ == "__main__":
    main()
