-- Find all locations within 500km of Berlin
SELECT name
FROM locations
WHERE ST_DWithin(
    geom::geography,
    ST_GeogFromText('POINT(13.4050 52.5200)'),
    500000
) AND name != 'Berlin';
