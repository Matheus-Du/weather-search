from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set up the input and url
province = input("Enter the province you are in: ").lower()
city = input("enter a city in {}: ".format(province)).lower()
province = province.replace(' ', '-')
city = city.replace(' ', '-')
url = "https://www.theweathernetwork.com/ca/weather/{}/{}".format(province, city)

# initiate a headless chrome browser
chromeOptions = Options()
chromeOptions.add_argument("--headless")
browser = webdriver.Chrome("drivers/chromedriver", options=chromeOptions)
# go to the webpage
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
# find the spans in the HTML text and put them into a list
spans = soup.find_all("span")
# close the browser
browser.quit()

# find the correct temperature from the list of spans
temp = ''
for i in range(len(spans)):
    spans[i] = str(spans[i])
    if "<span class=\"temp\">" in spans[i]:
        temp = spans[i]
        break
# isolate just the temperature from the string
temp = temp.replace("<span class=\"temp\">", '')
temp = temp.replace("</span>", '')
# print the temperature
print("it is currently {} degrees outside in {}".format(temp, city))
