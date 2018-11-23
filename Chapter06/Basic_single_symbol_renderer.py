from PyQt5.QtGui import QColor

symbol = QgsMarkerSymbol()

symbol.symbolLayer(0).setSize(10)

symbol.symbolLayer(0).setColor(QColor('#ffff00'))

v_layer.renderer().setSymbol(symbol)

v_layer.triggerRepaint()