from PySide6.QtWidgets import *
from Sub_Classes.neighbours_group_box import NeighboursGroupBox
from Sub_Classes.address_family_group_box import AddressFamilyGroupBox
from Sub_Classes.vrfs_group_box import VrfsGroupBox

class gui_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Solius Config Helper')
        self.resize(1300, 600)
        self.neighbours = []
        self.macVrfs = []
        self.ipVrfs = []
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
        self.horizontalLayout.addWidget(QTextEdit(), stretch=2)

    def init_left_pane(self):
        # creating vertical layout for the left pane
        self.leftVerticalLayout = QVBoxLayout()
        # creating 3 widgets to add in the vertical layout or left pane
        self.init_first_pane()
        self.init_second_pane()
        self.init_third_pane()
        # adding all 3 created widgets in the vertical layout
        self.leftVerticalLayout.addLayout(self.routerAs, stretch=0)
        self.leftVerticalLayout.addWidget(self.neighbourshipBox, stretch=2)
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
        self.neighbourshipBox = NeighboursGroupBox(self.neighbours)

    def init_third_pane(self):
        # creating the widget/formlayout for the bottom part in the left pane
        self.bottom_pane = QHBoxLayout()
        self.addressFamilyBox = AddressFamilyGroupBox()
        self.vrfDefinitionBox = VrfsGroupBox(self.macVrfs, self.ipVrfs)
        self.bottom_pane.addWidget(self.addressFamilyBox)
        self.bottom_pane.addWidget(self.vrfDefinitionBox)

    def generate_configs_connector(self):
        pass
        # will continue tomorrow
        # for X in self.neighbours:
        #     print(X)
        #     route_maps=X.findChildren(QLineEdit, "RouteMapName")

        #     IOList = X.findChildren(QComboBox, "IO")
        #     a= dict(zip(route_maps, IOList))
        #     for key, val in a.items():
        #         print(key.text(), val.currentText())


        
        




