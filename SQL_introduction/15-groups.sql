-- List the number of records with the same score in the second_table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score