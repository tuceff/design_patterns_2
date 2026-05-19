# Phase-1
    Bu kodda kodun daha esnek, sürdürülebilir ve genişletilebilir hale gelmesi için factory method ve singleton tasasrım örüntüleri uygulanmıştır.

## Factory Method

### Nerede kullanıldı?
    Factory method SifrelemeFactory sınıfında AES, RSA ve BASE64 sifreleyicilerini merkezi bir yapı üzerinden oluşturmak içim kullanıldı.
### Neden kullanıldı?
    Eski yapıda algoritma seçimi if-elif ile yapılmaktaydı. Bu durum kod tekrarına, yüksek bağımlılığa, düşük genişletilebilirliğe neden olmaktaydı. Yeni algoritma eklemek için kodun değiştirilmesi gerekiyordu. Factory method sayesinde nesne oluşturma işlemi merkezi hale geldi.
### Ne Kazandırdı?
    Nesne oluşturma işlemi ayrıldı, kod daha esnek hale geldi, yeni algoritma eklemek kolaylaştı, OCP'ye daha uygun hale geldi.
    
## Singleton

### Nerede kullanıldı?
    Singleton RSAAnahtarYoneticisi sınıfında RSA anahtarının tek nesne olmasını sağlamak için kullanıldı.

### Neden kullanıldı?
    Eski yapıda her yeni nesne oluşturulduğunda RSA anahtarını yeniden üretiyordu. Bu durum gereksiz kaynak tüketimine, performans kaybına, tutarsuz anahtar yönetimine neden oluyordu. Singleton kullanılarak RSA anahtarları merkezi bir yapı üzerinden tek bir nesne olarak üretildi.

### Ne Kazandırdı?
    RSA anahtarları yalnızca bir kez üretildi, gereksiz nesne üretimi engellendi, performans iyileştirildi.