# Problem 1
    Çok fazla if-else kullanılmış. Algoritma seçiminin if-else ile yapılması hem algoritmayı hem de okumayı zorlaştırıyor. (Spagetti)

# Promblem 2
    Yeni bir şifreleme algoritması eklemek istediğimde bunun if-else içine eklemem lazım. Kodun sürekli olarak değişmesine ve şişmesine yol açar. (OCP ihlali)

# Problem 3
    Tüm kod tek bir sınıf içerisine yazılmış. Tek görevli bir sınıf değil. (SRP ihlali)

# Problem 4
    Algoritma seçimi kurucu methodda kodlanmış. Çalıştırırken seçmek mümkün değil. (OCP ihlali)

# Problem 5
    Kod içerisinde interface ve polymorfizm kullanılmamıştır. Algoritmalar nesne yönelimli bir yapı yerine if-else bloklarıyla kontrol edilmektedir. (polymorfizm eksikliği)


# Önerilen prompt ile kaynak dosyasındaki kod yapay zeka araçlarına gönderilerek aşağıdaki çıktılar alınmıştır: 

# PROMPT:
    "Bu kodda hangi tasarım sorunlarını görüyorsun? Tüm sorunları yaz. Hangi tasarım örüntüleri bu sorunları çözebilir? Her sorun için kısa bir açıklama yaz."


# CHAT-GPT:
Bu kodda hem tasarımsal, hem de güvenlik, hem de bakım/ölçeklenebilirlik açısından birçok problem var. Özellikle “tek sınıfta her şeyi toplama” yaklaşımı ciddi bir anti-pattern oluşturuyor.

⭐ Tasarım Sorunları ve Çözüm Örüntüleri
## ⭐ 1. SRP (Single Responsibility Principle) İhlali

Kodun tek bir sınıf içinde:

AES işlemleri
RSA işlemleri
Base64 işlemleri
Anahtar yönetimi
Algoritma seçimi
Şifreleme
Çözme

gibi birçok farklı sorumluluğu var.

Bu sınıfın değişmesi için birden fazla sebep oluşuyor.

❌ Problem

SifrelemeAraci aşırı büyümüş ve “God Class” haline gelmiş.

✅ Çözüm Örüntüsü
Strategy Pattern
Factory Pattern

Her algoritma ayrı sınıfa ayrılmalı:

class AESSifreleme:
class RSASifreleme:
class Base64Kodlayici:
## ⭐ 2. Open/Closed Principle İhlali

Yeni algoritma eklemek için:

if self.algoritma == ...

bloklarını değiştirmek gerekiyor.

❌ Problem

Kod genişlemeye kapalı değil.

Örneğin yeni:

ChaCha20
DES
Blowfish

eklemek için mevcut kod değiştirilmek zorunda.

✅ Çözüm Örüntüsü
Strategy Pattern
Factory Method

Yeni algoritma sadece yeni sınıf eklenerek sisteme dahil olmalı.

## ⭐ 3. Büyük If-Else Zinciri (Conditional Complexity)

Kod sürekli:

if algoritma == ...
elif ...

şeklinde çalışıyor.

❌ Problem

Bu yaklaşım:

okunabilirliği düşürür
hata riskini artırır
bakım maliyetini yükseltir
✅ Çözüm Örüntüsü
Polymorphism
Strategy Pattern

Örneğin:

aktif_algoritma.sifrele(veri)

şeklinde çalışmalı.

## ⭐ 4. Sıkı Bağımlılık (Tight Coupling)

SifrelemeAraci, tüm algoritmaları doğrudan biliyor.

❌ Problem

Sınıflar birbirine aşırı bağımlı.

Bir algoritmadaki değişiklik ana sistemi etkileyebilir.

✅ Çözüm Örüntüsü
Dependency Injection
Strategy Pattern

Algoritmalar dışarıdan verilmelidir.

SifrelemeAraci(AESSifreleme())
## ⭐ 5. Algoritmanın Constructor İçinde Sabitlenmesi
self.algoritma = "AES"
❌ Problem

Runtime sırasında algoritma değiştirilemiyor.

Esnek değil.

✅ Çözüm Örüntüsü
Strategy Pattern
Dependency Injection
SifrelemeAraci(strategy)
## ⭐ 6. Primitive Obsession

Algoritmalar string ile temsil ediliyor:

"AES"
"RSA"
❌ Problem

Yazım hatalarına açık.

"Ase"
"aes"

gibi problemler oluşabilir.

✅ Çözüm Örüntüsü
Enum
Factory Pattern
class Algoritma(Enum):
    AES = 1
## ⭐ 7. Kod Tekrarı (Duplication)

Şifreleme ve çözme tarafında aynı kontrol yapıları tekrar ediyor.

❌ Problem

Aynı mantık iki kez yazılmış.

✅ Çözüm Örüntüsü
Template Method
Strategy Pattern
## ⭐ 8. God Object / Blob Anti-Pattern

Sınıf:

veri yönetiyor
anahtar üretiyor
algoritma seçiyor
encode/decode yapıyor
❌ Problem

