import traceback
#Author- Johnathan Lee
#Description- Welcome to this tutorial, this sample program will teach you how to take an existing User Parameter and display it in a message box

#Before you try editing or using this code, make sure you have already set up a parameter in Fusion 360 with the following values
#Name - Length
#unit - mm
#expression - 500 mm
#Value - 500 mm
#Comments - blank
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get() #grab application 
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        retParam = design.userParameters.itemByName('Length')

        ui.messageBox(retParam.expression)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
