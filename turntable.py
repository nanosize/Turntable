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
frm = 100
class VIEW3D_PT_track_obj(bpy.types.Panel):
    
     #where to add the panel
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "turntable"
    bl_label = "turntable"

    def draw(self, context):
        self.layout.operator("my.button")

class My_OT_Button(bpy.types.Operator):
    bl_idname = "my.button"
    bl_label = "create"

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
        
    
        return{'FINISHED'}
#----------------------------------------------------------------debug      
"""class OBJECT_PT_CustomPanel(bpy.types.Panel):
  bl_label = "パネル"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"

  def draw(self, context):
    self.layout.operator("my.button") """
#----------------------------------------------------------------

#make collection 'track' and link with collection

#sync frame and last keflame



#class SimpleOperator(bpy.types.Operator):
    #bl_idname = "object.simple_operator"
   # bl_label = "Tool Name"
'''
class MyButton1(bpy.types.Operator):
    bl_idname = "my.button1"
    bl_label = "select_all"#メニューに表示される名前
 
    def add_set():
        global tr_obj
        tr_obj = bpy.data.collections.new('track_obj')
        bpy.data.collections['track_obj'].color_tag = 'COLOR_04'
        bpy.context.scene.collection.children.link(tr_obj)
        
    def add_circle():
        #add circle
        bpy.ops.curve.primitive_bezier_circle_add(radius=5,location=(0,
        0, 1), scale=(1, 1, 1))
        global circle
        circle = bpy.context.view_layer.objects.active
        circle.name = 'circle'

    def add_empty():
        #add empty
        bpy.ops.object.empty_add() 
        global empty 
        empty = bpy.context.view_layer.objects.active
        empty.name = 'focus_target'


        #add camera
        #get data about add objects
        #change name
    def add_camera():
        
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

    def link_collection():
        #link with track_collection
        #should wright exception handling
        tr_obj.objects.link(circle)
        tr_obj.objects.link(cam)
        tr_obj.objects.link(empty)
        bpy.context.scene.collection.objects.unlink(circle)
        bpy.context.scene.collection.objects.unlink(cam)
        bpy.context.scene.collection.objects.unlink(empty)
    

add_set() 
add_empty()
add_empty()
add_circle()
add_camera()
link_collection()
'''

#bpy.utils.register_class(SimpleOperator)

def register():
    bpy.utils.register_class(VIEW3D_PT_track_obj)
    bpy.utils.register_class(My_OT_Button)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_track_obj)
    bpy.utils.register_class(My_OT_Button)    

if __name__ == "__main__":
    register()