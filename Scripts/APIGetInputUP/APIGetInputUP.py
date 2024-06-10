#Author-Johnathan Lee
#Description-Here we will learn how to take user input and place it inside a variable, we will also look at how to use the units manager to ensure different values other then cm can be used

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        defaultInput = "5.0 mm" #create a default value to display
        newInput = ui.inputBox('enter a new input val','New Input val', defaultInput) #input box within the UI, add default value inside
        if newInput[0]:                        #ensure the default value is used if nothing is used
            (defaultInput, isCanceled) = newInput
        if isCanceled:            #end the program if cancel button is pressed
            return
        unitsMgr = design.unitsManager #define fusion 360 built in unit manager to convert units
        try:
            NewInputReal = unitsMgr.evaluateExpression(newInput) # check if the units inputed are recognized 
            isValid = True #pass if true
        except:
            ui.messageBox('newInput' + 'is not a valid expression', 'Invalid Expression', adsk.core.MessageBoxButtonTypes.OKButtonType, adsk.core.MessageBoxIconTypes.CriticalIconType) 
            isValid = False 
        ui.messageBox('Input: ' + defaultInput + ' result: ' + NewInputReal) # input new values for user parameter and display in textbox
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
