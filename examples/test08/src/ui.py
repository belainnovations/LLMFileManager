import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from .qr_generator import generate_qr_code
from .data_validator import validate_input
from .image_utils import save_qr_code
from PIL.ImageQt import ImageQt

class QRCodeGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 400, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.data_input = QLineEdit()
        self.data_input.setPlaceholderText("Enter data for QR code")
        layout.addWidget(self.data_input)

        self.error_correction_combo = QComboBox()
        self.error_correction_combo.addItems(["Low", "Medium", "Quartile", "High"])
        layout.addWidget(QLabel("Error Correction:"))
        layout.addWidget(self.error_correction_combo)

        self.box_size_input = QLineEdit()
        self.box_size_input.setPlaceholderText("Box size (default: 10)")
        layout.addWidget(QLabel("Box Size:"))
        layout.addWidget(self.box_size_input)

        self.border_input = QLineEdit()
        self.border_input.setPlaceholderText("Border size (default: 4)")
        layout.addWidget(QLabel("Border Size:"))
        layout.addWidget(self.border_input)

        generate_button = QPushButton("Generate QR Code")
        generate_button.clicked.connect(self.generate_qr)
        layout.addWidget(generate_button)

        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.qr_label)

        save_button = QPushButton("Save QR Code")
        save_button.clicked.connect(self.save_qr)
        layout.addWidget(save_button)

    def generate_qr(self):
        try:
            data = self.data_input.text()
            if validate_input(data):
                error_correction = self.error_correction_combo.currentText()
                box_size = int(self.box_size_input.text() or 10)
                border = int(self.border_input.text() or 4)

                qr_image = generate_qr_code(data, error_correction, box_size, border)
                qimage = ImageQt(qr_image)
                pixmap = QPixmap.fromImage(qimage)
                self.qr_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
            else:
                self.qr_label.setText("Invalid input. Please try again.")
        except Exception as e:
            self.qr_label.setText(f"Error: {str(e)}")
            print(f"Error generating QR code: {str(e)}")

    def save_qr(self):
        if self.qr_label.pixmap():
            file_name, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png)")
            if file_name:
                self.qr_label.pixmap().save(file_name)

def run_ui():
    app = QApplication(sys.argv)
    window = QRCodeGeneratorUI()
    window.show()
    sys.exit(app.exec())
