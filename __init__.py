"""		
rjChannelBoxPlus will add search-ability over its attributes and it will 
colour user defined attributes, making them easier to distinguish. With 
the threshold argument you can determine when to switch between colours, 
the higher the threshold the more the 2 attributes will have to match up 
to stay the same colour.

.. figure:: https://github.com/robertjoosten/rjChannelBoxPlus/raw/master/README.gif
   :align: center

Installation
============
Copy the **rjChannelBoxPlus** folder to your Maya scripts directory
::
    C:/Users/<USER>/Documents/maya/scripts

Usage
=====
Add the interface and functionality to Maya:
::
    import maya.cmds as cmds
    cmds.evalDeferred(
        "import rjChannelBoxPlus;rjChannelBoxPlus.install(threshold=0.75)"
    )
    
This line of code can also be added in the userSetup.py if you would like the 
functionality to persist.

Note
====
rjChannelBoxPlus will add search-ability over its attributes and it will 
colour user defined attributes, making them easier to distinguish. With the 
threshold argument you can determine when to switch between colours, the 
higher the threshold the more the 2 attributes will have to match up to stay 
the same colour.

Colour palette can be updated in the colour.py file that is located in this 
package, simply change the colour values or add new ones following the same 
format.

Code
====
"""

__author__    = "Robert Joosten"
__version__   = "0.8.2"
__email__     = "rwm.joosten@gmail.com"

from . import ui

def install(threshold=0.75):
    """
    Add the search interface and colouring functionality to Maya's main
    channel box. If rjChannelBoxPlus is already installed it will remove
    the previous instance. A threshold can be set, this threshold determains
    when the attributes should change colour. the higher the threshold the 
    more the 2 attributes will have to match up to stay the same colour.
    
    :param float threshold: Threshold for attribute colour change
    """
    # get channel box
    channelBox = ui.getChannelBox()
	
    # get channel box layout
    parent = channelBox.parent()
    layout = parent.layout()
    layout.setSpacing(0)
    
    # remove existing search widgets
    children = parent.children()
    names = [child.objectName() for child in children]
    
    for name, child in zip(names, children):
        if name != ui.CHANNELBOXS_SEARCH:
            continue

        child.deleteLater()
    
    # initialize search widget
    search = ui.SearchWidget(parent, threshold)

    # add search widget to layout
    if type(layout) == ui.QLayout:
        item = layout.itemAt(0)
        widget = item.widget()
        
        layout.removeWidget(widget)
        layout.addWidget(search)
        layout.addWidget(widget)
    else:   
        layout.insertWidget(0,search)
