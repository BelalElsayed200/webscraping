import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 

jobs = []
company = []
location = []
skills = []
links = []
salary = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=navbl")

source = result.content 
#print(source)

soup = BeautifulSoup(source , "lxml") 
#print (soup) 



job_title = soup.find_all("h2" ,{"class" : "css-m604qf"} ) 

company_name= soup.find_all("a" , {"target":"_blank" , "rel":"noreferrer" , "class":"css-17s97q8"})

company_location = soup.find_all("span" , {"class":"css-5wys0k"})

Job_skills = soup.find_all("div" , {"class":"css-y4udm8" })



for i in range(len(job_title)):
    jobs.append(job_title[i].text)
    links.append(job_title[i].find("a").attrs['href'])
    company.append(company_name[i].text)
    location.append(company_location[i].text)
    skills.append(Job_skills[i].text)



for link in links:
    result = requests.get(link)
    source = result.content
    soup = BeautifulSoup(source , "lxml")
    salaries = soup.find("span" , {"class":"css-4xky9y"})
    salary.append(salaries.text)


    
#print(jobs , company ,location , skills )
file_list = [jobs , company , location , skills , links , salary]
exported = zip_longest(*file_list) 

with open("C:/Users/KIMOSTORE/Documents/wzfny.csv", "w") as myfile:
    wr = csv.writer(myfile) 
    wr.writerow(["jobs" , "company" , "location" , "skills" , "links" , "salary"]) 
    wr.writerows(exported) 











