import hashlib
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Functions import *
from cryptog import *
import sqlite3

Font1 = QFont("Calibri", 10)
spacer_expanding_H = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
spacer_expanding_V = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Password")
        self.setMaximumSize(200, 200)
        self.main_layout = QVBoxLayout()
        self.resize(200, 150)
        self.setLayout(self.main_layout)

        # Title
        self.big_title = QLabel()
        self.big_title.setText("Create your password")
        self.big_title.setAlignment(Qt.AlignCenter)
        self.big_title.setFont(QFont("Bahnschrift", 13))
        self.main_layout.addWidget(self.big_title)

        self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.main_layout.addItem(self.spacer1)

        # Signup grid
        self.signup_grid = QGridLayout()
        self.main_layout.addLayout(self.signup_grid)

        # Password + input
        self.signup_label = QLabel()
        self.signup_label.setText("Create password: ")
        self.signup_label.setFont(Font1)
        self.signup_grid.addWidget(self.signup_label, 0, 0)

        self.signup_lineedit = QLineEdit()
        self.signup_lineedit.setFont(Font1)
        self.signup_grid.addWidget(self.signup_lineedit, 0, 1)

        # Confirming password
        self.signup_c_label = QLabel()
        self.signup_c_label.setText("Confirm password: ")
        self.signup_c_label.setFont(Font1)
        self.signup_grid.addWidget(self.signup_c_label, 1, 0)

        self.signup_c_lineedit = QLineEdit()
        self.signup_c_lineedit.setFont(Font1)
        self.signup_grid.addWidget(self.signup_c_lineedit, 1, 1)

        # Signup button
        self.signup_button = QPushButton()
        self.signup_button.setText("Signup")
        self.signup_button.clicked.connect(lambda: signup_onClick(self))
        self.signup_grid.addWidget(self.signup_button, 1, 2)

        self.main_layout.addItem(spacer_expanding_V)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setMaximumSize(200, 200)
        self.main_layout = QVBoxLayout()
        self.resize(200, 150)
        self.setLayout(self.main_layout)

        # Title
        self.big_title = QLabel()
        self.big_title.setText("Enter your password to get started")
        self.big_title.setAlignment(Qt.AlignCenter)
        self.big_title.setFont(QFont("Bahnschrift", 13))
        self.main_layout.addWidget(self.big_title)

        self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.main_layout.addItem(self.spacer1)

        # Login grid
        self.login_grid = QGridLayout()
        self.main_layout.addLayout(self.login_grid)

        # Login + input
        self.login_label = QLabel()
        self.login_label.setText("Login: ")
        self.login_label.setFont(Font1)
        self.login_grid.addWidget(self.login_label, 0, 0)

        self.login_lineedit = QLineEdit()
        self.login_lineedit.setFont(Font1)
        self.login_grid.addWidget(self.login_lineedit, 0, 1)

        # Login button
        self.login_button = QPushButton()
        self.login_button.setText("Login")
        self.login_button.clicked.connect(lambda: login_onClick(self))
        self.login_grid.addWidget(self.login_button, 0, 2)

        # Signup?
        self.signup_layout = QHBoxLayout()
        self.main_layout.addLayout(self.signup_layout)

        self.signup_label = QLabel()
        self.signup_label.setText("Do you want to signup?")
        self.signup_label.setFont(Font1)
        self.signup_layout.addWidget(self.signup_label)

        self.signup_button = QPushButton()
        self.signup_button.setText("Signup")
        self.signup_button.clicked.connect(self.signup_onClick)
        self.signup_layout.addWidget(self.signup_button)

        self.signup_window = SignupWindow()

        self.main_layout.addItem(spacer_expanding_V)

    def signup_onClick(self):
        self.signup_window.show()
        self.close()


class AddingPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adding password")
        self.setMaximumSize(400, 400)
        self.main_layout = QVBoxLayout()
        self.resize(300, 300)
        self.setLayout(self.main_layout)

        self.grid = QGridLayout()
        self.main_layout.addLayout(self.grid)

        # Website Label + Input
        self.website_label = QLabel()
        self.website_label.setText("Website: ")
        self.website_label.setFont(Font1)
        self.grid.addWidget(self.website_label, 0, 0)

        self.website_lineedit = QLineEdit()
        self.website_lineedit.setFont(Font1)
        self.grid.addWidget(self.website_lineedit, 0, 1)

        # Password label + input + generation
        self.password_label = QLabel()
        self.password_label.setText("Password: ")
        self.password_label.setFont(Font1)
        self.grid.addWidget(self.password_label, 1, 0)

        self.password_lineedit = QLineEdit()
        self.password_lineedit.setFont(Font1)
        self.grid.addWidget(self.password_lineedit, 1, 1)

        self.generate_button = QPushButton()
        self.generate_button.setText("Generate")
        self.generate_button.clicked.connect(self.generate_onClick)
        self.grid.addWidget(self.generate_button, 1, 2)

        self.add_button = QPushButton()
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.add_onClick)
        self.grid.addWidget(self.add_button, 2, 2)

        # Generating options
        self.generating_layout = QHBoxLayout()
        self.main_layout.addLayout(self.generating_layout)

        self.generating_layout.addItem(spacer_expanding_H)

        self.generating_grid = QGridLayout()
        self.generating_layout.addLayout(self.generating_grid)

        self.lenght_label = QLabel()
        self.lenght_label.setText("Length: ")
        self.lenght_label.setFont(Font1)
        self.generating_grid.addWidget(self.lenght_label, 0, 0)

        self.length_spinbox = QSpinBox()
        self.length_spinbox.setValue(8)
        self.length_spinbox.setMaximum(64)
        self.generating_grid.addWidget(self.length_spinbox, 0, 1)

        self.generating_layout.addItem(spacer_expanding_H)

    # Clicking Generate Password
    def generate_onClick(self):
        passwd = create_password(self.length_spinbox.value())
        self.password_lineedit.setText(passwd)

    # Clicking Add
    def add_onClick(self):
        website = self.website_lineedit.text()
        passwd = self.password_lineedit.text()
        password_encrypted, iv = encrypt_password(passwd, get_key())
        if website != "" and passwd != "":
            add_to_database(website, password_encrypted, iv)
            loading_database(win)
            self.website_lineedit.setText("")
            self.password_lineedit.setText("")
            self.close()


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password generator")
        self.main_layout = QVBoxLayout(self)
        self.resize(500, 400)

        # Title
        self.big_title = QLabel()
        self.big_title.setText("Password generator")
        self.big_title.setAlignment(Qt.AlignCenter)
        self.big_title.setFont(QFont('Bahnschrift', 20))
        self.main_layout.addWidget(self.big_title)

        # Spacer 1
        self.space1 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.main_layout.addItem(self.space1)

        # Label (Saved Pass)
        self.savedPass_label = QLabel()
        self.savedPass_label.setText("Saved passwords:")
        self.savedPass_label.setAlignment(Qt.AlignLeft)
        self.savedPass_label.setFont(QFont('Bahnschrift', 15))
        self.main_layout.addWidget(self.savedPass_label)

        # Spacer 2
        self.space2 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.main_layout.addItem(self.space2)

        # Grid + Spacer
        self.vertical_layout = QVBoxLayout()
        self.main_layout.addLayout(self.vertical_layout)

        self.layout_scroll = QHBoxLayout()
        self.scrollArea = QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.vertical_layout.addWidget(self.scrollArea)

        # Grid Layout
        self.savedPassGrid = QGridLayout(self.scrollAreaWidgetContents)
        self.savedPassGrid.setColumnStretch(0, 5)
        self.savedPassGrid.setColumnStretch(1, 5)
        self.savedPassGrid.setColumnStretch(2, 5)

        self.websites_label = QLabel()
        self.websites_label.setText("Websites")
        self.websites_label.setAlignment(Qt.AlignCenter)
        self.websites_label.setFont(QFont('Calibri', 13))
        self.savedPassGrid.addWidget(self.websites_label, 0, 0)

        self.password_label = QLabel()
        self.password_label.setText('Password')
        self.password_label.setFont(QFont('Calibri', 13))
        self.password_label.setAlignment(Qt.AlignCenter)
        self.savedPassGrid.addWidget(self.password_label, 0, 1)

        self.visibility_label = QLabel()
        self.visibility_label.setText('Visibility')
        self.visibility_label.setAlignment(Qt.AlignCenter)
        self.visibility_label.setFont(QFont('Calibri', 13))
        self.savedPassGrid.addWidget(self.visibility_label, 0, 2)

        # Add button (Layout + button)
        self.add_button_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.add_button_layout)

        self.spacer3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.add_button_layout.addItem(self.spacer3)

        self.add_button = QPushButton()
        self.add_button.setText("Add")
        self.add_button_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.add_window = AddingPasswordWindow()

        self.spacer_endgrid = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(self.spacer_endgrid)
        self.vertical_layout.addItem(self.spacer_endgrid)

        # Final Spacer
        self.spacer_end = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(self.spacer_end)
        self.savedPassGrid.takeAt(1000)

    # Clicking add button
    def add_button_clicked(self):
        self.add_window.show()

    # Adding websites and passwords rows from Database
    def addRowToGrid(self, website, passwd):

        row_count = self.savedPassGrid.rowCount()

        website_label = QLabel()
        website_label.setText(website)
        website_label.setFont(QFont("Calibri", 12))
        website_label.setAlignment(Qt.AlignCenter)

        password_linedit = QLineEdit()
        password_linedit.setFrame(False)
        password_linedit.setReadOnly(True)
        password_linedit.setEchoMode(QLineEdit.Password)
        password_linedit.setText(passwd)
        password_linedit.setFont(QFont("Calibri", 12))
        password_linedit.setAlignment(Qt.AlignCenter)

        checkbox = QCheckBox()

        self.savedPassGrid.addWidget(website_label, row_count, 0, Qt.AlignCenter)
        self.savedPassGrid.addWidget(password_linedit, row_count, 1, Qt.AlignCenter)
        self.savedPassGrid.addWidget(checkbox, row_count, 2, Qt.AlignCenter)

        checkbox.stateChanged.connect(lambda: self.show_password(row_count, checkbox.isChecked()))

    # Checkbox visibility
    def show_password(self, row, checked):
        lineedit = self.savedPassGrid.itemAtPosition(row, 1).widget()
        if checked:
            lineedit.setEchoMode(QLineEdit.Normal)
        else:
            lineedit.setEchoMode(QLineEdit.Password)


