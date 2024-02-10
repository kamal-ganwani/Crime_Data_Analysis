show databases;
use crimeanalysis;
select AREA_NAME from crime_data;
select * from crime_data;


SELECT * FROM crime_data
WHERE Crm_Cd_Desc = "BATTERY - SIMPLE ASSAULT";

SELECT DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location 
FROM crime_data
WHERE Vict_Sex = "M";

SELECT DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location 
FROM crime_data
WHERE Vict_Sex = "F";

SELECT DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location 
FROM crime_data
WHERE Vict_Sex = "M";

SELECT COUNT(*) AS total_count, DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location
FROM crime_data
WHERE Vict_Sex = 'M';

SELECT COUNT(*) AS total_count, DR_NO, AREA_NAME, Crm_Cd_Desc, Vict_Age, Vict_Sex, Premis_Desc, Location
FROM crime_data
WHERE Vict_Sex = 'F';

SELECT Location, AREA_NAME, Vict_Age, Vict_Sex
FROM crime_data
WHERE Vict_Age BETWEEN 18 AND 30;

SELECT Crm_Cd_Desc, COUNT(*) AS crime_count
FROM crime_data
GROUP BY Crm_Cd_Desc
ORDER BY Crm_Cd DESC

SELECT Crime_Description, COUNT(*) AS crime_count
FROM crime_data
GROUP BY Crime_Description
ORDER BY crime_count DESC
LIMIT 1;

SELECT 
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
    Crime_Count DESC;
    

SELECT 
    Vict_Sex,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    Vict_Sex
ORDER BY 
    Crime_Count DESC;
    
SELECT 
    Vict_Sex,
    AREA_NAME,
    Location,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    Vict_Sex
ORDER BY 
    Crime_Count DESC;
    
SELECT 
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
    DATE_OCC;
    


SELECT 
    YEAR(Date_Rptd) AS Year,
    MONTH(Date_Rptd) AS Month,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    YEAR(Date_Rptd), MONTH(Date_Rptd)
ORDER BY 
    Year, Month;
    
SELECT DISTINCT
    Crm_Cd,
    Crm_Cd_Desc
FROM 
    crime_data;

SELECT 
    Status,
    COUNT(*) AS Total_Count
FROM 
    crime_data
GROUP BY 
    Status;
    
SELECT 
    Status,
    Date_Rptd,
    DATE_OCC,
    AREA_NAME,
    Crm_Cd,
    Crm_Cd_Desc,
    Vict_Age,
    Vict_Sex,
    Premis_Desc,
    Location,
    COUNT(*) AS Total_Count
FROM 
    crime_data
GROUP BY 
    Status;    

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

SELECT 
    AREA_NAME,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    AREA_NAME
ORDER BY 
    Crime_Count DESC;
    
    
SELECT 
    AREA_NAME,
    COUNT(*) AS Crime_Count
FROM 
    crime_data
GROUP BY 
    AREA_NAME
ORDER BY 
    Crime_Count DESC;
    