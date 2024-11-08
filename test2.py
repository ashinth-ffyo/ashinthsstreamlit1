from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load the UI file
        ui_file = QFile("qtguiapp/mainwindow.ui")
        ui_file.open(QFile.ReadOnly)
        
        # Set up the UI using QUiLoader
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        # Connect button to a function to print input values
        self.ui.findChild(QPushButton, "pushButton").clicked.connect(self.print_inputs_1)
        self.ui.findChild(QPushButton, "pushButton_2").clicked.connect(self.print_inputs_2)
        self.ui.findChild(QPushButton, "pushButton_3").clicked.connect(self.print_inputs_3)
        self.ui.findChild(QPushButton, "exitter").clicked.connect(quit)

    def print_inputs_1(self):
        print("Clicked Living Room")
    
    def print_inputs_2(self):
        print("Clicked Bed Room")

    def print_inputs_3(self):
        print("Clicked Dinging Room")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    app.exec()