# Empty the passwords grid
def empty_grid(grid):
    for i in range(1, grid.rowCount()):
        for j in range(0, 3):
            widget_item = grid.itemAtPosition(i, j)
            if widget_item is not None:
                widget = widget_item.widget()
                if widget:
                    grid.removeWidget(widget)
                    widget.deleteLater()


# Loading database to use
def loading_database(window):
    empty_grid(window.savedPassGrid)
    conn = sqlite3.connect("login_info.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Login_info (
                        Website TEXT NOT NULL,
                        Password BLOB,
                        iv BLOB
                        )''')

    cursor.execute("SELECT Website, Password, iv FROM Login_info")

    for r in cursor.fetchall():
        website = r[0]
        passwd_decrypted = decrypt_password(r[1], r[2], get_key())
        window.addRowToGrid(website, passwd_decrypted)


# Login Clicked
def login_onClick(current):
    hashed_entered_pass = hashlib.sha256(current.login_lineedit.text().encode()).hexdigest()
    with open('data.bin', 'rb') as f:
        hashed_pass = f.readline().rstrip(b'\n').decode()

    if hashed_entered_pass == hashed_pass:
        loading_database(win)
        win.show()
        current.close()


# Signup Clicked
def signup_onClick(current):

    enc_key_p = b"G\x82\x91\xf3\xf3\xf1)\xd4F\x8dd'$\x17\x1c\xfc\xe1\xf1\xed\xa0\x90-\xa3I\x1dL\xd0\x03\xcd\xbd\xdb\xe7"

    # If the two fields are matching
    if (current.signup_lineedit.text() == current.signup_c_lineedit.text()
            and current.signup_lineedit.text() != ""):

        reset_data_and_database()

        passwd = current.signup_lineedit.text()
        hashed_pass = hashlib.sha256(passwd.encode()).hexdigest()
        encrypted_pass, iv = encrypt_password(passwd, enc_key_p)

        # Saving to bin file
        with open('data.bin', 'ab') as f:
            f.write(hashed_pass.encode() + b'\n')
            f.write(encrypted_pass + b'\n')
        with open('data.bin', 'ab') as f:
            f.write(generate_key(enc_key_p, iv) + b'\n')

        loading_database(win)
        win.show()
        current.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = PasswordGenerator()

    if os.path.isfile('data.bin'):
        login = LoginWindow()
        login.show()
    else:
        signup = SignupWindow()
        signup.show()

    sys.exit(app.exec_())
