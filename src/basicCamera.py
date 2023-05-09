import bpy
 #
camera_data = bpy.data.cameras.new(name='camera_main')
camera_object = bpy.data.objects.new('camera_main', camera_data)
bpy.context.scene.collection.objects.link(camera_object)