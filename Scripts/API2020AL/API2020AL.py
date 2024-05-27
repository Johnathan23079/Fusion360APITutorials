#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent

        if app.activeEditObject.objectType != adsk.fusion.Sketch.classType():
            ui.messageBox('Please select a sketch')
            return
        
        sketch = adsk.fusion.Sketch.cast(app.activeEditObject)
        

        sketchLines = sketch.sketchCurves.sketchLines
        sketchArcs = sketch.sketchCurves.sketchArcs
        sketchCircles = sketch.sketchCurves.sketchCircles

        PosArray = [0,1,2,3,4,5]
        xArray = [0, 0.225, 0.55, 0.55, 0.31, 0.31, 0.85]
        yArray = [0.31, 0.31, 0.635, 0.85, 0.85, 1.0, 1.0]

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(xArray[i], yArray[i], 0)
            endPoint = adsk.core.Point3D.create(xArray[i+1], yArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)
        arcStart = adsk.core.Point3D.create(0.85, 1.0, 0)
        arcCenter = adsk.core.Point3D.create(0.85, 0.85, 0)
        sketchArcs.addByCenterStartSweep(arcCenter, arcStart, -1.5708)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(yArray[i], xArray[i], 0)
            endPoint = adsk.core.Point3D.create(yArray[i+1], xArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)
        for i in PosArray:
            startPoint = adsk.core.Point3D.create(xArray[i], -yArray[i], 0)
            endPoint = adsk.core.Point3D.create(xArray[i+1], -yArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)
        arcStart = adsk.core.Point3D.create(1.0, -0.85, 0)
        arcCenter = adsk.core.Point3D.create(0.85, -0.85, 0)
        sketchArcs.addByCenterStartSweep(arcCenter, arcStart, -1.5708)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(yArray[i], -xArray[i], 0)
            endPoint = adsk.core.Point3D.create(yArray[i+1], -xArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(-xArray[i], -yArray[i], 0)
            endPoint = adsk.core.Point3D.create(-xArray[i+1], -yArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)
        arcStart = adsk.core.Point3D.create(-0.85, -1.0, 0)
        arcCenter = adsk.core.Point3D.create(-0.85, -0.85, 0)
        sketchArcs.addByCenterStartSweep(arcCenter, arcStart, -1.5708)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(-yArray[i], -xArray[i], 0)
            endPoint = adsk.core.Point3D.create(-yArray[i+1], -xArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(-xArray[i], yArray[i], 0)
            endPoint = adsk.core.Point3D.create(-xArray[i+1], yArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)
        arcStart = adsk.core.Point3D.create(-1.0, 0.85, 0)
        arcCenter = adsk.core.Point3D.create(-0.85, 0.85, 0)
        sketchArcs.addByCenterStartSweep(arcCenter, arcStart, -1.5708)

        for i in PosArray:
            startPoint = adsk.core.Point3D.create(-yArray[i], xArray[i], 0)
            endPoint = adsk.core.Point3D.create(-yArray[i+1], xArray[i+1], 0)
            sketchLines.addByTwoPoints(startPoint, endPoint)

        sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0,0,0), 0.25)









    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
