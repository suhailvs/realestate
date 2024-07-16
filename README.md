# User Homes

To generate data goto : <https://www.google.com/maps/about/mymaps/> and draw polygons. 
Then `Export data` -> `CSV`

![screeshot1][logo1]


[logo1]: https://raw.github.com/suhailvs/realestate/main/exportdata.jpeg


<https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/>
https://www.paulox.net/2020/12/08/maps-with-django-part-1-geodjango-spatialite-and-leaflet/

# Download

## download osm.pdf files

    https://app.protomaps.com/

## convert pbf file to sqlite db

https://github.com/AmericanRedCross/workflows/blob/master/converting_pbf_into_spatialite.md

    ogr2ogr -f "SQLite" -dsco SPATIALITE=YES name_of_new_file.db name_of_extracted_file.pbf



# server deployment

### installing gdal

    $ sudo apt install gdal-bin
    $ sudo apt install postgis

