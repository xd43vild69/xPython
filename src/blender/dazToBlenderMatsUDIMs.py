import bpy
bl_info = {
    "name": "MatDazUDIM",
    "author": "xd43vild69-davidgomez",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbar > Object Adder",
    "description": "MatDazUDIM",
    "warning": "",
    "doc_url": "",
    "category": "MatDazUDIM",
}


def SetMaterial(materialId):

    if materialId == 1:
        materialName = "G8FBaseMaterial"  # BaseMaterial
    elif materialId == 2:
        materialName = "G8FMuscleMaterial"  # MuscleMaterial
    elif materialId == 3:
        materialName = "G8FClayMaterial"  # ClayMaterial
    elif materialId == 4:
        materialName = "G8FZbrushedMaterial"  # BaseMaterial

    activeObj = bpy.context.active_object

    # Get global material
    mat = bpy.data.materials.get(materialName)

    if mat is None:
        # create material
        mat = bpy.data.materials.new(name=materialName)

    if activeObj.data.materials:
        activeObj.data.materials[0] = mat
    else:
        # no slots
        activeObj.data.materials.append(mat)


# This is the Main Panel (Parent of Panel A and B)
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
        row.label(text="Select a Texture", icon='OBJECT_ORIGIN')
        row = layout.row()
        row.operator("wm.base", icon='MESH_MONKEY', text="Base")
        row = layout.row()
        row.operator("wm.muscle", icon='MESH_MONKEY', text="Muscle")
        row = layout.row()
        row.operator("wm.clay", icon='MESH_MONKEY', text="Clay")        
        row = layout.row()
        row.operator("wm.zbrush", icon='MESH_MONKEY', text="ZbrushBase")
        row = layout.row()
        row = layout.row()

class WM_OT_Base(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.base"

    text = bpy.props.StringProperty(name="Enter Option", default="")

    def execute(self, context):
        SetMaterial(1)
        return {'FINISHED'}

class WM_OT_Muscle(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.muscle"

    # text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        SetMaterial(2)
        return {'FINISHED'}

class WM_OT_Clay(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.clay"

    # text = bpy.props.StringProperty(name= "Enter Option", default= "")

    def execute(self, context):
        SetMaterial(3)
        return {'FINISHED'}

class WM_OT_Zbrush(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.zbrush"

    text = bpy.props.StringProperty(name="Enter Option", default="")

    def execute(self, context):
        SetMaterial(4)
        return {'FINISHED'}


class WM_OT_Daz(bpy.types.Operator):
    """Open the Add Cube Dialog box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.myop"

    text = bpy.props.StringProperty(name="Enter Name", default="")
    scale = bpy.props.FloatVectorProperty(name="Scale:", default=(1, 1, 1))

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

    # Here we are Registering the Classes


def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(WM_OT_Clay)
    bpy.utils.register_class(WM_OT_Muscle)
    bpy.utils.register_class(WM_OT_Zbrush)
    bpy.utils.register_class(WM_OT_Base)
    bpy.utils.register_class(WM_OT_Daz)

    # Here we are UnRegistering the Classes


def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(WM_OT_Clay)
    bpy.utils.unregister_class(WM_OT_Muscle)
    bpy.utils.unregister_class(WM_OT_Zbrush)
    bpy.utils.unregister_class(WM_OT_Base)
    bpy.utils.unregister_class(WM_OT_Daz)


    # This is required in order for the script to run in the text editor
if __name__ == "__main__":
    register()
