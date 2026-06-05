from PySide6.QtWidgets import *

class AddressFamilyGroupBox(QGroupBox):
    ''' This class is based on QGroupBox and has multiple elements encapsulated within it '''
    def __init__(self):
        super().__init__(title="Configure Address-Families")
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.mainlayout.addWidget(self.scrollArea)

        self.scrollAreaWidget = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.scrollAreaWidgetLayout = QVBoxLayout()
        self.scrollAreaWidget.setLayout(self.scrollAreaWidgetLayout)

        self.init_address_family_ipv4()
        self.init_address_family_vpnv4()
        self.init_address_family_evpn()



    def init_address_family_ipv4(self):
        self.AF_IPV4 = QGroupBox()
        self.AF_IPV4.setTitle("address-family ipv4")
        self.AF_IPV4_layout = QVBoxLayout()
        self.AF_IPV4.setLayout(self.AF_IPV4_layout)
        self.AF_IPV4_network = QLineEdit()
        self.AF_IPV4_network.setPlaceholderText("Eg: 8.8.8.8/32, 10.10.0.0/24")
        self.AF_IPV4_form = QFormLayout()
        self.AF_IPV4_form.addRow("network:", self.AF_IPV4_network)
        self.AF_IPV4_layout.addLayout(self.AF_IPV4_form)
        self.scrollAreaWidgetLayout.addWidget(self.AF_IPV4)

    def init_address_family_vpnv4(self):
        self.AF_VPNV4 = QGroupBox()
        self.AF_VPNV4.setTitle("address-family vpnv4")
        self.AF_VPNV4_layout = QVBoxLayout()
        self.AF_VPNV4.setLayout(self.AF_VPNV4_layout)
        self.AF_VPNV4_layout.addWidget(QLabel("** For Future Use **"))
        self.scrollAreaWidgetLayout.addWidget(self.AF_VPNV4)

    def init_address_family_evpn(self):
        self.AF_EVPN = QGroupBox()
        self.AF_EVPN.setTitle("address-family evpn")
        self.AF_EVPN_layout = QVBoxLayout()
        self.AF_EVPN.setLayout(self.AF_EVPN_layout)
        self.AF_EVPN_layout.addWidget(QLabel("** For Future Use **"))
        self.scrollAreaWidgetLayout.addWidget(self.AF_EVPN)

        