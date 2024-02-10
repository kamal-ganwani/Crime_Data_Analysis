#pip install matplotlib
#pip install seaborn

import seaborn as sns
import matplotlib as mtpltlb
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port='3306',
    database="crimeanalysis"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Query to display information about databases
show_databases_query = "SHOW DATABASES"

# Execute the query
cursor.execute(show_databases_query)

# Fetch all rows
databases = cursor.fetchall()

# Display database information
print("Databases:")
for database in databases:
    print(database[0])

# Choose a database to work with (replace 'yourdatabase' with the desired database name)
database_name = 'crimeanalysis'
conn.database = database_name

# Query to display information about tables in the selected database
show_tables_query = "SHOW TABLES"

# Execute the query
cursor.execute(show_tables_query)

# Fetch all rows
tables = cursor.fetchall()

# Display table information
print("\nTables in", database_name, "database:")
for table in tables:
    print(table[0])


# Query to select all rows and columns from the "crime_analysis" table
select_query = "SELECT * FROM crime_data"

# Execute the query
cursor.execute(select_query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


# Query to select all rows and columns from the "crime_analysis" table
select_query = "SELECT AREA_NAME FROM crime_data"

# Execute the query
cursor.execute(select_query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Query to select all rows and columns from the "crime_analysis" table
query = "SELECT * FROM crime_data WHERE Crm_Cd_Desc = 'BATTERY - SIMPLE ASSAULT';"


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Query to select all rows and columns from the "crime_analysis" table
query = "SELECT COUNT(*) AS total_count, DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location FROM crime_data WHERE Vict_Sex = 'F';"


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


# Query to select all rows and columns from the "crime_analysis" table
query = "SELECT COUNT(*) AS total_count, DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location FROM crime_data WHERE Vict_Sex = 'M';"


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = "SELECT DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location FROM crime_data WHERE Vict_Sex = 'M';"


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = "SELECT Crm_Cd_Desc, COUNT(*) AS crime_count FROM crime_data GROUP BY Crm_Cd_Desc ORDER BY Crm_Cd DESC;"


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""SELECT 
    CASE 
        WHEN Vict_Age BETWEEN 0 AND 18 THEN '0-18'
        WHEN Vict_Age BETWEEN 19 AND 30 THEN '19-30'
        WHEN Vict_Age BETWEEN 31 AND 40 THEN '31-40'
        WHEN Vict_Age BETWEEN 41 AND 50 THEN '41-50'
        WHEN Vict_Age BETWEEN 51 AND 60 THEN '51-60'
        ELSE 'Above 60'
    END AS Age_Group,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    Age_Group
ORDER BY 
    Crime_Count DESC;""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""SELECT 
    Vict_Sex,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    Vict_Sex
ORDER BY 
    Crime_Count DESC;
""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)



cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""SELECT 
    Vict_Sex,
    AREA_NAME,
    Location,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    Vict_Sex
ORDER BY 
    Crime_Count DESC;""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""SELECT 
    Date_Rptd,
    DATE_OCC,
    Vict_Sex,
    AREA_NAME,
    Location,
    COUNT(*) AS Crime_Count,
    CASE 
        WHEN COUNT(*) > 1 THEN 'Same Date'
        ELSE 'Unique Date'
    END AS Date_Status
FROM 
    crime_data
GROUP BY 
    Date_Rptd
ORDER BY 
    DATE_OCC;""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""SELECT DISTINCT
    Crm_Cd,
    Crm_Cd_Desc
FROM 
    crime_data;
""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""
SELECT 
    Status,
    COUNT(*) AS Total_Count
FROM 
    crime_data
GROUP BY 
    Status;
""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


cursor = conn.cursor()

# Query to select all rows and columns from the "crime_analysis" table
query = ("""
SELECT 
    Vict_Age AS Victim_Age,
    Vict_Sex AS Victim_Gender,
    COUNT(*) AS Victim_Count
FROM 
    crime_data
GROUP BY 
    Vict_Age, Vict_Sex
ORDER BY 
    Vict_Age, Vict_Sex;

""")


# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)


query = """
SELECT 
    LAT,
    LON
FROM 
    crime_data;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract latitude and longitude data
latitude = [row[0] for row in rows]
longitude = [row[1] for row in rows]

# Plot crime locations on a map
plt.figure(figsize=(10, 8))
plt.scatter(longitude, latitude, color='red', alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Data: Spatial Analysis')
plt.grid(True)
plt.show()

cursor = conn.cursor()

# Execute the SQL query to retrieve data
query = """
SELECT 
    LAT,
    LON
FROM 
    crime_data;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract latitude and longitude data
latitude = [row[0] for row in rows]
longitude = [row[1] for row in rows]

# Plot crime hotspots on a map
plt.figure(figsize=(10, 8))
plt.scatter(longitude, latitude, color='red', alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Hotspots Map')
plt.grid(True)
plt.show()


cursor = conn.cursor()

# Execute the SQL query to retrieve data
query = """
SELECT 
    Premis_Desc,
    COUNT(*) AS Premis_Count
FROM 
    crime_data
GROUP BY 
    Premis_Desc
ORDER BY 
    Premis_Count DESC;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract premises descriptions and counts
premises = [row[0] for row in rows]
counts = [row[1] for row in rows]

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.barh(premises, counts, color='skyblue')
plt.xlabel('Number of Crimes')
plt.ylabel('Premises Description')
plt.title('Common Premises for Crime Occurrence')
plt.gca().invert_yaxis()  # Invert y-axis to display premises with highest counts at the top
plt.show()



cursor = conn.cursor()

# Execute the SQL query to retrieve data
query = """
SELECT 
    Vict_Age AS Victim_Age,
    Vict_Sex AS Victim_Sex,
    COUNT(*) AS Victim_Count
FROM 
    crime_data
GROUP BY 
    Vict_Age, Vict_Sex
ORDER BY 
    Vict_Age, Vict_Sex;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract data for plotting
victim_ages = []
victim_sexes = []
victim_counts = []

for row in rows:
    victim_ages.append(row[0])
    victim_sexes.append(row[1])
    victim_counts.append(row[2])

# Plotting
plt.figure(figsize=(12, 6))
plt.scatter(victim_ages, victim_sexes, s=victim_counts, alpha=0.5)
plt.xlabel('Victim Age')
plt.ylabel('Victim Sex')
plt.title('Distribution of Victim Age and Sex')
plt.grid(True)
plt.show()


# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the SQL query to retrieve data
query = """
SELECT 
    LAT,
    LON
FROM 
    crime_data;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract latitude and longitude data
LAT = [row[0] for row in rows]
LON = [row[1] for row in rows]

# Plotting
plt.figure(figsize=(10, 8))
sns.kdeplot(LAT, cmap='inferno', shade=True, shade_lowest=False)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Crime Hotspot Heatmap')
plt.show()



# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the SQL query to retrieve data
query = """
SELECT 
    LAT,
    LON
FROM 
    crime_data;
"""
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Extract latitude and longitude data
LAT = [row[0] for row in rows]
LON = [row[1] for row in rows]

# Plotting
plt.figure(figsize=(10, 8))
sns.kdeplot(LON, cmap='inferno', shade=True, shade_lowest=False)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Crime Hotspot Heatmap')
plt.show()








# Close the connection
conn.close()

