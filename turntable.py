bl_info = {
   "name": "turntable",
   "author": "nao_3dcg",
   "version": (0, 0, 0),
   "blender": (3, 0, 0),
   "location": "View3D > turntable",
   "description": "It automatically creates and animates the turntable.",
   "warning": "This add-on is a beta version, so please install at your own risk!",
   "wiki_url": "",
   "tracker_url": "",
   "category": "animation"
}

import bpy


initial_frame_count = None

if bpy.context.scene.frame_start:
    initial_frame_count = bpy.context.scene.frame_end

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
        layout.prop(scene, "turntable_frames", text="Frames")
        
        #layout.separator()
        
        #create button
        #layout.label(text="Create Camera:",icon="CAMERA_DATA")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.create", text="Create Camera",icon="CAMERA_DATA")
        
        layout.separator()
        
        #layout.operator("render.render", text="Start Animation Render",icon = "RENDER_ANIMATION")
        
        #delete
        layout.operator("object.delete_objects", text="Delete Objects", icon="CANCEL")



    
class  OBJECT_TO_create(bpy.types.Operator):
    bl_idname = "object.create"
    bl_label = "Tool Name"
    
    def execute(self, context):
        
        frm = bpy.context.scene.turntable_frames
        
        global cam
        cam = None
        
        if not bpy.data.collections.get('turntable'):
            
            tr_obj = bpy.data.collections.new('turntable')
            bpy.data.collections['turntable'].color_tag = 'COLOR_04'
            bpy.context.scene.collection.children.link(tr_obj)
            
            #add circle
            bpy.ops.curve.primitive_bezier_circle_add(radius=5,location=(0,
            0, 1), scale=(1, 1, 1))
            circle = bpy.context.view_layer.objects.active
            circle.name = 'turntable_circle'

            #add empty
            bpy.ops.object.empty_add() 
            empty = bpy.context.view_layer.objects.active
            empty.name = 'turntable_focus_target'

            #add camera
            #get data about add objects
            #change name
            bpy.ops.object.camera_add()
            cam = bpy.context.view_layer.objects.active
            bpy.context.scene.camera = cam
            cam.name = 'turntable_cam'
            
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
            
            end_frame = bpy.context.scene.frame_end
            end_frame = frm
      
            #add object constraint track to
            bpy.ops.object.constraint_add(type='TRACK_TO')
            cam.constraints["Track To"].target = bpy.data.objects['turntable_focus_target']
            
            # set last frame
            bpy.context.scene.frame_end = frm
            
            #link with track_collection
            #should wright exception handling
            unlink_object_from_all_collections(circle)
            unlink_object_from_all_collections(cam)
            unlink_object_from_all_collections(empty)
            tr_obj.objects.link(circle)
            tr_obj.objects.link(cam)
            tr_obj.objects.link(empty)

            return {'FINISHED'} 
        
        
def unlink_object_from_all_collections(object):
    # すべてのコレクションからオブジェクトをアンリンク
    for collection in bpy.data.collections:
        if object.name in collection.objects:
            collection.objects.unlink(object)
            
    '''
        else:
            if cam is not None:
                cam.constraints["Follow Path"].keyframe_insert("offset", frame=frm)
                bpy.context.scene.frame_end = frm
                bpy.context.scene.turntable_frames = frm 
    '''
    


class OBJECT_delete_objects(bpy.types.Operator):
    bl_idname = "object.delete_objects"
    bl_label = "Delete Objects"

    def execute(self, context):
        object_names_to_delete = ["turntable_circle", "turntable_cam", "turntable_focus_target"]

        for object_name in object_names_to_delete:
            if bpy.data.objects.get(object_name):
                bpy.data.objects.remove(bpy.data.objects[object_name])

        if bpy.data.collections.get('turntable'):
            bpy.data.collections.remove(bpy.data.collections['turntable'])
            
        if initial_frame_count is not None:
            bpy.context.scene.frame_end = initial_frame_count

        return {'FINISHED'}
    

def register():
    bpy.utils.register_class(VIEW3D_PT_track_obj)
    bpy.utils.register_class(OBJECT_TO_create)
    bpy.utils.register_class(OBJECT_delete_objects)
    bpy.types.Scene.turntable_frames = bpy.props.IntProperty(
        name="Turntable Frames",
        default=100,  # set defalt value
        min=1,  # min
        description="Number of frames for the turntable animation"
    )
    #bpy.utils.register_class()
    #bpy.utils.register_class()
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_track_obj) 
    bpy.utils.unregister_class(OBJECT_TO_create)
    #bpy.utils.unregister_class()
    #bpy.utils.unregister_class()
if __name__ == "__main__":
    register()