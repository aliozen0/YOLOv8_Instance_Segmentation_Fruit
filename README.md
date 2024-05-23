
# YOLOv8 Fruit Instance Segmentation

Bu proje, YOLOv8 kullanarak meyve tespiti yapmayı amaçlar. Proje kapsamında mango, kivi ve portakal gibi meyvelerin görüntüleri kullanılmıştır. Bu proje, veri indirme, model eğitimi ve tahmin yapma gibi adımları içermektedir.

## Proje Yapısı

```
yolov8_fruit_detection/
├── data/
│   ├── test/
│   │   └── ...  
│   │   
│   ├── train/
│   │   └── ...
|   |
│   |── valid/
│   |    └── ...
|   |
|   └── data.yaml/
│       
├── models/
│   ├── best_model.pt
│   └── ...
├── notebooks/
│   ├── model_training.ipynb
│   └── ...
├── scripts/
│   ├── data_scraping.py
│   └── app.py
|
├── runs/
│   ├── segment/
│   │   ├── train/
│   │   └── ...
|
├── README.md
└── requirements.txt
```

## Kurulum

### Gerekli Kütüphanelerin Kurulumu

Proje için gerekli olan tüm bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt
```

### Google Colab Kullanımı

Eğer modeli Google Colab üzerinde eğitmek isterseniz, aşağıdaki adımları takip edebilirsiniz:

1. Google Colab'e gidin.
2. `notebooks/model_training.ipynb` dosyasını yükleyin ve çalıştırın.
3. '/data' klasörü ile modele etiketlenmiş veriler ile eğitin. 
4. Eğitim tamamlandığında, model dosyasını Google Drive'a kaydedin.

## Kullanım

### 1. Görüntü İndirme

İlk olarak, internetten meyve görüntülerini indirmek için aşağıdaki komutu çalıştırın:

Not: Verileri etiketlemek için roboflow.com kullanılabilir.

```bash
python scripts/data_scraping.py
```

### 2. Model Eğitimi

Modeli eğitmek için `notebooks/model_training.ipynb` dosyasını kullanın. Google Colab üzerinde çalıştırarak '/data' klasöründeki etiketlenmiş veriler ile modeli eğitebilirsiniz. Eğitim tamamlandıktan sonra model ağırlıklarını `models/best.pt` dosyasına kaydedin.

### 3. Tahmin ve Sonuç Görüntüleme

Tkinter kütüphanesi kullanılarak oluşturulmuş arayüz uygulması ile eğitimli modeli kullanarak tahmin yapmak ve sonuçları görüntülemek için :

```bash
python scripts/app.py
```

Bu komut, bir grafiksel kullanıcı arayüzü (GUI) açarak görüntü seçmenizi ve modelin tahmin sonuçlarını ayrı bir pencerede görmenizi sağlar.
![image](https://github.com/aliozen0/YOLOv8_Instance_Segmentation_Fruit/assets/113714644/d125046e-3843-4a5e-9875-e0227002d366)

## Dosya ve Klasör Açıklamaları

- **data/**: Veri seti klasörü. İçinde meyve resimleri bulunur.
- **models/**: Eğitimli modellerin saklandığı klasör.
- **notebooks/**: Jupyter notebook dosyaları. Eğitim ve değerlendirme işlemlerini içeren dosyalar.
- **scripts/**: Python script dosyaları. Görüntü indirme ve GUI uygulama dosyaları.
- **runs/**: Eğitim sırasında oluşturulan geçici dosyalar.
- **README.md**: Proje hakkında genel bilgi, kurulum ve kullanım talimatları.
- **requirements.txt**: Proje bağımlılıklarını içeren dosya.

## Sonuçlar
Modelin eğitim sonucunda alınan değerler aşağıda bulunmaktadır.

Precision: 0.8388792404906095

Recall: 0.7654271224458425

F1-Score (mAP50-95): 0.7169014069637037


