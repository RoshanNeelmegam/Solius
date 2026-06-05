from PySide6.QtWidgets import *

class VrfsGroupBox(QGroupBox):
    ''' This class is based on QGroupBox and has multiple elements encapsulated within it '''
    def __init__(self, macVrfsList, ipVrfsList):
        self.macVrfs = macVrfsList
        self.ipVrfs = ipVrfsList
        super().__init__(title="Define Mac/Ip Vrfs")
        self.verticalLayout = QVBoxLayout()
        self.setLayout(self.verticalLayout)
        # creating the innermost widget first
        self.ScrollAreaWidgetLayout = QVBoxLayout()
        # creating the next layer widget
        ScrollAreaWidget = QWidget()
        ScrollAreaWidget.setLayout(self.ScrollAreaWidgetLayout)
        # creating the next layer widget
        ScrollArea = QScrollArea()
        ScrollArea.setWidget(ScrollAreaWidget)
        ScrollArea.setWidgetResizable(True)
        self.ButtonsLayout = QHBoxLayout()
        self.add_mac_vrf_btn = QPushButton("Add Mac Vrf")
        self.add_mac_vrf_btn.clicked.connect(lambda: self.ScrollAreaWidgetLayout.addWidget(self.mac_vrf_defintion()))
        self.add_ip_vrf_btn = QPushButton("Add Ip Vrf")
        self.add_ip_vrf_btn.clicked.connect(lambda: self.ScrollAreaWidgetLayout.addWidget(self.ip_vrf_defintion()))
        self.ButtonsLayout.addWidget(self.add_mac_vrf_btn)
        self.ButtonsLayout.addWidget(self.add_ip_vrf_btn)
        self.verticalLayout.addWidget(ScrollArea)
        self.verticalLayout.addLayout(self.ButtonsLayout)

    def mac_vrf_defintion(self):
        mac_vrf = QGroupBox()
        layout = QVBoxLayout()
        mac_vrf.setLayout(layout)
        mac_vrf_form = QFormLayout()
        # defining mac vrf type field
        vlan_type = QComboBox()
        vlan_type.setObjectName("vlanType")
        vlan_type.setPlaceholderText("Select Mac Vrf Type")
        vlan_type.addItems(["vlan", "vlan-aware-bundle"])
        mac_vrf_form.addRow("mac-vrf type:", vlan_type)      
        # define mac vrf vlan input field
        vlans = QLineEdit()
        vlans.setObjectName("VlanNumber")
        vlans.setPlaceholderText("Enter the vlan(s) number")
        mac_vrf_form.addRow("vlan(s):", vlans)
        # define mac vrf specific redistribute check boxes
        host_route = QCheckBox("redistribute host-route")
        static = QCheckBox("redistribute static")
        learned = QCheckBox("redistribute learned")
        igmp = QCheckBox("redistribute igmp")
        router_mac = QCheckBox("redistribute router-mac")
        mac_vrf_form.addRow(host_route)
        mac_vrf_form.addRow(static)
        mac_vrf_form.addRow(learned)
        mac_vrf_form.addRow(igmp)
        mac_vrf_form.addRow(router_mac)
        ## can add more in the future if needed ##
        # define rd for the mac vrf
        rd = QLineEdit()
        rd.setObjectName("MACRD")
        rd.setPlaceholderText("Enter RD")
        mac_vrf_form.addRow("rd", rd)
        # defining the buttons for the function of adding/deleting route-targets and deleting the mac-vrf in itself
        options = QHBoxLayout()
        add_route_target_btn = QPushButton("Add Route-Target")
        add_route_target_btn.clicked.connect(lambda: self.add_mac_route_target_connector(mac_vrf_form))
        delete_mac_vrf_btn = QPushButton("Delete Mac Vrf")
        delete_mac_vrf_btn.clicked.connect(lambda: self.delete_vrf_connector(vrf=mac_vrf, vrfType="MacVrf"))   
        options.addWidget(add_route_target_btn)
        options.addWidget(delete_mac_vrf_btn)

        layout.addLayout(mac_vrf_form)
        layout.addLayout(options)
        self.macVrfs.append(mac_vrf)
        return mac_vrf

    def ip_vrf_defintion(self):
        ip_vrf = QGroupBox()
        layout = QVBoxLayout()
        ip_vrf.setLayout(layout)
        ip_vrf_form = QFormLayout()
        # define ip vrf name input field
        vrf = QLineEdit()
        vrf.setObjectName("VrfName")
        vrf.setPlaceholderText("Enter the vrf name")
        ip_vrf_form.addRow("vrf:", vrf)
        # define mac vrf specific redistribute check boxes
        attached_host = QCheckBox("redistribute attached-host")
        static = QCheckBox("redistribute static")
        connected = QCheckBox("redistribute connected")
        evpn_multicast = QCheckBox("evpn multicast")
        ip_vrf_form.addRow(attached_host)
        ip_vrf_form.addRow(static)
        ip_vrf_form.addRow(connected)
        ip_vrf_form.addRow(evpn_multicast)
        ## can add more in the future if needed ##
        # define rd for the mac vrf
        rd = QLineEdit()
        rd.setObjectName("IPRD")
        rd.setPlaceholderText("Enter RD")
        ip_vrf_form.addRow("rd", rd)
        # defining the buttons for the function of adding/deleting route-targets and deleting the mac-vrf in itself
        options = QHBoxLayout()
        add_route_target_btn = QPushButton("Add Route-Target")
        add_route_target_btn.clicked.connect(lambda: self.add_ip_route_target_connector(ip_vrf_form))
        delete_ip_vrf_btn = QPushButton("Delete IP Vrf")
        delete_ip_vrf_btn.clicked.connect(lambda: self.delete_vrf_connector(vrf=ip_vrf, vrfType="IpVrf"))
        options.addWidget(add_route_target_btn)
        options.addWidget(delete_ip_vrf_btn)

        layout.addLayout(ip_vrf_form)
        layout.addLayout(options)
        self.ipVrfs.append(ip_vrf)
        return ip_vrf

    def add_mac_route_target_connector(self, mac_vrf_form):
        layout = QHBoxLayout() # horizontal layout containing route-map name and the inbound/outbound dropdown
        layout.setObjectName("RouteTargetLayout")
        route_target = QLineEdit()
        route_target.setObjectName("RouteTarget")
        route_target.setPlaceholderText("Route-Target")
        import_export = QComboBox()
        import_export.setObjectName("IE")
        import_export.setPlaceholderText("Inbound or Outbound")
        import_export.addItems(["import", "export", "both"])
        layout.addWidget(route_target)
        layout.addWidget(import_export)
        mac_vrf_form.addRow("route-target:", layout)

    def add_ip_route_target_connector(self, ip_vrf_form):
        layout = QHBoxLayout() # horizontal layout containing route-map name and the inbound/outbound dropdown
        layout.setObjectName("RouteTargetLayout")
        route_target = QLineEdit()
        route_target.setObjectName("RouteTarget")
        route_target.setPlaceholderText("Route-Target")
        import_export = QComboBox()
        import_export.setObjectName("IE")
        import_export.setPlaceholderText("Import or Export")
        import_export.addItems(["import", "export", "both"])
        address_family = QComboBox()
        address_family.setObjectName("AF")
        address_family.setPlaceholderText("evpn or vpnv4")
        address_family.addItems(["evpn", "vpnv4"])
        layout.addWidget(route_target)
        layout.addWidget(import_export)
        layout.addWidget(address_family)
        ip_vrf_form.addRow("route-target:", layout)

    def delete_vrf_connector(self, vrf, vrfType):
        if vrfType == "MacVrf":
            if vrf in self.macVrfs:
                self.macVrfs.remove(vrf)
            self.ScrollAreaWidgetLayout.removeWidget(vrf) # removing the widget from the layout
            vrf.deleteLater() # deleting the widget as well
            return None
        elif vrfType == "IpVrf":
            if vrf in self.ipVrfs:
                self.ipVrfs.remove(vrf)
            self.ScrollAreaWidgetLayout.removeWidget(vrf) # removing the widget from the layout
            vrf.deleteLater() # deleting the widget as well
            return None

        