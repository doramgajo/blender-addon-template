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

# Blender modules
import bpy

# Blender classes
from bpy.types import Operator


class BLENDERADDONTEMPLATE_OT_create_object(Operator):
    bl_idname = "blenderaddontemplate.create_object"
    bl_label = "Create object"

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}
