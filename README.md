# Python202 Proje
# Python202 Proje: Kitap Yönetim Sistemi

# İçindekiler
Genel Bilgi

Kullanım

Bölümler
Bölüm 1: JSON Dosya İşlemleri
Bölüm 2: OOP ve Kitaplık Sistemi
Bölüm 3: FastAPI ile REST API

Kurulum

Testler

Gelecek Geliştirmeler

# Genel Bilgi
Bu proje, bir kitaplık uygulaması örneği üzerinden farklı Python kavramlarını öğretmek amacıyla üç aşamada tasarlanmıştır.
Her bölüm bir önceki üzerine inşa edilmiştir:

Bölüm 1 – Temel dosya okuma/yazma ve JSON işlemleri

Bölüm 2 – Nesne yönelimli programlama ile kitap sınıfı ve kitaplık yönetimi

Bölüm 3 – Web API (FastAPI) ile kitapların internet üzerinden yönetilmesi

# Kullanım
Gerekli kütüphaneleri yüklemek için:

pip install -r requirements.txt

# Bölümler:

# Bölüm 1: JSON Dosya İşlemleri
Dosya: bolum1/

Öğrenilenler:
Python’da JSON dosyalarını okuma ve yazma

Basit veri ekleme/silme

Bir kitaplık verisinin library.json dosyasında saklanması

Bu bölümde temel amaç, verilerin dosyada nasıl tutulduğunu öğrenmek.

# Bölüm 2: OOP ve Kitaplık Sistemi
Dosya: bolum2/

Öğrenilenler:
OOP (Nesne Yönelimli Programlama) yapıları

Book sınıfı: ISBN, kitap adı, yazar bilgilerini tutar

Library sınıfı: Kitap ekleme, silme, arama gibi işlemleri yapar

Bu bölümde amaç, gerçek hayattaki bir kitaplık sistemini kod ile modellemek.

# Bölüm 3: FastAPI ile REST API
Dosya: bolum3/

Öğrenilenler:
FastAPI framework kullanarak REST API geliştirme

Endpointler:
POST /books → Yeni kitap ekler (ISBN üzerinden)

GET /books → Tüm kitapları listeler

DELETE /books/{isbn} → ISBN’e göre kitap siler

Pytest ile API testleri yazma

Bu bölümde amaç, kitaplık sistemini artık bir web servisi haline getirip dışarıya açmak.

# Kurulum
Projeyi klonladıktan sonra:
git clone https://github.com/serracabaz34/python202-proje.git

cd python202-proje

Sanal ortam oluşturma (opsiyonel):
python -m venv .venv

.venv\Scripts\activate  # Windows için

source .venv/bin/activate  # Mac/Linux için

Gereksinimleri yükleme:
pip install fastapi uvicorn pytest requests

# Testler

Projede testler pytest ile yazılmıştır.

Çalıştırmak için:
pytest -q

Testler:
API’ye kitap ekleme

API’den kitapları listeleme

Kitap silme işlemleri

# Gelecek Geliştirmeler
Kitaplara kategori eklenmesi

Verilerin JSON yerine SQLite veritabanında saklanması

Kullanıcı giriş sistemi eklenmesi

Frontend (React / Vue) ile basit bir arayüz

# Not: Bu proje, Python öğrenimini desteklemek amacıyla hazırlanmış olup gerçek bir kitaplık sistemi için temel bir iskelet sunmaktadır.



