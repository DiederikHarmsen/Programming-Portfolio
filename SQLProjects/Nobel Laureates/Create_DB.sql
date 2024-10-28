-- Drop table if exists
DROP TABLE IF EXISTS Person;

-- Create table
CREATE TABLE Person(
    Id INT,
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
    PRIMARY KEY (Id)
);

-- Load data into the table from CSV
LOAD DATA INFILE 'Nobel Laureates\nobel-prize-laureates.csv'
INTO TABLE Person
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
