import bpy

collection = bpy.data.collections.new("ph_light")
bpy.context.scene.collection.children.link(collection)