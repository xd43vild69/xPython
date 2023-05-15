import bpy

def GetAllElements():
    # Get all elements in scene
    for ob in bpy.data.objects:
        print(ob.name)


def GetSelectedElements():
    selection_names = [obj.name for obj in bpy.context.selected_objects]        
    print (selection_names)


def getActiveObject():
    ob = bpy.context.active_object
    print(ob.name)

def SetMaterial():    
    activeObj = bpy.context.active_object        
    
    # Get global material
    mat = bpy.data.materials.get("G8FBaseMaterial")
    
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name="G8FBaseMaterial")
    
    if activeObj.data.materials:        
        activeObj.data.materials[0] = mat
    else:
        # no slots
        activeObj.data.materials.append(mat)
    

SetMaterial()

#SetMaterial()
    
#GetSelectedElements()

#GetAllElements()   