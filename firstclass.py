from geojson import Polygon, Point, MultiPoint, MultiPolygon, LineString, MultiLineString
from pathlib import Path
import csv
import json


class Converter:
    def convert(self, path):
        suffix = Path(path).suffix  # Получение расширения файла
        match suffix:
            case '.csv':
                return self.fromCSV(path)
            # case '.json':
            #     self.fromJSON(path)
            # case '.xml':
            #     self.convert1(path)
            # case '.kml':
            #     self.convert1(path)
            case _:
                print('Неверный формат файла')

    def fromCSV(self, path):  # +- готово
        Points = []
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                point = Point((float(row[0]), float(row[1])))
                Points.append(point)
        return Points

    # def fromJSON(self, path): # не доделано
    #     input_file = json.load(open(path, "r", encoding="utf-8"))
    #     geojs = {
    #         "type": "FeatureCollection",
    #         "features": [
    #             {
    #                 "type": "Feature",
    #                 "geometry": {
    #                     "type": "LineString",
    #                     "coordinates": d["geojson"]["coordinates"],
    #                 },
    #                 "properties": d,
    #             } for d in input_file
    #         ]
    #     }
    #     output_file = open("geodata.json", "w", encoding="utf-8")
    #     json.dump(geojs, output_file)
    #     output_file.close()
    # def convert3(self, extension):
    #     pass
    # def convert4(self, extension):
    #     pass
