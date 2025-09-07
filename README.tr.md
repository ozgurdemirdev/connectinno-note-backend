# Connectinno Not Uygulaması Arka Ucu (Backend)

[English Version](README.md)

Bu, Connectinno Not Uygulaması için **FastAPI** kullanılarak geliştirilmiş bir arka uç (backend) hizmetidir.

## 🚀 Proje Özellikleri

* **Not Yönetimi:** Not oluşturma, okuma, güncelleme ve silme (CRUD) işlevleri sunar.
* **Firebase Kimlik Doğrulama:** Tüm API uç noktaları, Firebase ID belirteçleri (token) kullanılarak güvenli hale getirilmiştir.
* **Kolay Kurulum:** Minimum kurulum adımlarıyla hızlı bir şekilde ayağa kalkabilir.
* **API Belgeleri:** Otomatik olarak oluşturulan interaktif API belgeleri (`/docs`) sayesinde geliştiricilerin işini kolaylaştırır.

---

## 🛠️ Kullanılan Teknolojiler

* **FastAPI:** Yüksek performanslı ve kullanımı kolay bir Python web çatısı.
* **Firebase Admin SDK:** Kullanıcı kimlik belirteçlerini doğrulamak ve Firestore veritabanına erişmek için.
* **Uvicorn:** Asenkron sunucu olarak.
* **Python Decouple:** Ortam değişkenlerini yönetmek için.

---

## 🏁 Başlangıç

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin.

### Firebase Kurulumu

Bu arka uç, Firebase Firestore ve Firebase Kimlik Doğrulama hizmetlerini kullanır.

1.  **Firebase Projesi:** [Firebase Console](https://console.firebase.google.com/) adresine gidin ve yeni bir proje oluşturun.
2.  **Hizmet Hesabı:** Proje Ayarları → Hizmet Hesapları (Service Accounts) bölümüne gidin ve "Yeni özel anahtar oluştur" (Generate new private key) seçeneğine tıklayın.
3.  **Anahtar Dosyası:** İndirilen JSON dosyasını projenin `app/` dizinine **`firebase_key.json`** adıyla kaydedin.
4.  **Kimlik Doğrulama:** Firebase Console'da **Authentication** bölümüne gidin ve **E-posta/Şifre** ile giriş yapmayı etkinleştirin.
5.  **Veritabanı:** Firestore Veritabanı oluşturun ve geliştirme için "test modunda" başlatın.

### Proje Kurulumu

1.  Proje dizininde bir sanal ortam oluşturun ve etkinleştirin:
 ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
```
2.  Gerekli Python paketlerini kurun:
```bash
    pip install -r requirements.txt
```
3.  **Ortam Değişkenleri:** `.env.example` dosyasını `**`.env`**` olarak yeniden adlandırın ve Firebase anahtar dosyasının yolunu aşağıdaki gibi güncelleyin:
```
    FIREBASE_CREDENTIALS_JSON=app/firebase_key.json
```

---

## API Documentation

- Swagger UI is accessible at `/docs`.
- There is no Authorization button; when calling the endpoints, you must include the header: Authorization: Bearer <ID token>

## ▶️ Sunucuyu Çalıştırma

```bash
uvicorn app.main:app --reload
```

⚠️ **Swager UI İçin Test Notu**

- The `/test/create_user` and `/test/signin` endpoints are **for testing purposes only**.
- These endpoints are provided to create test users without a frontend.
- In the actual application, user registration, login, and logout are handled through the frontend.

## 📄 API Belgeleri ve Kimlik Doğrulama

API belgelerine, sunucu çalışırken `**/docs**` adresinden erişilebilir.

* **Swagger UI:** İnteraktif API belgeleri `**/docs**` adresinde bulunmaktadır.
* **Kimlik Doğrulama:** Güvenli uç noktalara erişim için, istek başlığında `Authorization: Bearer <ID token>` formatında bir token gönderilmesi gerekmektedir.

> **⚠️ ÖNEMLİ: Test Uç Noktaları**
>
> `**/test/create_user**` ve `**/test/signin**` uç noktaları **yalnızca test amaçlıdır**. Bu uç noktalar, ön uç (frontend) olmadan test kullanıcıları oluşturmak için sağlanmıştır. Üretim ortamında kullanıcı kaydı, oturum açma ve oturum kapatma işlemleri yalnızca ön uç uygulama üzerinden yapılmalıdır.