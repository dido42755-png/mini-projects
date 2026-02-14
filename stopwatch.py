import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel('00:00:00', self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(500, 200, 600, 300)

        # Vertical layout for time label + buttons
        vbox = QVBoxLayout()
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label)

        # Horizontal layout for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Connect buttons
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Styling
        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                padding: 20px;
                font-weight: bold;
                font-family: Calibri;
            }
            QLabel {
                font-size: 80px;
                font-weight: bold;
                color: red;
                background-color: black;
                border-radius: 20px;
            }
        """)

    def start(self):
        self.timer.start(10)  # Update every 10 ms

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText('00:00:00')  # Display zero immediately

    def update_display(self):
        self.time = self.time.addMSecs(10)
        minutes = self.time.minute()
        seconds = self.time.second()
        centiseconds = int(self.time.msec() / 10)  # Two digits for milliseconds
        self.time_label.setText(f"{minutes:02}:{seconds:02}:{centiseconds:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec())
