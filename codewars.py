import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def get_kata_completed(username):
    print("Fetching completed katas...")
    url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed"
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    else:
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return None

def get_kata_description(kata_id):
    url = f"https://www.codewars.com/api/v1/code-challenges/{kata_id}"
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    else:
        if response.status_code == 200:
            return response.json()["description"]
        else:
            return None
    
def get_kata_completed_solution(username):
    url = f"https://www.codewars.com/users/{username}/completed_solutions"
    driver = webdriver.Chrome()
    connect_User(driver)
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    kata_collected = soup.find_all("div", class_="list-item-solutions")
    kata_completed_data = {}

    for kata in kata_collected:
        big_title = kata.find("div", class_="item-title")
        if big_title:
            kata_title = big_title.find("a").text.strip()
            kata_id = big_title.find("a")["href"].split("/")[-1]
            kata_code = kata.find("code").text.strip() if kata.find("code") else "Pas de code trouvé"
            kata_completed_data[kata_id] = { "name": kata_title, "code": kata_code}

    return kata_completed_data

def connect_User(driver):
    username = "yepiengesso@gmail.com"  # ou ton username
    password = "Hardboynedy1"

    driver.get("https://www.codewars.com/users/sign_in")
    time.sleep(2)
    driver.find_element(By.ID, "user_email").send_keys(username)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit" and text()="Sign in"]').click()
    time.sleep(5)
    