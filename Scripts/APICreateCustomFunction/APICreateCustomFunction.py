#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()
ui  = app.userInterface

def customFunction(newUserString):
    ui.messageBox("inside custom function")
    ui.messageBox(newUserString)
    editUserString = newUserString + " returned"
    return '{}' .format(editUserString)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Main function')
        passedValue = customFunction("User string")
        ui.messageBox(passedValue)
        ui.messageBox('Main function end')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
