# Python202 Proje: Kitap Yönetim Sistemi

Bu proje, Python OOP mantığını ve API geliştirmeyi öğrenmek için hazırlanmış bir projedir.  
Proje üç aşamadan oluşmaktadır:  
1. Terminal uygulaması (kitap ekleme, listeleme, silme vb.)  
2. OOP (Sınıflar ve nesneler kullanılarak proje yapılandırması)  
3. FastAPI ile REST API geliştirme  

---

## Kurulum:

### 1. Depoyu Klonla
```bash
git clone https://github.com/serracabaz34/python202-proje.git
cd python202-proje

### Sanal Ortam (Opsiyonel)
python -m venv venv
venv\Scripts\activate   # Windows için

## Bağımlılıkları Kur:
pip install -r requirements.txt

### Aşama 1-2 Terminal Uygulaması:
python main.py

### Aşama 3: API Sunucusu
uvicorn api:app --reload
Daha sonra tarayıcıdan http://127.0.0.1:8000/docs şu adrese giderek API dokümantasyonuna ulaşabilirsin.

### API Dokümantasyonu
GET /books → Tüm kitapları listeler
POST /books → Yeni kitap ekler
Body (JSON örnek):

{
  "isbn": "123456789",
  "title": "Python Öğreniyorum",
  "author": "Serra Cabaz"
}

DELETE /books/{isbn} → ISBN numarasına göre kitap siler

### Test Senaryoları:
Terminal uygulamasında kitap ekle → ardından listele → eklenen kitabı gör.
Aynı işlemleri API üzerinden yap → POST ile kitap ekle, GET ile doğrula.
Var olmayan bir ISBN silmeye çalış → hata mesajı döndüğünü gör.
