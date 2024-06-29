import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow,
               QFileDialog, QMessageBox)
from PyQt5.QtGui import QImage, QPixmap
from View import View

class ImageApp(QMainWindow, View):
  def __init__(self):
    super().__init__()
    
    self.initUI(self)
    self.image = None
    self.modified_image = None
    
    
  def load_image(self):
    file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 
                           'Images (*.png *.jpg *.jpeg)')
    if file_name:
      self.image = cv2.imread(file_name)
      if self.image is None:
        QMessageBox.critical(self, 'Error', 'Failed to load image.')
      else:
        self.modified_image = self.image.copy()
        self.display_image(self.image)
        
  def capture_image(self):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
      QMessageBox.critical(self, 'Error', 'Failed to open webcam.')
      return
    ret, frame = cap.read()
    cap.release()
    if ret:
      self.image = frame
      self.modified_image = self.image.copy()
      self.display_image(self.image)
    else:
      QMessageBox.critical(self, 'Error', 'Failed to capture image.')
  
  def display_image(self, image):
    qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, ch = image.shape
    bytes_per_line = ch * w
    qimage = QImage(image.data, w, h, bytes_per_line, qformat)
    pixmap = QPixmap.fromImage(qimage)
    self.image_label.setPixmap(pixmap)
    
  def show_channel(self, **args):
    if self.image is None:
      QMessageBox.critical(self, 'Error', 'The image was not found')
      return
    channel = self.channel_combo.currentIndex()
    if "image" in args:
      channels = cv2.split(args["image"])
    else:
      channels = cv2.split(self.modified_image)
    zeros = np.zeros_like(channels[0])
    if channel == 0:
      merged = cv2.merge([zeros, zeros, channels[2]])
    elif channel == 1:
      merged = cv2.merge([zeros, channels[1], zeros])
    else:
      merged = cv2.merge([channels[0], zeros, zeros])
    self.display_image(merged)
    
  def resize_image(self):
    if self.image is None:
      QMessageBox.critical(self, 'Error', 'The image was not found')
      return
    if self.modified_image is None:
      self.modified_image = self.image.copy()
    try:
      width = int(self.resize_width_input.text())
      height = int(self.resize_height_input.text())
      if(width <= 0 or height <= 0):
        QMessageBox.critical(self, 'Error', 'Invalid width or height.')
      else:
        self.modified_image = cv2.resize(self.modified_image, (width, height))
        self.display_image(self.modified_image)
        self.change_brightness()
    except ValueError:
      QMessageBox.critical(self, 'Error', 'Invalid width or height.')
      
  def draw_circle(self):
    if self.image is None:
      QMessageBox.critical(self, 'Error', 'The image was not found')
      return
    
    if self.modified_image is None:
      self.modified_image = self.image.copy()
    try:
      x = int(self.circle_x_input.text())
      y = int(self.circle_y_input.text())
      radius = int(self.circle_radius_input.text())
      cv2.circle(self.modified_image, (x, y), radius, (0, 0, 255), 2)
      self.display_image(self.modified_image)
      self.change_brightness()
    except ValueError:
      QMessageBox.critical(self, 'Error', 'Invalid coordinates or radius.')
      
  def change_brightness(self):
    if self.image is None:
      QMessageBox.critical(self, 'Error', 'The image was not found')
      return
    if self.modified_image is None:
      self.modified_image = self.image.copy()
    brightness = self.brightness_slider.value()
    tempImage = cv2.convertScaleAbs(self.modified_image, alpha=1, beta=brightness)
    self.show_channel(image = tempImage)

def main():
  app = QApplication(sys.argv)
  ex = ImageApp()
  ex.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()