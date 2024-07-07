from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Browser options
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir","C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201803_QLD1 (1).csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201802_QLD1 (1).csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201801_QLD1 (1).csv",
"C:\Users\Adithiyha R\Downloads\prices_dataset (3).csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201812_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201811_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201810_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201809_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201808_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201807_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201806_QLD1.csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201805_QLD1 (1).csv",
"C:\Users\Adithiyha R\Downloads\PRICE_AND_DEMAND_201804_QLD1 (1).csv")
options.set_preference("browser.helperApps.neverAsk.openFile", "application/vnd.ms-excel")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

# Fetching data from AEMO
driver = webdriver.Firefox(options=options)
driver.get('https://www.aemo.com.au/Electricity/National-Electricity-Market-NEM/Data-dashboard#aggregated-data')

tab = driver.find_element_by_id('dashADF')
year = webdriver.support.ui.Select(tab.find_element_by_xpath("//select[@data-type='year']"))
month = webdriver.support.ui.Select(tab.find_element_by_xpath("//select[@data-type='month']"))

year.select_by_value('2018')
month.select_by_value('March')

download_btn = tab.find_element_by_xpath("//*[contains(text(), 'Download Historic Data as .csv')]")
download_btn.click()

driver.close()

    