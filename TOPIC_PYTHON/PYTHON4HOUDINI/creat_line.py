import hou
from PySide2 import QtWidgets

# Create a simple dialog to input the length of side a from the user
class InputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(InputDialog, self).__init__(parent)
        
        self.setWindowTitle("Enter the length of side a")
        
        self.length_label = QtWidgets.QLabel("Length of side a:")
        self.length_spinbox = QtWidgets.QSpinBox()
        self.length_spinbox.setMinimum(1)
        self.length_spinbox.setValue(5)
        
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_spinbox)
        layout.addWidget(self.button_box)
        self.setLayout(layout)
        
    def get_length(self):
        return self.length_spinbox.value()


# Create a line object with length 'a' and display it on the render view
def create_and_display_line(length):
    # Create a new curve node
    geo_node = hou.node("/obj").createNode("geo")
    curve_node = geo_node.createNode("curve")
    
    # Create two points for the line
    ptnum1 = curve_node.createPoint()
    ptnum2 = curve_node.createPoint()
    
    # Set the positions of the points
    curve_node.setPointPosition(ptnum1, (0, 0, 0))
    curve_node.setPointPosition(ptnum2, (length, 0, 0))
    
    # Create a primitive (curve) using the two points
    prim_num = curve_node.createPrim("polyline")
    curve_node.setCurveVertex(prim_num, [ptnum1, ptnum2])
    
    # Display the geometry in the render view
    geo_node.layoutChildren()
    render_node = geo_node.createNode("render")
    render_node.setDisplayFlag(True)
    render_node.setRenderFlag(True)

    return curve_node


# Run the dialog to input the length of side a from the user
dialog = InputDialog()
if dialog.exec_() == QtWidgets.QDialog.Accepted:
    length = dialog.get_length()
    line = create_and_display_line(length)
    print("Created a line with length", length)
else:
    print("User cancelled line creation.")
