bl_info = {
    "name": "MatDaz",
    "author": "xd43vild69-davidgomez",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbar > Object Adder",
    "description": "MatDaz",
    "warning": "",
    "doc_url": "",
    "category": "MatDaz",
}

import bpy

def ChangeMaterial(materialId):
#    bpy.ops.mesh.primitive_cube_add()     
    if materialId == 1:
        prefix = "1D.C" #ClayMaterial
    elif materialId == 2:
        prefix = "1D.M" #MuscleMaterial
    elif materialId == 3:
        prefix = "1D." #BaseMaterial
    elif materialId == 4:
        prefix = "1D_Z" #BaseMaterial

    #Select object here
    obj = bpy.context.selected_objects[0]
    obj.name = prefix + "Character"
    obj.data.name = prefix + "Character"
     
    if materialId != 4:
        sel = bpy.context.selected_objects[0]
        mat = bpy.data

        sel.material_slots[0].material = mat.materials.get(prefix + 'Torso')
        sel.material_slots[1].material = mat.materials.get(prefix + 'Face')
        sel.material_slots[2].material = mat.materials.get(prefix + 'Face') #lips
        sel.material_slots[4].material = mat.materials.get(prefix + 'Face') #ears
        sel.material_slots[5].material = mat.materials.get(prefix + 'Legs')
        sel.material_slots[8].material = mat.materials.get(prefix + 'Arms')
        sel.material_slots[11].material = mat.materials.get(prefix + 'Arms') #Fingernails
        sel.material_slots[15].material = mat.materials.get(prefix + 'Legs') #Toenails    


#This is the Main Panel (Parent of Panel A and B)
class MainPanel(bpy.types.Panel):

    bl_label = "PanelTexturesDaz"
    bl_idname = "VIEW_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TexturesDaz'
   
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2
       
        row = layout.row()
        row.label(text= "Select a Texture", icon= 'OBJECT_ORIGIN')
        row = layout.row()
        row.operator("wm.clay", icon= 'MESH_MONKEY', text= "Clay")
        row = layout.row()        
        row.operator("wm.muscle", icon= 'MESH_MONKEY', text= "Muscle")
        row = layout.row()        
        row.operator("wm.base", icon= 'MESH_MONKEY', text= "Base")
        row = layout.row()        
        row.operator("wm.zbrush", icon= 'MESH_MONKEY', text= "ZbrushBase")                        
        row = layout.row()        
        row = layout.row()


class WM_OT_Clay(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.clay"
    
    #text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        ChangeMaterial(1)
        return {'FINISHED'}

    
class WM_OT_Muscle(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.muscle"
    
    #text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        ChangeMaterial(2)
        return {'FINISHED'}


class WM_OT_Base(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.base"
    
    text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        ChangeMaterial(3)
        return {'FINISHED'}
        
class WM_OT_Zbrush(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.zbrush"
    
    text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        ChangeMaterial(4)
        return {'FINISHED'}
        
class WM_OT_Daz(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.myop"
   
    text = bpy.props.StringProperty(name= "Enter Name", default= "")
    scale = bpy.props.FloatVectorProperty(name= "Scale:", default= (1,1,1))
   
   
   
    def execute(self, context):
       
        t = self.text
        s = self.scale
       
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object
        obj.name = t
        obj.scale[0] = s[0]
        obj.scale[1] = s[1]
        obj.scale[2] = s[2]
       
        return {'FINISHED'}
   
    def invoke(self, context, event):
       
        return context.window_manager.invoke_props_dialog(self)        


    #Here we are Registering the Classes        
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(WM_OT_Clay)
    bpy.utils.register_class(WM_OT_Muscle)    
    bpy.utils.register_class(WM_OT_Zbrush)
    bpy.utils.register_class(WM_OT_Base)
    bpy.utils.register_class(WM_OT_Daz)        
   
   
 
    #Here we are UnRegistering the Classes    
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(WM_OT_Clay)
    bpy.utils.unregister_class(WM_OT_Muscle)    
    bpy.utils.unregister_class(WM_OT_Zbrush)    
    bpy.utils.unregister_class(WM_OT_Base)    
    bpy.utils.unregister_class(WM_OT_Daz)    
   
    #This is required in order for the script to run in the text editor    
if __name__ == "__main__":
    register()     