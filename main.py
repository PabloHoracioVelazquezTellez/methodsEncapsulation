from classWindow import Window

ventana = Window()
ventana.setSize(500,500)
ventana.setTitulo("Mi primera App :D")
ventana.setResize(True)

print(ventana.getSize())
print(ventana.getResize())
print(ventana.getTitulo())

ventana.crear_ventana()
print("\n")