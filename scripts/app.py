import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from ultralytics import YOLO
import numpy as np
import cv2

# Modeli yükleyin
model = YOLO('models/best.pt')

# Tkinter uygulamasını başlat
root = tk.Tk()
root.title("YOLOv8 Görüntü Tanıma")
root.geometry("800x600")

# Görüntü etiketi
image_label = tk.Label(root)
image_label.pack()

# Doğruluk seviyesi etiketi
confidence_value_label = tk.Label(root, text="Doğruluk Seviyesi: 50%", font=("Helvetica", 14))
confidence_value_label.pack()

# Görüntü seçme fonksiyonu
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))  # Görüntüyü yeniden boyutlandır
        img = ImageTk.PhotoImage(image)
        image_label.configure(image=img)
        image_label.image = img
        process_image(file_path)

# Görüntü işleme ve tahmin yapma fonksiyonu
def process_image(file_path):
    confidence = confidence_scale.get() / 100
    results = model.predict(source=file_path, conf=confidence)
    
    # İlk sonucu al
    result = results[0]
    
    # Sonuçları numpy array olarak alın
    result_image = result.plot(show=False)
    
    # OpenCV ile görüntüyü tkinter'da gösterilecek şekilde yeniden boyutlandırın
    img = cv2.cvtColor(np.array(result_image), cv2.COLOR_RGB2BGR)
    img = Image.fromarray(img)
    img = img.resize((800, 600), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    
    show_result_window(img_tk)

# Doğruluk seviyesini güncelleme fonksiyonu
def update_confidence_label(value):
    confidence_value_label.config(text=f"Doğruluk Seviyesi: {int(float(value))}%")

# Sonuçları ayrı pencerede gösterme fonksiyonu
def show_result_window(img_tk):
    result_window = tk.Toplevel(root)
    result_window.title("Tahmin Sonuçları")
    result_window.geometry("800x600")
    
    result_canvas = tk.Canvas(result_window, width=800, height=600)
    result_canvas.pack()
    
    result_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    result_canvas.image = img_tk

# Görüntü seçme butonu
select_button = tk.Button(root, text="Görüntü Seç", command=select_image)
select_button.pack(pady=10)

# Doğruluk seviyesi kaydırıcısı
confidence_label = tk.Label(root, text="Doğruluk Seviyesi:")
confidence_label.pack()

confidence_scale = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_confidence_label)
confidence_scale.set(50)  # Başlangıç değeri
confidence_scale.pack(pady=10)

# Uygulamayı çalıştır
root.mainloop()
