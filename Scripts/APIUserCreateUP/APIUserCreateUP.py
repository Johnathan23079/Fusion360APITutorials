#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        defaultInput = 'diameter'
        defaultInputNum =  '5 mm'
        newInputName = ui.inputBox('Enter a new parameter name', 'New Parameter', defaultInput)
        newInputValue = ui.inputBox('Enter a new parameter value', 'New Parameter', defaultInputNum)

        unitsMgr = design.unitsManager
        realInputNumber = unitsMgr.evaluateExpression(newInputValue[0], unitsMgr.defaultLengthUnits)

        realValueInput = adsk.core.ValueInput.createByReal(realInputNumber)

        design.userParameters.add(newInputName[0], realValueInput, unitsMgr.defaultLengthUnits, '')



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
