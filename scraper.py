'''
Francisco Figueroa
04/29/2022
scraper.py
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

url = r'https://www.nba.com/stats/players/advanced/?sort=GP&dir=-1' #can change this
driver = webdriver.Chrome() #webdriver.Firefox()
driver.get(url)
select = Select(driver.find_element('xpath', r"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")) 
select.select_by_index(0)
source = driver.page_source
parser = BeautifulSoup(source, 'lxml')
table = parser.find("div", attrs={"class": "nba-stat-table__overflow"})
titles = table.find_all('th')
#clean each title of html tags and placing them in an array exluding the first
header = [title.text.strip() for title in titles[1:]]
#keeping each element in og header that does not contain hidden attr "RANK"
header = [el for el in header if not "RANK" in el]
header = header[:-5]
rows = table.findAll('tr')[1:]
#for every row in table, find all <td> tags and strip them of anything not the data
stats = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
df = pd.DataFrame(stats, columns=header)
print(df.to_string())#quick print to show constructed dataframe


