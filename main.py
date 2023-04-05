import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a table with two columns: DataSource and URL
conn.execute('''CREATE TABLE IF NOT EXISTS DataSources
             (DataSource TEXT, URL TEXT)''')

# Define a list of tuples with the data sources and their URLs
data_sources = [
    ('Google Dataset Search', 'https://datasetsearch.research.google.com'),
    ('Native Python Dataset', 'https://docs.python.org/3/library/index.html'),
    ('Kaggle', 'https://www.kaggle.com/'),
    ('Datahub.io', 'https://datahub.io/'),
    ('Data.gov', 'https://www.data.gov/'),
    ('UCI Machine Learning Repository', 'https://archive.ics.uci.edu/ml/index.php'),
    ('Earth Data', 'https://earthdata.nasa.gov/'),
    ('Gapminder', 'https://www.gapminder.org/data/'),
    ('CERN Open Data Portal', 'http://opendata.cern.ch/'),
    ('BFI Film Industry Statistics', 'https://www.bfi.org.uk/industry-data-education/film-industry-statistics-research/film-statistics/'),
    ('World Bank Open Data', 'https://data.worldbank.org/'),
    ('IMF Data', 'https://www.imf.org/en/Data'),
    ('Eurostat', 'https://ec.europa.eu/eurostat/data/database'),
    ('UN Data', 'https://data.un.org/'),
    ('OECD Data', 'https://data.oecd.org/'),
    ('The COVID Tracking Project', 'https://covidtracking.com/data'),
    ('FiveThirtyEight', 'https://data.fivethirtyeight.com/'),
    ('Bureau of Labor Statistics', 'https://www.bls.gov/data/'),
    ('National Centers for Health Statistics', 'https://www.cdc.gov/nchs/data_access/ftp_data.htm'),
    ('OpenStreetMap Data', 'https://www.openstreetmap.org/about')
]

# Insert the data sources into the table
conn.executemany('INSERT INTO DataSources VALUES (?, ?)', data_sources)

# Commit the changes and close the connection
conn.commit()
conn.close()
