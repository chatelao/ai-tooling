-- Simple Lua config for osm2pgsql flex output
local tables = {}

tables.places = osm2pgsql.define_table({
    name = 'places',
    columns = {
        { column = 'name', type = 'text' },
        { column = 'type', type = 'text' },
        { column = 'geom', type = 'point' },
    }
})

function osm2pgsql.process_node(object)
    if object.tags.place then
        tables.places:insert({
            name = object.tags.name,
            type = object.tags.place,
            geom = object:as_point()
        })
    end
end
