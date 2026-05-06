import FreeCAD as App
import Part

# Create a new document
doc = App.newDocument("BoxExample")

# Create a box
box = Part.makeBox(10, 10, 10)
obj = doc.addObject("Part::Feature", "MyBox")
obj.Shape = box

# Create a cylinder
cyl = Part.makeCylinder(5, 20)
cyl_obj = doc.addObject("Part::Feature", "MyCylinder")
cyl_obj.Shape = cyl
cyl_obj.Placement = App.Placement(App.Vector(15, 0, 0), App.Rotation(0, 0, 0))

# Save the document
doc.recompute()
# doc.saveAs("example.fcstd")
print("FreeCAD objects created successfully.")
