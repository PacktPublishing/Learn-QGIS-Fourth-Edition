from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis.core import *
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .my_first_plugin_dialog import MyFirstPluginDialog
import os.path