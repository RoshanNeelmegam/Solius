from PySide6.QtWidgets import *

class NeighboursGroupBox(QGroupBox):
    ''' This class is based on QGroupBox and has multiple elements encapsulated within it '''
    def __init__(self, neighbours_list):
        super().__init__(title="Define Neighbourships")
        self.neighbours_list = neighbours_list
        self.neighboursBoxVerticalLayout = QVBoxLayout()
        self.setLayout(self.neighboursBoxVerticalLayout)
        # building the innermost widget fully
        self.scrollAreaWidgetLayout = QVBoxLayout()
        self.scrollAreaWidgetLayout.addWidget(self.neighbour_defintion())
        # self.scrollAreaWidgetLayout.addWidget(self.neighbour_defintion())
        self.scrollAreaWidgetLayout.addStretch()  # makes it absorb the left out space 
        ScrollAreaWidget = QWidget()
        ScrollAreaWidget.setLayout(self.scrollAreaWidgetLayout)
        # building the next top layer
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(ScrollAreaWidget)
        ScrollArea.setWidgetResizable(True)
        # adding scroll area to group box layout
        self.neighboursBoxVerticalLayout.addWidget(ScrollArea)
        self.addNeigbourshipsButton = QPushButton("Add Neighbourships")
        self.addNeigbourshipsButton.clicked.connect(lambda: self.scrollAreaWidgetLayout.addWidget(self.neighbour_defintion()))
        self.neighboursBoxVerticalLayout.addWidget(self.addNeigbourshipsButton) 
    
    def neighbour_defintion(self):
        neighbour = QGroupBox()
        layout = QVBoxLayout()
        neighbour.setLayout(layout)
        neighbour_form = QFormLayout()
        # defining neighbour ip
        neighbour_ip = QLineEdit()
        neighbour_ip.setObjectName("NIP")
        neighbour_ip.setPlaceholderText("Enter neighbour address. eg: 10.0.0.1")
        neighbour_form.addRow("neighbour:", neighbour_ip)
        # defining remote as
        neighbour_as = QLineEdit()
        neighbour_as.setObjectName("NAS")
        neighbour_as.setPlaceholderText("Enter remote-as")
        neighbour_form.addRow("remote-as:", neighbour_as)
        # defining peer group
        neighbour_peer_group = QLineEdit()
        neighbour_peer_group.setObjectName("NPG")
        neighbour_peer_group.setPlaceholderText("Optional")
        neighbour_form.addRow("peer-group:", neighbour_peer_group)
        # defining address-family dropbox
        address_family_dropdown = QComboBox()
        address_family_dropdown.setObjectName("NAF")
        address_family_dropdown.setPlaceholderText("Select address-family")
        address_family_dropdown.addItems(["ipv4", "vpnv4", "evpn"])
        neighbour_form.addRow("address-family:", address_family_dropdown)        
        # defining update-source group
        neighbour_update_source = QLineEdit()
        neighbour_update_source.setObjectName("NUS")
        neighbour_update_source.setPlaceholderText("Optional")
        neighbour_form.addRow("update-source:", neighbour_update_source)
        # defining eBGP-multihop option
        eBGP_multihop = QCheckBox("eBGP multihop (set to 10 as default)")
        eBGP_multihop.setObjectName("NEMP")
        neighbour_form.addRow(eBGP_multihop)
        # defining a horizontal layout that contains add route-map and delete option
        options = QHBoxLayout()
        add_route_map_btn = QPushButton("Add Route-Map")
        add_route_map_btn.clicked.connect(lambda: self.add_route_map_connector(neighbour_form))
        delete_neighbour_btn = QPushButton("Delete Neighbour")
        delete_neighbour_btn.clicked.connect(lambda: self.delete_neighbour_connector(neighbour))
        options.addWidget(add_route_map_btn)
        options.addWidget(delete_neighbour_btn)

        layout.addLayout(neighbour_form)
        layout.addLayout(options)
        self.neighbours_list.append(neighbour)
        return neighbour

    def add_route_map_connector(self, neighbour_form):
        layout = QHBoxLayout() # horizontal layout containing route-map name and the inbound/outbound dropdown
        layout.setObjectName("RouteMap")
        route_map = QLineEdit()
        route_map.setObjectName("RouteMapName")
        route_map.setPlaceholderText("Route-Map")
        in_out = QComboBox()
        in_out.setObjectName("IO")
        in_out.setPlaceholderText("Inbound or Outbound")
        in_out.addItems(["in", "out"])
        layout.addWidget(route_map)
        layout.addWidget(in_out)
        neighbour_form.addRow("route-map:", layout)

    def delete_neighbour_connector(self, neighbour):
        if neighbour in self.neighbours_list:
            self.neighbours_list.remove(neighbour)
        self.scrollAreaWidgetLayout.removeWidget(neighbour) # removing the widget from the layout
        neighbour.deleteLater() # deleting the widget as well
        return None