Aşırı merkezi yapı oluşmuş.

✅ Çözüm Örüntüsü
Facade Pattern (yüksek seviye arayüz)
Alt tarafta küçük servis sınıfları
## ⭐ 9. Güvenlik ve İş Mantığının Karışması

Kod içinde hem:

güvenlik mantığı
iş mantığı
veri dönüşümü

aynı yerde.

❌ Problem

Katmanlı mimari yok.

✅ Çözüm Örüntüsü
Layered Architecture
Service Pattern
## ⭐ 10. Sabit AES Anahtarı Kullanılması
self.aes_key = b"1234567890123456"
❌ Problem

Çok ciddi güvenlik açığı.

Anahtar source code içine gömülmüş.

✅ Çözüm Örüntüsü
Configuration Pattern
Secrets Management

Anahtar dışarıdan alınmalı:

environment variable
config
vault
## ⭐ 11. RSA Anahtarlarının Constructor’da Oluşturulması
RSA.generate(2048)
❌ Problem

Her nesne oluştuğunda yeni anahtar oluşuyor.

Performans problemi yaratır.

✅ Çözüm Örüntüsü
Singleton
Factory
Key Management Service
## ⭐ 12. Base64’ün Şifreleme Gibi Sunulması

Base64 aslında encoding yöntemidir.

❌ Problem

Yanlış soyutlama yapılmış.

✅ Çözüm Örüntüsü
Ayrı interface:
Encoder
Encryptor
## ⭐ 13. Hata Yönetimi Zayıf
raise Exception(...)
❌ Problem

Genel exception kullanılıyor.

Özel hata türleri yok.

✅ Çözüm Örüntüsü
Custom Exception Pattern
class DesteklenmeyenAlgoritmaHatasi(Exception):
## ⭐ 14. Interface Eksikliği

Algoritmaların ortak bir sözleşmesi yok.

❌ Problem

Tüm sınıflar farklı davranabilir.

Standart garanti edilmiyor.

✅ Çözüm Örüntüsü
Strategy Interface
Abstract Base Class
class SifrelemeStrategy(ABC):
## ⭐ 15. Test Edilebilirliğin Düşük Olması

Her şey tek sınıfta olduğu için unit test zorlaşıyor.

❌ Problem

Mock kullanımı zor.

Bağımlılıklar ayrışmamış.

✅ Çözüm Örüntüsü
Dependency Injection
Interface Segregation
## ⭐ 16. AES/RSA/Base64 Aynı Soyutlama Altında Toplanmış

Aslında:

AES → simetrik şifreleme
RSA → asimetrik şifreleme
Base64 → encoding

aynı kategori değil.

❌ Problem

Yanlış abstraction.

✅ Çözüm Örüntüsü
Hierarchy Separation
Bridge Pattern
## ⭐ 17. Anahtar Yönetimi ile Algoritma Mantığının Karışması

RSA key üretimi algoritma sınıfının içinde.

❌ Problem

Key management ayrı bir sorumluluk olmalı.

✅ Çözüm Örüntüsü
Factory
Provider Pattern
## ⭐ 18. Magic Values Kullanımı
16
2048
"AES"
❌ Problem

Sabit değerlerin anlamı belirsiz.

✅ Çözüm Örüntüsü
Constants
Config Object
## ⭐ 19. Interface Segregation Principle İhlali

Base64 için gerçek anlamda:

coz()

şifre çözme değildir.

❌ Problem

Tüm algoritmalara aynı interface zorla uygulanmış.

✅ Çözüm Örüntüsü
Ayrı interface’ler:
Encryptor
Encoder
## ⭐ 20. Ölçeklenebilirlik Problemi

10+ algoritma olduğunda sınıf aşırı büyür.

❌ Problem

Bakımı imkansız hale gelir.

✅ Çözüm Örüntüsü
Plugin Architecture
Strategy + Factory
⭐ Kullanılabilecek En Uygun Tasarım Örüntüleri
Örüntü	Ne İçin Kullanılır
Strategy Pattern	Algoritmaları runtime’da değiştirmek
Factory Method	Algoritma nesnesi üretmek
Dependency Injection	Sıkı bağımlılığı azaltmak
Facade Pattern	Kullanıcıya sade API sunmak
Template Method	Ortak akışları merkezileştirmek
Singleton	Anahtar yöneticisi için
Bridge Pattern	Şifreleme türlerini ayırmak
Provider Pattern	Key management için
Abstract Factory	Algoritma aileleri üretmek
⭐ Bu Kodun En Büyük Tasarım Problemi

En büyük problem:

“Tüm algoritmaların tek sınıfta if-else ile yönetilmesi.”

Bu nedenle kod:

genişlemeye kapalı
sıkı bağlı
test edilmesi zor
bakım maliyeti yüksek
SOLID ihlalleri içeriyor

hale geliyor.

Bu yapı için en doğru temel çözüm:

✅ Strategy Pattern + Factory Pattern

kombinasyonudur.
