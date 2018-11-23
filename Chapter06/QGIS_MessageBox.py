msgbox = QMessageBox(QMessageBox.Information, "How many layers?", "Number of features in layer: %s" % layer.featureCount(), QMessageBox.Ok)
msgbox.exec_()