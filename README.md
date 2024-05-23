
# YOLOv8 Fruit Detection

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
3. Eğitim tamamlandığında, model dosyasını Google Drive'a kaydedin.

## Kullanım

### 1. Görüntü İndirme

İlk olarak, internetten meyve görüntülerini indirmek için aşağıdaki komutu çalıştırın:

```bash
python scripts/download_images.py
```

### 2. Model Eğitimi

Modeli eğitmek için `notebooks/training.ipynb` dosyasını kullanın. Google Colab üzerinde çalıştırarak modeli eğitebilirsiniz. Eğitim tamamlandıktan sonra model ağırlıklarını `models/best_model.pt` dosyasına kaydedin.

### 3. Tahmin ve Sonuç Görüntüleme

Eğitimli modeli kullanarak tahmin yapmak ve sonuçları görüntülemek için:

```bash
python scripts/app.py
```

Bu komut, bir grafiksel kullanıcı arayüzü (GUI) açarak görüntü seçmenizi ve modelin tahmin sonuçlarını ayrı bir pencerede görmenizi sağlar.

## Dosya ve Klasör Açıklamaları

- **data/**: Veri seti klasörü. İçinde meyve resimleri bulunur.
- **models/**: Eğitimli modellerin saklandığı klasör.
- **notebooks/**: Jupyter notebook dosyaları. Eğitim ve değerlendirme işlemlerini içeren dosyalar.
- **scripts/**: Python script dosyaları. Görüntü indirme ve GUI uygulama dosyaları.
- **runs/**: Eğitim sırasında oluşturulan geçici dosyalar.
- **README.md**: Proje hakkında genel bilgi, kurulum ve kullanım talimatları.
- **requirements.txt**: Proje bağımlılıklarını içeren dosya.

## Sonuçlar



