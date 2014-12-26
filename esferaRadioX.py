import maya.cmds
resultado = cmds.promptDialog(message='Escribe el radio:')
radio =  cmds.promptDialog(query=True,text=True)
print radio
maya.cmds.sphere(radius=radio)