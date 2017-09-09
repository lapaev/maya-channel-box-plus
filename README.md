# rjChannelBoxPlus
rjChannelBoxPlus will add search-ability over its attributes and it will colour user defined attributes, making them easier to distinguish. With the threshold argument you can determine when to switch between colours, the higher the threshold the more the 2 attributes will have to match up to stay the same colour.

<p align="center"><img src="https://github.com/robertjoosten/rjChannelBoxPlus/blob/master/README.gif"></p>

## Installation
Copy the **rjChannelBoxPlus** folder to your Maya scripts directory:
> C:\Users\<USER>\Documents\maya\scripts

## Usage
Add the interface and functionality to Maya:
```python
import maya.cmds as cmds
cmds.evalDeferred(
    "import rjChannelBoxPlus;rjChannelBoxPlus.install(threshold=0.75)"
)
```
This line of code can also be added in the userSetup.py if you would like the functionality to persist.
  
## Customize
Colour palette can be updated in the colour.py file that is located in this package, simply change the colour values or add new ones following the same format.
