from PySide6.QtWidgets import *
from jinja2 import Template
from Sub_Classes.neighbours_group_box import NeighboursGroupBox
from Sub_Classes.address_family_group_box import AddressFamilyGroupBox
from Sub_Classes.vrfs_group_box import VrfsGroupBox 
from templates.arista.mpBGP.arista_mp_bgp_neighbourship import neighbourship_template


class gui_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Solius Config Helper')
        self.resize(1300, 600)
        self.neighbours_list = []
        self.mac_vrfs_list = []
        self.ip_vrfs_list = []
        self.init_left_pane()
        self.init_main_layout()
        self.init_central_widget()
    
    def init_central_widget(self):
         # creating central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralWidget)

    def init_main_layout(self):
        # creating the main horizontal layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addLayout(self.leftVerticalLayout, stretch=3)
        self.text_space = QTextEdit()
        self.horizontalLayout.addWidget(self.text_space, stretch=2)

    def init_left_pane(self):
        # creating vertical layout for the left pane
        self.leftVerticalLayout = QVBoxLayout()
        # creating 3 widgets to add in the vertical layout or left pane
        self.init_first_pane()
        self.init_second_pane()
        self.init_third_pane()
        # adding all 3 created widgets in the vertical layout
        self.leftVerticalLayout.addLayout(self.routerAs, stretch=0)
        self.leftVerticalLayout.addWidget(self.neighbours_listhipBox, stretch=2)
        self.leftVerticalLayout.addLayout(self.bottom_pane, stretch=2)

    def init_first_pane(self):
        # creating the widget/formlayout for the top part in the leaf pane
        self.routerAs =  QFormLayout()
        textbox=QLineEdit()
        textbox.setMaximumWidth(120)
        generate_btn = QPushButton("Generate Configs")
        generate_btn.clicked.connect(self.generate_configs_connector)
        self.routerAs.addRow(generate_btn)
        self.routerAs.addRow("router bgp", textbox)

    def init_second_pane(self):
        # creating the widget/formlayout for the middle part in the left pane
        self.neighbours_listhipBox = NeighboursGroupBox(self.neighbours_list)

    def init_third_pane(self):
        # creating the widget/formlayout for the bottom part in the left pane
        self.bottom_pane = QHBoxLayout()
        self.addressFamilyBox = AddressFamilyGroupBox()
        self.vrfDefinitionBox = VrfsGroupBox(self.mac_vrfs_list, self.ip_vrfs_list)
        self.bottom_pane.addWidget(self.addressFamilyBox)
        self.bottom_pane.addWidget(self.vrfDefinitionBox)

    def generate_configs_connector(self):
        output = ''
        for neighbour in self.neighbours_list:
            neighbour_ip = neighbour.findChild(QLineEdit, "NIP").text()
            neighbour_remote_as = neighbour.findChild(QLineEdit, "NAS").text()
            neighbour_peer_group = neighbour.findChild(QLineEdit, "NPG").text()
            neighbour_address_family = neighbour.findChild(QComboBox, "NAF").currentText()
            neighbour_update_source = neighbour.findChild(QLineEdit, "NUS").text()
            neighbour_ebgp_multihop = neighbour.findChild(QCheckBox, "NEMP").isChecked()
            ntemplate = Template(neighbourship_template, trim_blocks=True)
            output += ntemplate.render(neighbour_ip=neighbour_ip, peer_group=neighbour_peer_group, neighbour_remote_as=neighbour_remote_as, neighbour_address_family=neighbour_address_family)
            self.text_space.clear()
            self.text_space.setPlainText(output)
            for route_map_entity in self.neighbours_list:
                route_map = route_map_entity.findChildren(QLineEdit, "RouteMapName")
                inbound_outbound = route_map_entity.findChildren(QComboBox, "IO")
                rm_dict = dict(zip(route_map, inbound_outbound))
                for key, val in rm_dict.items():
                    print(key.text(), val.currentText())


        
        




