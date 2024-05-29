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
        ui  = app.userInterface #start user interface
        design = adsk.fusion.Design.cast(app.activeProduct) #create a design variable that is assigned to the active product which is the file you are currently working in
        retParam = design.userParameters.itemByName('Length') #use the userParameters.itemByName to find the parameter called Length and place this parameter in retparam

        ui.messageBox(retParam.expression)# call the parameter and return the expression it can be replaced with name, unit, value and comment as well

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
