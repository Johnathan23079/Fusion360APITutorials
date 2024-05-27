#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        # ui.messageBox('Hello script')
        # ui.messageBox('OKButtonType', 'OK Button', 0,4) #no icon, 1 question, 2 information, 3 warning, 4 critical
        OKButtonPress = ui.messageBox()
        if OKButtonPress == 0:
            ui.messageBox('OK Pressed')
            return
        ui.messageBox('Cancel Pressed')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
