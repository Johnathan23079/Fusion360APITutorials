#Author-Johnathan Lee
#Description-This is a tutorial on how to create a User paramenter inside a fusion 360 script

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get() #These 3 lines of code will be present in most examples refer to the sample code for information
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        # Create a user parameter
        pName = 'Width' #name
        pUnit = 'mm'# unit
        pExpression  = 5.0/10 #expression is always in cm natively dividing by 10 puts it into mmm
        pExpressionReal = adsk.core.ValueInput.createByReal(pExpression) #creates the new parameter according to the variables

        design.userParameters.add(pName, pExpressionReal, pUnit, "") #print the output

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
