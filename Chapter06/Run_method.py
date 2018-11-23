def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # clear the combo box
        self.dlg.layerCombo.clear()
        layers=QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                 self.dlg.layerCombo.addItem( layer.name(), layer )
        result = self.dlg.exec_()