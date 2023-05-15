import bpy

def GetAllElements():
    # Get all elements in scene
    for ob in bpy.data.objects:
        print(ob.name)


def GetSelectedElements():
    selection_names = [obj.name for obj in bpy.context.selected_objects]
    print (selection_names)
    
GetSelectedElements()

GetAllElements()    
