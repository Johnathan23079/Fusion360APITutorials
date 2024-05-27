#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        # Create a user parameter
        pName = 'Width'
        pUnit = 'mm'
        pExpression  = 5.0/10
        pExpressionReal = adsk.core.ValueInput.createByReal(pExpression)

        design.userParameters.add(pName, pExpressionReal, pUnit, "")

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
