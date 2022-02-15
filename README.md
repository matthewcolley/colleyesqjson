Author: Matthew Colley
Date: February 10th, 2021
Python Version: 3.10.2

//Overview
This project is designed to accept latitude/longitude parameters and determine whether or not the given point is located with an urbanized area, population >= 100k, in relation to the attached geoJSON file. Flask and Shapely were the two primary resources used to complete this project. Flask provided a means of hosting the API locally as well as facilitating a simpler user interface in the form of the form.html file. Shapely is a package available to python that allows for the manipulation of geoJSON data, specifically though creating polygon objects from the geoJSON geometry coordinates. In addition to these polygons, a singular latitude/longitude point can be created and then subsequently compared to polygon to determine whether or not the point was located within its area. Through the use of HTTP 'GET' request, the form.html page can be displayed through browser, where the API accepts a follow up HTTP 'POST' request containing latitude/longitude parameters from the user. From there, the point is parsed through the polygons in the geoJSON file to determine whether or not it is located within an urbanized area. Once complete, a 'True' or 'False' is displayed through browser.

//How to use
From the directory of the colleyesqjson folder, the program can be run by the following:
    py colleyesqjson.py
From there, navigate to http://localhost:5000/ to interact with the API

Since this project requires Flask and Shapely to operate, the following packages will need to be installed:
pip install Flask
pip install Shapely-1.8.0-cp310-cp310-win_amd64.whl

*the whl file for Shapely 1.8.0 has been included in this folder