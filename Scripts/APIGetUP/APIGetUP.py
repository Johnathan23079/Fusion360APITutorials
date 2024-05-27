import traceback
#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        retParam = design.userParameters.itemByName('Length')

        ui.messageBox(retParam.expression)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
