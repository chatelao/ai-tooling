CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  geom GEOMETRY(Point, 4326)
);

CREATE INDEX locations_geom_idx ON locations USING GIST (geom);
