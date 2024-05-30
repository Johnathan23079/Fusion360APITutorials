#Author-JOhnathan Lee
#Description-This code is exactly the same as the first but it assumes you are already in the sketch window and it will apply the sketch to whatever plane you are working on
#the old code is commented out just for reference 
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent
        # sketches = rootComp.sketches

        sketch = adsk.fusion.Sketch.cast(app.activeEditObject)
        #this is the new line of code which casts the sketch to the active edit object which is what you are currently working on
        #the sketch is then created using the plane the user is already on
        #try running it on multiple different planes


        #sketch = sketches.add(rootComp.xYConstructionPlane)
        # sketchLines = sketch.sketchCurves.sketchLines

        sketchLines = sketch.sketchCurves.sketchLines
        
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5, 5, 0)

        sketchLines.addCenterPointRectangle(startPoint, endPoint)
        sketchLines.addByTwoPoints(startPoint, endPoint)


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
