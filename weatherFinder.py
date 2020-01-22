from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk


def getTemperature(*args):
    # set up the input and url
    province = prvStr.get()
    city = cityStr.get()
    provinceIn = province.replace(' ', '-')
    cityIn = city.replace(' ', '-')
    url = "https://www.theweathernetwork.com/ca/weather/{}/{}".format(provinceIn, cityIn)

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
    location.set("The current weather in {}, {} is: {}".format(city, province, temp))
    locationLabel.grid()


root = Tk()
root.title("Weather Lookup")
window = ttk.Frame(root, padding='3 4 12 12')
window.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

prvStr = StringVar()
cityStr = StringVar()
location = StringVar()

title = ttk.Label(window, text="Weather Lookup v0.1")
title.grid(column=0, row=0, columnspan=3)
title.configure(foreground='blue', font='default, 32', padding=(10, 0, 0, 20))
ttk.Label(window, text="Enter province name: ").grid(column=0, row=1, sticky=W)
ttk.Label(window, text="Enter city name: ").grid(column=0, row=2, sticky=W)

provinceEntry = ttk.Entry(window, width=7, textvariable=prvStr)
provinceEntry.grid(column=1, row=1, sticky=(W, S), columnspan=2)
cityEntry = ttk.Entry(window, width=7, textvariable=cityStr)
cityEntry.grid(column=1, row=2, sticky=(W, S))
calcButton = ttk.Button(window, text='Get Weather', command=getTemperature)
calcButton.grid(column=0, row=3, sticky=W)

locationLabel = ttk.Label(window, textvariable=location, padding='0 5 0 0')
locationLabel.grid(column=0, row=4, columnspan=3, sticky=E)
locationLabel.grid_forget()

provinceEntry.focus()
root.bind('<Return>', getTemperature)

root.mainloop()
