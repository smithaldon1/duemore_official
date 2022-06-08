from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # MainWindow Properties
        self.setWindowTitle("DueMore Life Manager | Tasks")
        # call setupUi function
        self.setupUi(self)
    
    def setupUi(self):
        """Setup User Interface
        """
        # Layout
        label = QLabel("Main Window")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

        # Toolbar Definition
        toolbar = QToolBar("mainWindow ToolBar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        new_task = QAction(QIcon("plus-circle.png"), "New Task")
        new_project = QAction(QIcon("folder--plus.png"))

