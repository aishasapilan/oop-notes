import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QGridLayout

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 300)
        
        # Create central widget and set layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create an input field
        self.entry = QLineEdit()
        self.entry.setFixedHeight(40)
        layout.addWidget(self.entry)
        
        # Create buttons for digits and operations
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "=", "/"
        ]
        
        grid_layout = QGridLayout()
        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedHeight(50)
            btn.clicked.connect(lambda _, b=button: self.button_click(b))
            grid_layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create Backspace and Clear buttons
        clear_btn = QPushButton("C")
        clear_btn.setFixedHeight(50)
        clear_btn.clicked.connect(lambda: self.button_click("C"))
        grid_layout.addWidget(clear_btn, row, 2)

        backspace_btn = QPushButton("?")
        backspace_btn.setFixedHeight(50)
        backspace_btn.clicked.connect(lambda: self.button_click("?"))
        grid_layout.addWidget(backspace_btn, row, 3)
        
        layout.addLayout(grid_layout)

    def button_click(self, char):
        current = self.entry.text()
        if char == "C":
            self.entry.clear()
        elif char == "=":
            try:
                result = eval(current)
                self.entry.setText(str(result))
            except Exception:
                self.entry.setText("Error")
        elif char == "?":
            self.entry.setText(current[:-1])
        else:
            self.entry.setText(current + char)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()

