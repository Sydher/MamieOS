#!/usr/bin/env python3

import sys, random, json
from datetime import datetime, timedelta
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont, QPixmap, QColor, QPainter

CONFIG_DIR = Path.home() / ".config" / "antivirus"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
SAVE_FILE = CONFIG_DIR / "last_scan.json"

MIN_DURATION = 8000
MAX_DURATION = 20000

class Nettoyeur(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analyse Antivirus - PC NoVirusOrMalware")
        self.resize(500, 400)

        layout = QVBoxLayout(self)

        # Charger date
        self.last_clean = self.load_last_clean()
        self.label_date = QLabel(f"Dernier scan : {self.last_clean.strftime('%d/%m/%Y %H:%M')}")
        self.label_date.setFont(QFont("Arial", 22))
        layout.addWidget(self.label_date, alignment=Qt.AlignmentFlag.AlignCenter)

        # Bouton
        self.btn = QPushButton("Scanner l'ordinateur")
        self.btn.setStyleSheet("background-color:#2196F3; color:white; font-size:22px; padding:15px;")
        self.btn.clicked.connect(self.start_clean)
        layout.addWidget(self.btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # Progression
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        self.progress.setFixedHeight(40)
        layout.addWidget(self.progress)

        # Résultat
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Coche verte agrandie
        self.check_label = QLabel()
        self.check_label.setVisible(False)
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setPen(QColor("green"))
        painter.setBrush(Qt.GlobalColor.green)
        painter.drawEllipse(0, 0, 100, 100)
        painter.setPen(Qt.GlobalColor.white)
        painter.setFont(QFont("Arial", 50, QFont.Weight.Bold))
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "✓")
        painter.end()
        self.check_label.setPixmap(pixmap)
        layout.addWidget(self.check_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Timer
        self.timer, self.interval, self.elapsed = QTimer(), 100, 0
        self.timer.timeout.connect(self.update_progress)

    def load_last_clean(self):
        if SAVE_FILE.exists():
            try:
                data = json.loads(SAVE_FILE.read_text())
                return datetime.fromisoformat(data["last_scan"])
            except Exception:
                pass
        return datetime.now() - timedelta(days=1)

    def save_last_clean(self):
        SAVE_FILE.write_text(json.dumps({"last_scan": self.last_clean.isoformat()}))

    def start_clean(self):
        self.duration = random.randint(MIN_DURATION, MAX_DURATION)
        self.progress.setVisible(True)
        self.progress.setValue(0)
        self.result_label.setText("")
        self.check_label.setVisible(False)
        self.btn.setEnabled(False)
        self.elapsed = 0
        self.timer.start(self.interval)

    def update_progress(self):
        self.elapsed += self.interval
        self.progress.setValue(int((self.elapsed / self.duration) * 100))
        if self.elapsed >= self.duration:
            self.timer.stop()
            self.progress.setVisible(False)
            self.check_label.setVisible(True)
            self.last_clean = datetime.now()
            self.label_date.setText(f"Dernier scan : {self.last_clean.strftime('%d/%m/%Y %H:%M')}")
            self.save_last_clean()
            z = self.duration / 1000
            self.result_label.setText(f"{0} virus ou logiciels malveillant repéré sur cet ordinateur\nVotre ordinateur ne risque rien !\n\nPC analysé en {z} secondes")
            self.btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Nettoyeur()
    win.show()
    sys.exit(app.exec())
