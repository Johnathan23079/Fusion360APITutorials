#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        defaultVal = "5.0 mm"
        newInput = ui.inputBox('enter a new input val','New Input val', defaultVal) 
        if newInput[0]:
            (defaultVal, isCanceled) = newInput
        if isCanceled:
            return
        unitsMgr = design.unitsManager
        try:
            NewInputReal = unitsMgr.evaluateExpression(newInput)
            isValid = True
        except:
            ui.messageBox('newInput' + 'is not a valid expression', 'Invalid Expression', adsk.core.MessageBoxButtonTypes.OKButtonType, adsk.core.MessageBoxIconTypes.CriticalIconType) 
            isValid = False 
        ui.messageBox('Input', + defaultVal + 'result' + NewInputReal)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
