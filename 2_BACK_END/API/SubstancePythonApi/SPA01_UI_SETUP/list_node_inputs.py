# Danh sách node 
import sd
from sd.api import sduimgr
from sd.api.sdproperty import *


# Truy cập quản lí giao diện và graph và node

graph = uiMgr.getCurentGraph()
node = graph.getNodeFromId('1349044622')
nodeProps = node.getProperties(SDPropertyCategory.Input)

#L Liệt kê các node 
for i in range(len(nodeProps)):
	print(nodeProps[i].getId())
	print(nodePros[i].getType())
