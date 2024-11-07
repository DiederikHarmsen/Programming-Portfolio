-- Drop table if exists

-- DROP TABLE IF EXISTS Person;

CREATE TABLE Person(
    PersonId INT,
    FirstName VARCHAR(255),
    Surname VARCHAR(255),
    Born DATETIME,
    Died DATETIME,
    BornCountry VARCHAR(255),
    BrnCnt VARCHAR(255),
    BornCity VARCHAR(255),
    DiedCountry VARCHAR(255),
    DdCnt VARCHAR(255),
    DiedCity VARCHAR(255),
    Gender VARCHAR(255),
    Year INT,
    Category VARCHAR(255),
    Overall_Motivation VARCHAR(255),
    Motivation VARCHAR(255),
    Organization_Name VARCHAR(255),
    Organization_City VARCHAR(255),
    Organization_Country VARCHAR(255),
    PRIMARY KEY (PersonId)
)


-- Load data from CSV file
LOAD DATA INFILE 'C:/path/to/your/csvfile.csv'
INTO TABLE Person
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;