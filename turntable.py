bl_info = {
   "name": "turntable",
   "author": "nao_3dcg",
   "version": (0, 0, 0),
   "blender": (3, 0, 0),
   "location": "View3D > turntable",
   "description": "It automatically creates and animates the turntable.",
   "warning": "TThis add-on is a beta version, so please install at your own risk!",
   "wiki_url": "",
   "tracker_url": "",
   "category": "animation"
}



import bpy
from bpy.types import Panel

#UI set
class VIEW3D_PT_track_obj(bpy.types.Panel):

     #where to add the panel
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bl_category = "Turntable"
    bl_label = "Turntable"
    def draw(self, context):
        layout = self.layout
        scene = context.scene


        # Frame
        layout.label(text="Frame:")
        row = layout.row()
        row.prop(scene, "frame_end")

        layout.separator()
        
        #create button
        layout.label(text="Create Camera:",icon="CAMERA_DATA")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.create", text="Create")
        




class  OBJECT_TO_create(bpy.types.Operator):
    bl_idname = "object.create"
    bl_label = "Tool Name"
    
    def execute(self, context):
        
        global tr_obj
        tr_obj = bpy.data.collections.new('track_obj')
        bpy.data.collections['track_obj'].color_tag = 'COLOR_04'
        bpy.context.scene.collection.children.link(tr_obj)
        
        #add circle
        bpy.ops.curve.primitive_bezier_circle_add(radius=5,location=(0,
        0, 1), scale=(1, 1, 1))
        global circle
        circle = bpy.context.view_layer.objects.active
        circle.name = 'circle'

        #add empty
        bpy.ops.object.empty_add() 
        global empty 
        empty = bpy.context.view_layer.objects.active
        empty.name = 'focus_target'

        #add camera
        #get data about add objects
        #change name      
        global cam
        global scn
        
        bpy.ops.object.camera_add()
        cam = bpy.context.view_layer.objects.active
        cam.name = 'cam'
        
        #add object constraint follow_path
        #set target
        #animate
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        cam.constraints["Follow Path"].target = circle
        
        #set start keyflame
        cam.constraints["Follow Path"].offset = 0
        cam.constraints["Follow Path"].keyframe_insert("offset",frame=1)
        #set last keyflame
        cam.constraints["Follow Path"].offset = 100
        cam.constraints["Follow Path"].keyframe_insert("offset",frame= frm)
        #set framerange
        scn = bpy.context.scene
        scn.frame_end = frm
        
        #add object constraint track to
        bpy.ops.object.constraint_add(type='TRACK_TO')
        cam.constraints["Track To"].target = empty 
        
        #link with track_collection
        #should wright exception handling
        tr_obj.objects.link(circle)
        tr_obj.objects.link(cam)
        tr_obj.objects.link(empty)
        bpy.context.scene.collection.objects.unlink(circle)
        bpy.context.scene.collection.objects.unlink(cam)
        bpy.context.scene.collection.objects.unlink(empty)
        
        return {'FINISHED'} 
    
def register():
    bpy.utils.register_class(VIEW3D_PT_track_obj)
    bpy.utils.register_class(OBJECT_TO_create)
    bpy.utils.register_class(EnableDisableAutoSmoothOperator)
    #bpy.utils.register_class()
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_track_obj) 
    bpy.utils.unregister_class(OBJECT_TO_create)
    bpy.utils.unregister_class(EnableDisableAutoSmoothOperator)
    #bpy.utils.unregister_class()
if __name__ == "__main__":
    register()