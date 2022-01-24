from selenium import webdriver

PATH = "C:\msedgedriver\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.close()

