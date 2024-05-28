#Author-Johnathan Lee
#Description-Starter Code

import adsk.core, adsk.fusion, adsk.cam, traceback

# adsk = Autodesk Core Package (Core, Fusion, CAM)
# traceback = Python Standard Library (traceback)

def run(context): # Function that runs on startup of script
    ui = None  # User Interface
    try: # Try to run the following code block, most code will be placed here
        app = adsk.core.Application.get()   # Get the application and assign to the "app" variable 

        ui  = app.userInterface # Get the user interface

        ui.messageBox('Hello script') # Display a message box with the text 'Hello script' that pops up on run

    except: # If an error occurs, run the following code block usually to display the error message
        if ui:

            ui.messageBox('Failed:\n{}'.format(traceback.format_exc())) # Display a message box with the error message
