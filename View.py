from PyQt5.QtWidgets import (QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, 
                             QSlider, QLineEdit, QComboBox)
from PyQt5.QtCore import Qt

class View():
  def initUI(self, MainWindow):
        MainWindow.setWindowTitle('Image Processing Application')
        MainWindow.setGeometry(100, 100, 800, 600)
        
        self.image_label = QLabel(self)
        
        self.load_button = QPushButton('Load Image', self)
        self.load_button.clicked.connect(self.load_image)
        
        self.camera_button = QPushButton('Capture Image', self)
        self.camera_button.clicked.connect(self.capture_image)
        
        self.channel_combo = QComboBox(self)
        self.channel_combo.addItems(['Red', 'Green', 'Blue'])
        self.channel_combo.currentIndexChanged.connect(self.show_channel)
        
        self.resize_button = QPushButton('Resize Image', self)
        self.resize_button.clicked.connect(self.resize_image)
        self.resize_width_input = QLineEdit(self)
        self.resize_width_input.setPlaceholderText('Width')
        self.resize_height_input = QLineEdit(self)
        self.resize_height_input.setPlaceholderText('Height')
        
        self.circle_button = QPushButton('Draw Circle', self)
        self.circle_button.clicked.connect(self.draw_circle)
        self.circle_x_input = QLineEdit(self)
        self.circle_x_input.setPlaceholderText('X')
        self.circle_y_input = QLineEdit(self)
        self.circle_y_input.setPlaceholderText('Y')
        self.circle_radius_input = QLineEdit(self)
        self.circle_radius_input.setPlaceholderText('Radius')
        
        self.brightness_slider = QSlider(Qt.Horizontal, self)
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.setTickInterval(10)
        self.brightness_slider.setTickPosition(QSlider.TicksBelow)
        self.brightness_slider.valueChanged.connect(self.change_brightness)
        
        self.image = None
        self.modified_image = None
        
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.camera_button)
        layout.addWidget(self.channel_combo)
        
        resize_layout = QHBoxLayout()
        resize_layout.addWidget(self.resize_width_input)
        resize_layout.addWidget(self.resize_height_input)
        resize_layout.addWidget(self.resize_button)
        layout.addLayout(resize_layout)
        
        circle_layout = QHBoxLayout()
        circle_layout.addWidget(self.circle_x_input)
        circle_layout.addWidget(self.circle_y_input)
        circle_layout.addWidget(self.circle_radius_input)
        circle_layout.addWidget(self.circle_button)
        layout.addLayout(circle_layout)
        
        layout.addWidget(self.brightness_slider)
        layout.addWidget(self.image_label)
        
        container = QWidget()
        container.setLayout(layout)
        MainWindow.setCentralWidget(container)
