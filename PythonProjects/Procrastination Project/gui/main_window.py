import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from utils.time_tracker import TimeTracker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tracker = TimeTracker()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("App Time Tracker")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to App Time Tracker", self)
        self.layout.addWidget(self.label)

        self.start_button = QPushButton("Start Tracking", self)
        self.start_button.clicked.connect(self.start_tracking)
        self.layout.addWidget(self.start_button)

        self.add_app_input = QLineEdit(self)
        self.add_app_input.setPlaceholderText("Add App (e.g., chrome.exe)")
        self.layout.addWidget(self.add_app_input)

        self.add_app_time_input = QLineEdit(self)
        self.add_app_time_input.setPlaceholderText("Add Time Limit in seconds")
        self.layout.addWidget(self.add_app_time_input)

        self.add_app_button = QPushButton("Add App", self)
        self.add_app_button.clicked.connect(self.add_app)
        self.layout.addWidget(self.add_app_button)

        self.add_site_input = QLineEdit(self)
        self.add_site_input.setPlaceholderText("Add Website (e.g., example.com)")
        self.layout.addWidget(self.add_site_input)

        self.add_site_time_input = QLineEdit(self)
        self.add_site_time_input.setPlaceholderText("Add Time Limit in seconds")
        self.layout.addWidget(self.add_site_time_input)

        self.add_site_button = QPushButton("Add Website", self)
        self.add_site_button.clicked.connect(self.add_website)
        self.layout.addWidget(self.add_site_button)

    def start_tracking(self):
        self.tracker.track_time()

    def add_app(self):
        app = self.add_app_input.text()
        limit = int(self.add_app_time_input.text())
        self.tracker.add_app(app, limit)
        self.add_app_input.clear()
        self.add_app_time_input.clear()

    def add_website(self):
        site = self.add_site_input.text()
        limit = int(self.add_site_time_input.text())
        self.tracker.add_website(site, limit)
        self.add_site_input.clear()
        self.add_site_time_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
