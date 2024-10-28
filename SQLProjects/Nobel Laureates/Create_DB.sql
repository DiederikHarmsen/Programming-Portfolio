-- DROP TABLES IF ALREADY EXISTS
DROP TABLE IF EXISTS Person; 

CREATE TABLE Person(
    Id INT,
    FirstName STRING,
    Surname STRING,
    Born DATETIME,
    Died DATETIME,
    BournCountry STRING,
    BrnCnt STRING,
    BornCity STRING,
    DiedCountry STRING,
    DdCnt STRING,
    DiedCity String,
    Gender STRING,
    Year DATETIME,
    Category String,
    Overall_Motivation String,
    Motivation String,
    Organization_Name String,
    Organization_City String,
    Organization_Country String,
    PRIMARY KEY (Id)
)


SELECT * INTO Person FROM OPENROWSET(SELECT *
FROM OPENROWSET(
    'Microsoft.ACE.OLEDB.12.0',
    'Excel 8.0;HDR=NO;Database=Nobel Laureates\nobel-prize-laureates.xlsx',
    'select * from [sheet1$]'))