from PySide6.QtWidgets import *

class AddressFamilyGroupBox(QGroupBox):
    ''' This class is based on QGroupBox and has multiple elements encapsulated within it '''
    def __init__(self):
        super().__init__(title="Configure Address-Families")