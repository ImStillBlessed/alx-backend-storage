-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: band_name and lifespan
-- (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database

LOAD DATA INFILE 'metal_bands.sql'
INTO TABLE bands
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(band_name, lifespan,);
