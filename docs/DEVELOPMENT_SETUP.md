# Development instructions

This guide shows how to set up a custom scripts folder so you can reload your
add-ons without restarting **Blender**.

### Open preferences

Open **Blender** preferences by pressing `Ctrl` + `,` or going to `Edit` →
`Preferences` in the **Blender** menu.

<p align="center">
    <img src="media/blender_addon_01.webp" alt="Open preferences">
</p>

### Add custom scripts directory

In the File Paths section, add a custom scripts directory.
> [!NOTE]
Make sure there is a directory named 
`addons` (lowercase) inside the selected folder.

<p align="center">
    <img src="media/blender_addon_02.webp" alt="Add scripts directory">
</p>

### Save preferences

Save your preferences so the settings persist between **Blender** sessions.

### Refresh local add-ons
Refresh local add-ons. Your add-on should now appear in the list for enabling/disabling.

> [!NOTE]
Reload your add-on during development by refreshing local add-ons again with no need to restart Blender.

<p align="center">
    <img src="media/blender_addon_03.webp" alt="Refresh add-ons list">
</p>

### Activate the addon

Search for your add-on and activate it.

<p align="center">
<img src="media/blender_addon_04.webp" alt="Activate add-on">
</p>

## Custom scripts directory structure

Here’s an example of how your custom scripts directory might be organized when adding **Blender** add-ons.

> [!NOTE]
**Blender** supports both single-file and folder-based add-ons.

<pre>
custom scripts directory/
    └── addons/
        ├── addon.py              # Single-file add-on
        └── addon_folder/         # Folder-based add-on
            ├── __init__.py
            ├── other_module.py
            └── ...
</pre>


