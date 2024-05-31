import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import cv2
import numpy as np

# Modeli yükleyin
model = YOLO('models/b.pt')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retinopati Hasta Takip Ekranı")
        self.setGeometry(100, 100, 1200, 800)

        # Ana düzeni oluştur
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QHBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)

        # Sol taraftaki düğmeler
        self.leftLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.btn_select_patient = QPushButton("Hasta Seç", self)
        self.btn_add_patient = QPushButton("Hasta Ekle", self)
        self.btn_patient_details = QPushButton("Hasta Detayı", self)
        self.btn_past_images = QPushButton("Geçmiş Görüntüler", self)
        self.btn_select_image = QPushButton("Görüntüyü Seç", self)
        self.btn_select_image.clicked.connect(self.select_image)
        self.leftLayout.addWidget(self.btn_select_patient)
        self.leftLayout.addWidget(self.btn_add_patient)
        self.leftLayout.addWidget(self.btn_patient_details)
        self.leftLayout.addWidget(self.btn_past_images)
        self.leftLayout.addWidget(self.btn_select_image)

        # Orta kısımdaki görüntü
        self.imageLabel = QLabel(self)
        self.mainLayout.addWidget(self.imageLabel)

        # Sağ taraftaki hasta bilgisi ve raporlama
        self.rightLayout = QVBoxLayout()
        self.patient_info = QLabel("Hasta Bilgisi", self)
        self.patient_info.setStyleSheet("background-color: gray; width: 200px; height: 100px")
        self.report_text = QTextEdit(self)
        self.btn_diagnosis = QPushButton("Tanı Koy", self)
        self.rightLayout.addWidget(self.patient_info)
        self.rightLayout.addWidget(self.report_text)
        self.rightLayout.addWidget(self.btn_diagnosis)
        self.mainLayout.addLayout(self.rightLayout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Görüntüyü Seç", "", "Image files (*.jpg *.jpeg *.png)")
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        results = model.predict(source=file_path, conf=0.5)
        result = results[0]
        result_image = result.plot(show=False)
        img = cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = QPixmap.fromImage(convert_to_Qt_format)
        self.imageLabel.setPixmap(p.scaled(800, 600, Qt.KeepAspectRatio))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
