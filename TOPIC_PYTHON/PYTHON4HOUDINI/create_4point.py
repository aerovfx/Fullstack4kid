import hou

# Nhập chiều dài cạnh a từ người dùng
a = 5

# Tạo một đối tượng Geometry
geo = hou.node("/obj").createNode("geo", "box_Geometry")

# Tạo một hộp vuông với chiều dài cạnh bằng a
box = geo.createNode("box")
box.parm("sizex").set(a)
box.parm("sizey").set(a)
box.parm("sizez").set(a)

# Xóa các mặt của khối hộp
box.parm("deletexneg").set(True)
box.parm("deleteyneg").set(True)
box.parm("deletezneg").set(True)
box.parm("deletexpos").set(True)

# Tạo 4 điểm A, B, C, D
point_A = geo.createNode("point")
point_A.parm("tx").set(-a / 2)
point_A.parm("ty").set(-a / 2)
point_A.parm("tz").set(a / 2)
point_A.setName("A")

point_B = geo.createNode("point")
point_B.parm("tx").set(a / 2)
point_B.parm("ty").set(-a / 2)
point_B.parm("tz").set(a / 2)
point_B.setName("B")

point_C = geo.createNode("point")
point_C.parm("tx").set(a / 2)
point_C.parm("ty").set(a / 2)
point_C.parm("tz").set(a / 2)
point_C.setName("C")

point_D = geo.createNode("point")
point_D.parm("tx").set(-a / 2)
point_D.parm("ty").set(a / 2)
point_D.parm("tz").set(a / 2)
point_D.setName("D")

# Hiển thị tọa độ của 4 điểm lên màn hình render
point_geo = geo.createNode("point")
point_geo.parm("dcolor").set((1, 1, 0))  # Màu vàng cho điểm
point_geo.parm("pscale").set(0.1)  # Kích thước điểm

# Kết nối 4 điểm với đối tượng Geometry
point_A.setInput(0, point_geo)
point_B.setInput(0, point_geo)
point_C.setInput(0, point_geo)
point_D.setInput(0, point_geo)

# Hiển thị đối tượng lên màn hình render
render_node = hou.node("/out").createNode("render")
render_node.setRenderFlag(True)
render_node.setRenderBackground(True)
render_node.setRenderRegion(True)
render_node.setDisplayFlag(True)

# Kết nối đối tượng Geometry và điểm với màn hình render
box.setRenderFlag(True)
box.setRenderNode(render_node)
point_geo.setRenderFlag(True)
point_geo.setRenderNode(render_node)


# Tự động chuyển đến màn hình render
hou.ui.curDesktop().setCurrentNode(render_node)