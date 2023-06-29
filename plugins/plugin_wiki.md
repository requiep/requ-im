# Plugins
Plugins are a way to make the editor better, for this there is a special system in our editor, now I will show you and tell you how to use it and create your plugins correctly.

## Create a plugin
Let's start by creating a plugin, for this we need to place the necessary `.py` file in the `plugins/` folder, now we need the plugin architecture and how it will work, after creating the file we go into it, and we start by putting the class there for execution:
```python
class Plugin(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def init(*args) -> None:
        arguments = args[0]
        print('Hello from plugin!')
```
> Note the class name! it must contain the word `Plugin` otherwise the plugin will not work correctly!

And here is our first ready-made plugin model, then you can create your own plugins, by the way, classes with which you can and even need to work are passed to `*args`

This code works immediately when the editor is launched. Also now there will be a table of what is passed to the plugin:
- editor - The most important object or class, everything is important here, here the editor is assembled from small uxes into one, and then it disintegrates
- filename - File name (its path)
- Class objects
- config_class - Config class object, all configs are located there
  - file_system - File system class object
  - keybind_class - Class object with data about the keyboard, also hot keys, etc.
  - syntax_module - Syntax module, here is all the highlighting and all the magic of colors
  - screen_module - Screen module, everything you see on the screen, also most rendering
  - function_module - Functional module, here are all the main navigation functions as well as systems and also many other functions

All this can be used, for example, now I will show you a system that opens and immediately closes, this is like a plugin:
```python
class Plugin(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def init(*args) -> None:
        arguments = args[0]
        editor = arguments['editor']
        editor.exit()
```