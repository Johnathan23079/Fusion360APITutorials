#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
       
        draftName = 'draftAngle'
        draftAngle =  2
        thicknessVal =  2
        thicknessName = 'WallThickness'
        internalWallthickness =  thicknessVal * 0.6
        internalWallName = 'InternalWallThickness'

        unitsMgr = design.unitsManager

        draftAngleReal = unitsMgr.evaluateExpression(str(draftAngle), 'deg')
        thicknessValReal = unitsMgr.evaluateExpression(str(thicknessVal), 'mm')
        internalWallReal = unitsMgr.evaluateExpression(str(internalWallthickness), 'mm')

        realDraft = adsk.core.ValueInput.createByReal(draftAngleReal)
        realThickness = adsk.core.ValueInput.createByReal(thicknessValReal)
        realWallT = adsk.core.ValueInput.createByReal(internalWallReal)
    


        design.userParameters.add(draftName, realDraft, 'deg', '')
        design.userParameters.add(thicknessName, realThickness,'mm', '')
        design.userParameters.add(internalWallName, realWallT, 'mm', '')
     






    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
