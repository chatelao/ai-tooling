INSERT INTO locations (name, geom) VALUES
  ('Berlin', ST_GeomFromText('POINT(13.4050 52.5200)', 4326)),
  ('Munich', ST_GeomFromText('POINT(11.5819 48.1351)', 4326)),
  ('Hamburg', ST_GeomFromText('POINT(9.9937 53.5511)', 4326));
