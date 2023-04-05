# SQL Data Sources Table Creator

This Python script uses SQL to create a table with two columns: "DataSource" and "URL", and adds a list of data sources and their URLs to the table. This can be useful for keeping track of data sources and their corresponding URLs, and for quickly querying the table to find specific data sources.

## Requirements

To run this script, you'll need the following:

-   Python 3.x
-   SQLite 3.x (or another SQL database if you modify the script)

## Usage

1.  Clone this repository or download the `sql_data_sources.py` file.
2.  Open the `sql_data_sources.py` file in a text editor.
3.  Modify the placeholders for the database name, username, and password with your own values if necessary.
4.  Modify the `data_sources` list to add or remove data sources and their corresponding URLs.
5.  Save the changes to the `sql_data_sources.py` file.
6.  Open a terminal or command prompt.
7.  Navigate to the directory where the `sql_data_sources.py` file is located.
8.  Run the script using the command `python sql_data_sources.py`.
9.  The script will create a table called "DataSources" with two columns ("DataSource" and "URL"), and insert the data sources and URLs from the `data_sources` list into the table.
10.  You can now use SQL to query the "DataSources" table to find specific data sources.
