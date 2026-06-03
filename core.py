from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QGroupBox, QScrollArea, QPushButton, QLineEdit

class gui_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Solius Config Helper')
        self.resize(1300, 700)
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
        self.init_routerAS_box()
        self.init_neighbourships_box()
        self.init_addressFamily_box()
        # adding all 3 created widgets in the vertical layout
        self.leftVerticalLayout.addLayout(self.routerAs, stretch=0)
        self.leftVerticalLayout.addWidget(self.neighboursBox, stretch=2)
        self.leftVerticalLayout.addWidget(self.addressFamilyBox, stretch=2)

    def init_routerAS_box(self):
        # creating Widget 1 in the left layout
        self.routerAs =  QFormLayout()
        textbox=QLineEdit()
        textbox.setMaximumWidth(120)
        self.routerAs.addRow("router bgp", textbox)

    def init_neighbourships_box(self):
        # creating Widget 2 in the left layout
        self.neighboursBox = QGroupBox(title="Define Neighbourships")
        self.neighboursBoxVerticalLayout = QVBoxLayout()
        # creating a Scroll Area
        ScrollArea = QScrollArea()
        ScrollAreaWidget = QWidget()
        ScrollArea.setWidget(ScrollAreaWidget)
        # creating a vertical layout withing the Scroll Area Widget
        self.neighboursScrollAreaVerticalLayout = QVBoxLayout()
        ScrollAreaWidget.setLayout(self.neighboursScrollAreaVerticalLayout)
        self.neighboursBoxVerticalLayout.addWidget(ScrollArea, stretch=2)
        self.neighboursBoxVerticalLayout.addWidget(QPushButton("Add Neighbourships"))
        self.neighboursBox.setLayout(self.neighboursBoxVerticalLayout)
        self.neighboursScrollAreaVerticalLayout.addWidget(QLabel("Test"))
        self.neighboursScrollAreaVerticalLayout.addLayout(self.neighbour_defintion())
        

    def init_addressFamily_box(self):
        # creating Widget 3 in the left layout
        self.addressFamilyBox = QGroupBox(title="Configure Address-Families")

    def neighbour_defintion(self):
        neighbourship_box = QVBoxLayout()
        neighbour_ip = QLineEdit()
        neighbour_ip.setPlaceholderText("Enter neighbour address. eg: 10.0.0.1")
        neighbourship_box.addWidget(neighbour_ip)
        return neighbourship_box
        



