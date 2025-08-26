"""
Blender Add-on Template

Blender Add-on operators module.
"""

# Blender-Python API imports
from bpy.types import Operator
from bpy.ops import mesh


class ADDONNAME_OT_create_cube(Operator):
    """Operator to create a primitive cube in the scene."""
    bl_idname = "addonname.create_cube"
    bl_label = "Create cube"

    def execute(self, context):
        mesh.primitive_cube_add()
        return {"FINISHED"}


registrable = [
    ADDONNAME_OT_create_cube,
]
