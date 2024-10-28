/*
Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points.
*/

SELECT 
 races.race_name,
 circuits.circuit_location,
 drivers.driver_name,
 results.grid,
 results.position,
 results.points,
 results.fastest_lap,
 results.race_time as time,
 races.race_year as year,
 constructors.team as team_name,
 races.race_date as date

 FROM races
 JOIN circuits ON races.circuit_id = circuits.circuit_id
 JOIN results ON races.race_id = results.race_id
 JOIN drivers ON results.driver_id = drivers.driver_id
 JOIN constructors ON results.constructor_id = constructors.constructor_id
 WHERE races.race_year = 2020
 ORDER BY results.points DESC;