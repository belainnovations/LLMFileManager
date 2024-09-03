import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QFileDialog, QColorDialog, QSlider
from PyQt6.QtGui import QPixmap, QImage, QColor
from PyQt6.QtCore import Qt
from .qr_generator import generate_qr_code
from .data_validator import validate_input
from .image_utils import save_qr_code, rgba_to_hex
from PIL.ImageQt import ImageQt

class QRCodeGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 400, 600)

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

        # Color pickers
        self.fg_color = QColor(0, 0, 0, 255)
        self.bg_color = QColor(255, 255, 255, 255)

        fg_color_layout = QHBoxLayout()
        fg_color_layout.addWidget(QLabel("Foreground Color:"))
        self.fg_color_button = QPushButton()
        self.fg_color_button.setStyleSheet(f"background-color: {self.fg_color.name()}")
        self.fg_color_button.clicked.connect(lambda: self.pick_color('fg'))
        fg_color_layout.addWidget(self.fg_color_button)
        layout.addLayout(fg_color_layout)

        bg_color_layout = QHBoxLayout()
        bg_color_layout.addWidget(QLabel("Background Color:"))
        self.bg_color_button = QPushButton()
        self.bg_color_button.setStyleSheet(f"background-color: {self.bg_color.name()}")
        self.bg_color_button.clicked.connect(lambda: self.pick_color('bg'))
        bg_color_layout.addWidget(self.bg_color_button)
        layout.addLayout(bg_color_layout)

        # Transparency sliders
        self.fg_alpha_slider = QSlider(Qt.Orientation.Horizontal)
        self.fg_alpha_slider.setRange(0, 255)
        self.fg_alpha_slider.setValue(255)
        layout.addWidget(QLabel("Foreground Transparency:"))
        layout.addWidget(self.fg_alpha_slider)

        self.bg_alpha_slider = QSlider(Qt.Orientation.Horizontal)
        self.bg_alpha_slider.setRange(0, 255)
        self.bg_alpha_slider.setValue(255)
        layout.addWidget(QLabel("Background Transparency:"))
        layout.addWidget(self.bg_alpha_slider)

        generate_button = QPushButton("Generate QR Code")
        generate_button.clicked.connect(self.generate_qr)
        layout.addWidget(generate_button)

        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.qr_label)

        save_button = QPushButton("Save QR Code")
        save_button.clicked.connect(self.save_qr)
        layout.addWidget(save_button)

    def pick_color(self, color_type):
        color = QColorDialog.getColor()
        if color.isValid():
            if color_type == 'fg':
                self.fg_color = color
                self.fg_color_button.setStyleSheet(f"background-color: {color.name()}")
            else:
                self.bg_color = color
                self.bg_color_button.setStyleSheet(f"background-color: {color.name()}")

    def generate_qr(self):
        try:
            data = self.data_input.text()
            if validate_input(data):
                error_correction = self.error_correction_combo.currentText()
                box_size = int(self.box_size_input.text() or 10)
                border = int(self.border_input.text() or 4)

                fg_color = self.fg_color.getRgb()[:3] + (self.fg_alpha_slider.value(),)
                bg_color = self.bg_color.getRgb()[:3] + (self.bg_alpha_slider.value(),)

                qr_image = generate_qr_code(data, error_correction, box_size, border, fg_color, bg_color)
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
                image = self.qr_label.pixmap().toImage()
                image.save(file_name, "PNG")

def run_ui():
    app = QApplication(sys.argv)
    window = QRCodeGeneratorUI()
    window.show()
    sys.exit(app.exec())
