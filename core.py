from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QGroupBox, QScrollArea, QPushButton, QLineEdit

class gui_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Solius Config Helper')
        self.resize(1300, 700)
        self.neighbours = []
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
        self.leftVerticalLayout.addWidget(self.neighbourshipBox, stretch=2)
        self.leftVerticalLayout.addWidget(self.addressFamilyBox, stretch=2)

    def init_routerAS_box(self):
        # creating Widget 1 in the left layout
        self.routerAs =  QFormLayout()
        textbox=QLineEdit()
        textbox.setMaximumWidth(120)
        self.routerAs.addRow("router bgp", textbox)

    def init_neighbourships_box(self):
        # creating Widget 2 in the left layout
        self.neighbourshipBox = QGroupBox(title="Define Neighbourships")
        self.neighboursBoxVerticalLayout = QVBoxLayout()
        self.neighbourshipBox.setLayout(self.neighboursBoxVerticalLayout)
        
        # building the innermost widget fully
        self.scrollAreaWidgetLayout = QVBoxLayout()
        self.scrollAreaWidgetLayout.addWidget(self.neighbour_defintion())
        self.scrollAreaWidgetLayout.addWidget(self.neighbour_defintion())
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

    def init_addressFamily_box(self):
        # creating Widget 3 in the left layout
        self.addressFamilyBox = QGroupBox(title="Configure Address-Families")

    def neighbour_defintion(self):
        neighbour = QGroupBox()
        layout = QVBoxLayout()
        neighbour.setLayout(layout)
        # defining neighbour ip
        neighbour_ip = QLineEdit()
        neighbour_ip.setPlaceholderText("Enter neighbour address. eg: 10.0.0.1")
        neighbour_ip_form = QFormLayout()
        neighbour_ip_form.addRow("neighbour:", neighbour_ip)
        # defining remote as
        neighbour_as = QLineEdit()
        neighbour_as.setPlaceholderText("Enter remote-as")
        neighbour_as_form = QFormLayout()
        neighbour_as_form.addRow("remote-as:", neighbour_as)

        layout.addLayout(neighbour_ip_form)
        layout.addLayout(neighbour_as_form)
        self.neighbours.append(neighbour)
        return neighbour
        



