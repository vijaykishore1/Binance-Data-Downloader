from constants import CHART_TIME_STRING, HTML_TEXT, BINANCE_URL

CHART_TIME_STRING = CHART_TIME_STRING.replace(" ", "")
CHART_TIME_ARRAY = CHART_TIME_STRING.split(",")

from bs4 import BeautifulSoup

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(HTML_TEXT, 'lxml')
# print(soup.prettify())
containers = soup.find_all('div', class_='container-md')[1]
table_rows = containers.find('tbody', {'id': 'listing'}).find_all("tr")
URL_ARRAY = [row.find("td").find('a').get('href') for row in table_rows]
URL_ARRAY.pop(0)
for link in URL_ARRAY:
    print(link)

from datetime import datetime, timedelta

# Set the start date and end date
start_date = datetime(2020, 1, 1)
end_date = datetime(2040, 1, 1)

# Initialize the list of year-month pairs
MONTH_ARRAY = []

# Iterate over the dates from start to end
date = start_date
while date < end_date:
    # Format the date as a year-month pair
    year_month = date.strftime("%Y-%m")

    # Add the year-month pair to the list
    MONTH_ARRAY.append(year_month)

    # Increment the date by one month
    date += timedelta(days=31)

SYMBOL_ARRAY = []
for url in URL_ARRAY:
    symbol = url.replace(BINANCE_URL, "").replace("/", "")
    SYMBOL_ARRAY.append(symbol)
print(SYMBOL_ARRAY)
print(MONTH_ARRAY)
print(CHART_TIME_ARRAY)
print(URL_ARRAY)
