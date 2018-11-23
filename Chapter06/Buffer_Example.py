import processing
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsProcessingAlgorithm, QgsProcessing, QgsProcessingParameterFeatureSink,QgsProcessingParameterFeatureSource

class testAlg(QgsProcessingAlgorithm):
    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'

    def tr(self, text):
        return QCoreApplication.translate('testalg', text)

    def createInstance(self):
        return type(self)()

    def group(self):
        return self.tr('Test')

    def groupId(self):
        return 'test'

    def __init__(self):
        super().__init__()

    def initAlgorithm(self, config=None):
        
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT, 
                self.tr('Output'), 
                QgsProcessing.TypeVectorPoint ### changed
            )
        )

    def name(self):
        return 'testalg'

    def displayName(self):
        return self.tr('Test Algorithm')

    def processAlgorithm(self, parameters, context, feedback):

        output = processing.run("native:buffer", {
            'INPUT': parameters['INPUT'],
            'DISTANCE': 10,
            'SEGMENTS': 5,
            'END_CAP_STYLE': 0,
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'DISSOLVE': False,
            'OUTPUT': 'memory:' ## changed to memory
            
        }, context=context, feedback=feedback)['OUTPUT']
        
        ### new process
        output2 = processing.run("native:centroids", {
            'INPUT': output,
            'ALL_PARTS': False,
            'OUTPUT': parameters['OUTPUT']
            
        }, context=context, feedback=feedback)['OUTPUT']
        
        return {self.OUTPUT: output2} ### a different output (output2 is now returned) 