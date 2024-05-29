#Author-Johnathan Lee
#Description-Here we will make a script to be able to create a user parameter in fusion based on user input

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        defaultInput = 'diameter'       #default values
        defaultInputNum =  '5 mm'
        newInputName = ui.inputBox('Enter a new parameter name', 'New Parameter', defaultInput)    #input box name
        newInputValue = ui.inputBox('Enter a new parameter value', 'New Parameter', defaultInputNum) # input box value

        unitsMgr = design.unitsManager #begin the units manager
        realInputNumber = unitsMgr.evaluateExpression(newInputValue[0], unitsMgr.defaultLengthUnits)# evaluate the expression in the input value and set it to default units wiht unit manager 
                                                        #[] are used because it is 5 mm and 5 is in the [0[ slot this example only takes mm
                                                        # a second input could be used for units if you want variability
        realValueInput = adsk.core.ValueInput.createByReal(realInputNumber) #assign this value to the real input value

        design.userParameters.add(newInputName[0], realValueInput, unitsMgr.defaultLengthUnits, '')#create the parameter using the values



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
