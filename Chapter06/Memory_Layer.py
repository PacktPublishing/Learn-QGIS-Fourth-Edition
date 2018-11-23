from qgis.core import QgsProject
mem_layer = QgsVectorLayer("Polygon?crs=epsg:4326&field=MYNUM:integer&field=MYTXT:string", "temp_layer", "memory")

if not mem_layer.isValid():

    raise Exception("Failed to create memory layer")

mem_layer_provider = mem_layer.dataProvider()

my_polygon = QgsFeature()

my_polygon.setGeometry(
  QgsGeometry.fromRect(QgsRectangle(16,48,17,49)))

my_polygon.setAttributes([10,"hello world"])
mem_layer_provider.addFeatures([my_polygon])

QgsProject.instance().addMapLayer(mem_layer)