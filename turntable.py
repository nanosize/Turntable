import bpy
from bpy.types import Panel,Operator

bl_info = {
   "name": "turntable",
   "author": "nao_3dcg",
   "version": (1, 0),
   "blender": (3, 6, 0),
   "location": "3D View",
   "description": "It automatically creates and animates the turntable.",
   "warning": "",
   "support": "TESTING",
   "wiki_url": "",
   "tracker_url": "",
   "category": "animation"
}

#UI set

class VIEW3D_PT_track_obj(bpy.types.Panel):
    
     #where to add the panel
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bl_category = "turntable"
    bl_label = "turntable"

    def draw(self, context):
        """difine the layout of panel"""
        row = self.layout.row()
        row.operator("add_set",text ="prepare")
#----------------------------------------------------------------

#make collection 'track' and link with collection
track_obj = bpy.data.collections.new('track_obj')
bpy.context.scene.collection.children.link(track_obj)


def add_set() : 
    #add circle
    bpy.ops.curve.primitive_bezier_circle_add(radius=5,location=(0,
    0, 1), scale=(1, 1, 1))
    circle = bpy.context.view_layer.objects.active
    circle.name = 'circle'
    
    #add empty
    bpy.ops.object.empty_add()
    empty = bpy.context.view_layer.objects.active
    empty.name = 'focus_target'

    #add camera
    #get data about add objects
    #change name
    bpy.ops.object.camera_add()
    cam = bpy.context.view_layer.objects.active
    cam.name = 'cam'
    #add object constraint follow_path
    #set target
    #animate
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    cam.constraints["Follow Path"].target = circle
    #bpy.ops.constraint.followpath_path_animate(constraint="Follow     Path", owner='OBJECT')
    #add object constraint track to

    bpy.ops.object.constraint_add(type='TRACK_TO')
    cam.constraints["Track To"].target = empty


    #link with track_collection
    #should wright exception handling

    track_obj.objects.link(circle)
    track_obj.objects.link(cam)
    track_obj.objects.link(empty)
    bpy.context.scene.collection.objects.unlink(circle)
    bpy.context.scene.collection.objects.unlink(cam)
    bpy.context.scene.collection.objects.unlink(empty)




def register():
    bpy.utils.register_class(VIEW3D_PT_track_obj)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_track_obj)
    
if __name__ == "__main__":
    register()