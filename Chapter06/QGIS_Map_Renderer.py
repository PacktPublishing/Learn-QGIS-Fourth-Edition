from PyQt5.QtGui import QImage, QPainter

from PyQt5.QtCore import QSize

# configure the output image

width = 800

height = 600

dpi = 92

img = QImage(QSize(width, height), QImage.Format_RGB32)

img.setDotsPerMeterX(dpi / 25.4 * 1000)

img.setDotsPerMeterY(dpi / 25.4 * 1000)

# get the map layers and extent

layers = [ layer for layer in iface.mapCanvas().layers() ]

extent = iface.mapCanvas().extent()

# configure map settings for export

mapSettings = QgsMapSettings()


mapSettings.setExtent(extent)

mapSettings.setOutputDpi(dpi)

mapSettings.setOutputSize(QSize(width, height))

mapSettings.setLayers(layers)

mapSettings.setFlags(QgsMapSettings.Antialiasing |
QgsMapSettings.UseAdvancedEffects |
QgsMapSettings.ForceVectorOutput | QgsMapSettings.DrawLabeling)

# configure and run painter

p = QPainter()

p.begin(img)

mapRenderer = QgsMapRendererCustomPainterJob(mapSettings, p)

mapRenderer.start()

mapRenderer.waitForFinished()

p.end()

# save the result

img.save("D:/temp/custom_export.png","png")