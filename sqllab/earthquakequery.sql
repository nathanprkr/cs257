-- all earthquakes that have negative longitude
SELECT * FROM earthquakes WHERE longitude<0 ORDER BY longitude DESC;

-- all earthquakes that have positive longitude and are greater than 4 magnitude
SELECT * FROM earthquakes WHERE longitude>0
INTERSECT
SELECT * FROM earthquakes WHERE mag>6 ORDER BY longitude DESC;

-- all earthquakes deeper than 600 miles
SELECT * FROM earthquakes WHERE quakedepth>600 ORDER BY quakedepth DESC;
