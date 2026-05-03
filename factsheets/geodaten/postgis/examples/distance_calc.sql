SELECT
    l1.name AS city1,
    l2.name AS city2,
    ST_Distance(l1.geom::geography, l2.geom::geography) / 1000 AS distance_km
FROM locations l1, locations l2
WHERE l1.name = 'Berlin' AND l2.name = 'Munich';
