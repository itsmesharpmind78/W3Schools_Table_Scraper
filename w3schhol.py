import requests
from lxml import html
import pandas as pd

# Step 1: Fetch the webpage
url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)

# Step 2: Parse HTML
tree = html.fromstring(response.content)

# Step 3: Select all rows except the header
# Use relative XPath from table
rows = tree.xpath('//*[@id="customers"]/tr[position()>1]')

# Step 4: Extract data
data = []
for row in rows:
    cols = row.xpath('./td/text()')
    if len(cols) == 3:  # ensure row has 3 columns
        name = cols[0].strip()
        country = cols[1].strip()
        city = cols[2].strip()
        data.append({
            "Name": name,
            "Country": country,
            "City": city
        })

# Step 5: Verify data
print(data)  # Should print all rows

# Step 6: Convert to DataFrame
df = pd.DataFrame(data)

# Step 7: Export CSV & Excel
df.to_csv("customers.csv", index=False)
df.to_excel("customers.xlsx", index=False)

print("Scraping completed! CSV & Excel saved.")
