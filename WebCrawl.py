import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs of the websites you want to scrape
urls = [
    'https://www.seabaycargo.com/alphabetical/port-code/a.html',
    'https://www.seabaycargo.com/alphabetical/port-code/b.html',
    'https://www.seabaycargo.com/alphabetical/port-code/c.html',
    'https://www.seabaycargo.com/alphabetical/port-code/d.html',
    'https://www.seabaycargo.com/alphabetical/port-code/e.html',
    'https://www.seabaycargo.com/alphabetical/port-code/f.html',
    'https://www.seabaycargo.com/alphabetical/port-code/g.html',
    'https://www.seabaycargo.com/alphabetical/port-code/h.html',
    'https://www.seabaycargo.com/alphabetical/port-code/i.html',
    'https://www.seabaycargo.com/alphabetical/port-code/j.html',
    'https://www.seabaycargo.com/alphabetical/port-code/k.html',
    'https://www.seabaycargo.com/alphabetical/port-code/l.html',
    'https://www.seabaycargo.com/alphabetical/port-code/m.html',
    'https://www.seabaycargo.com/alphabetical/port-code/n.html',
    'https://www.seabaycargo.com/alphabetical/port-code/o.html',
    'https://www.seabaycargo.com/alphabetical/port-code/p.html',
    'https://www.seabaycargo.com/alphabetical/port-code/q.html',
    'https://www.seabaycargo.com/alphabetical/port-code/r.html',
    'https://www.seabaycargo.com/alphabetical/port-code/s.html',
    'https://www.seabaycargo.com/alphabetical/port-code/t.html',
    'https://www.seabaycargo.com/alphabetical/port-code/u.html',
    'https://www.seabaycargo.com/alphabetical/port-code/v.html',
    'https://www.seabaycargo.com/alphabetical/port-code/w.html',
    'https://www.seabaycargo.com/alphabetical/port-code/y.html',
    'https://www.seabaycargo.com/alphabetical/port-code/z.html',
    
]

# List to store all dataframes
dfs = []

for url in urls:
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with id="infoiata"
        table = soup.find('table', id='infoiata')

        # Extract data from the table
        data = []
        # Find all rows in the table
        rows = table.find_all('tr')
        for row in rows:
            # Extract data from each cell in the row
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)

        # Convert the data into a DataFrame
        df = pd.DataFrame(data, columns=['Port Code', 'Port Name', 'Port Type', 'City', 'Column5'])
        
        # Append DataFrame to list
        dfs.append(df)
    except Exception as e:
        print(f"Error scraping data from {url}: {e}")

# Concatenate all dataframes into one if there is any data
if dfs:
    result_df = pd.concat(dfs, ignore_index=True)

    # Save concatenated DataFrame to Excel
    result_df.to_excel('data.xlsx', index=False)
else:
    print("No data scraped from any URL.")