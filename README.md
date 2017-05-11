# WebMap

Creates a world map of volcano locations in the United States. The data file is a comma separated CSV. 

Map Features:
* Layer Control Panel

* Countries are shaded according to population size (Using 2005 census data):
Green - Less than or equal to 10 million
Orange - less than or equal to 20 million
Red - Greater than 20 million

* Volcano location markers are shaded according to elevation:

The color function takes one argument, 'elev', from the Volcanoes-USA.txt file.
Minimum - lowest elevation
Step - highest elevation - lowest elevation
