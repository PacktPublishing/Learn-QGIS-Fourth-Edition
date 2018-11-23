from PyQt5.QtGui import QColor

rules = [['Civil','USE LIKE \'%Civil%\'','green'], ['Other','USE NOT LIKE \'%Civil%\'','red']]

symbol = QgsSymbol.defaultSymbol(v_layer.geometryType())

renderer = QgsRuleBasedRenderer(symbol)

root_rule = renderer.rootRule()

for label, expression, color_name in rules:

    rule = root_rule.children()[0].clone()

    rule.setLabel(label)

    rule.setFilterExpression(expression)

    rule.symbol().setColor(QColor(color_name))

    root_rule.appendChild(rule)

root_rule.removeChildAt(0)

v_layer.setRenderer(renderer)

v_layer.triggerRepaint()