"""
ChannelBoxPlus will add search-ability over its attributes and it will
colour user defined attributes, making them easier to distinguish. With
the threshold argument you can determine when to switch between colours,
the higher the threshold the more the 2 attributes will have to match up
to stay the same colour, this value can be adjusted in the userSetup.py.

.. figure:: /_images/channelBoxPlusExample.gif
   :align: center

Installation
============
* Extract the content of the .rar file anywhere on disk.
* Drag the channelBoxPlus.mel file in Maya to permanently install the script.

Note
====
Colour palette can be updated in the `colour.py file` that is located in this
package, simply change the colour values or add new ones following the same 
format.
"""
from .ui import install

__author__ = "Robert Joosten"
__version__ = "0.8.3"
__email__ = "rwm.joosten@gmail.com"
