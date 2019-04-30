# variable name depends on you
greeting = "hello world"
number = 1
print(greeting) # output: hello world

import os
path = os.getcwd()
os.listdir(path) # output: files within the directory 

#
names = ["金吒", "木吒", "哪吒"]
len(names) # output: the sum of names list -- 3

# 
import requests
url = "https://www.example.com/article/?q=1"
response = requests.get(url)
print(response.text) # output: a string representaion of html

#
from selenium import webdriver
path_to_driver = '/home/fish/\
Desktop/chromedriver_linux64/chromedriver'
browser = webdriver.Chrome(path_to_driver)
browser.get("https://www.example.com")