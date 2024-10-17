# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> BLENDER ADDON TEMPLATE

- AUTHOR:	Doramas García Jorge
- EMAIL:	doramgajo@gmail.com
- GITHUB:	https://github.com/doramgajo
- REPOSITORY:	https://github.com/doramgajo/blender-addon-template
- LINKEDIN:	https://www.linkedin.com/in/doramgajo
------------------------------------------------------------
"""

# Blender classes
from bpy.types import Panel

# Blender Addon Template classes
from ..controller.operators import BLENDERADDONTEMPLATE_OT_create_object


class BLENDERADDONTEMPLATE_PT_main_panel(Panel):
    bl_idname = "BLENDERADDONTEMPLATE_PT_main_panel"
    bl_category = "Blender Addon Template"
    bl_label = "Blender Addon Template"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass


class BLENDERADDONTEMPLATE_PT_tools(Panel):
    bl_idname = "BLENDERADDONTEMPLATE_PT_tools"
    bl_parent_id = "BLENDERADDONTEMPLATE_PT_main_panel"
    bl_label = "Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        layout.operator(
            BLENDERADDONTEMPLATE_OT_create_object.bl_idname,
            text="Create object", icon="CUBE")
