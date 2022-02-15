import json
from flask import Flask, request, render_template
from shapely.geometry import Point, shape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #performs initial GET
def flow():
    return render_template('form.html')

@app.route('/colleyesqjson', methods=['GET', 'POST']) #performs subsequent POST
def geolocate():
    if request.method == 'POST':
        with open('census_2010_100k_convexHulls.geojson') as file: #loads geoJSON data for parsing
            polygons = json.load(file)

        latCoor = float(request.form['lat'])
        lonCoor = float(request.form['lon'])
        point = Point(lonCoor, latCoor) #longitude, latitude
        urbanized = False

        for urbanArea in polygons['features']: #parses through each location with the geoJSON file
            area = shape(urbanArea['geometry']) #creates a polygon for the location from the associated geometry data
            if area.contains(point): #if the given latitude/longitude point is within the polygon, the point is in an urbanized area
                urbanized = True
        if urbanized:
            return "True"
        else:
            return "False"

if __name__ == '__main__':
    app.run(host='localhost', port=5000)