#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        document = adsk.core.Document.cast(app.activeDocument)

        path = design.parentDocument.dataFile.parentFolder
        ui.messageBox(str(path))
        ui.messageBox(path.name)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
