#Author-Johnathan Lee
#Description- Here I will show you how to make a simple sketch of a line in Fusion 360 API as well as a rectangle, 
#To make sketches in Fusion 360 you first need to make your sketch in a two dimensional plane and make sure all the coordinates are marked as these are where your points will be placed 

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        #cast to the active product
        rootComp = design.rootComponent #the root component is the default component inside of every fusion 360 file it is at the top of the hierarchy
        sketches = rootComp.sketches #grabs the sketches header and assigns it to the "sketches" variable could also be written design.rootComponent.sketches
                                    # this is done to make calling the same variables easier to read and shorter
        sketch = sketches.add(rootComp.xYConstructionPlane)# create a sketch on the xy plane of the project
        sketchLines = sketch.sketchCurves.sketchLines #sketchCurves covers the various types of lines you can make and sketchLines is used for straight lines. this is assigned to the sketchLines variable

        #creating and connecting points is the basis of creating sketches, points are plotted on the plane and then connected with various fusion functions
        startPoint = adsk.core.Point3D.create(0, 0, 0)# This creates the first point called startPoint at (0,0) which is the middle of the workspace
        endPoint = adsk.core.Point3D.create(5, 5, 0)# create and end point at the points (5,5) the 3rd value denotes the z values but we are only working in 2d for now

        sketchLines.addCenterPointRectangle(startPoint, endPoint)# uses the center point rectangle to create the center at 0,0 and outside corner at 5,5
        #It is important to know what values are needed for each function, these two happen to only need 2 points
        sketchLines.addByTwoPoints(startPoint, endPoint)
        #create a line between the two points


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
