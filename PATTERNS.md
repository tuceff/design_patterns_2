# Phase-1
    Bu fazda kodun daha esnek, sürdürülebilir ve genişletilebilir hale gelmesi için factory method ve singleton tasasrım örüntüleri uygulanmıştır.

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


# Phase-2
    Bu fazda sistemin genişletilebilirliğini artırmak ve kullanıcıya daha sade bir kullanım sunmak için Decorator ve Facade tasarım örüntüleri uygulanmıştır.

## Decorator Pattern

### Nerede kullanıldı?
    Decorator pattern log_decorator.py ve sure_decorator.py sınıflarında şifreleme ve çözme işlemlerine loglama ve süre ölçümü eklemek için kullanıldı.

### Neden kullanıldı?
    Mevcut şifreleyici sınıflar değiştirilmeden yeni davranışlar eklenmek istendi. Eğer doğrudan sınıflar içine log veya süre ölçümü eklenmiş olsaydı, kodun sorumluluğu artacak ve SRP ihlal edilecekti. Ayrıca her yeni özellik için sınıf yapısının değiştirilmesi gerekecekti. Decorator sayesinde davranışlar dinamik olarak eklenebilir hale geldi.

### Ne Kazandırdı?
    Kod değiştirilmeden yeni özellik eklenebilir hale geldi, sistem daha modüler oldu, SRP korundu ve OCP güçlendirildi. Ayrıca loglama ve performans ölçümü bağımsız hale getirildi.

## Facade Pattern

### Nerede kullanıldı?
    Facade pattern sifreleme_fascade.py sınıfında factory ve decorator yapılarının karmaşıklığını gizleyerek tek bir arayüz üzerinden sistemin kullanılmasını sağlamak için kullanıldı.

### Neden kullanıldı?
    Factory, decorator ve şifreleyici sınıflar birlikte kullanıldığında main dosyasında karmaşık bir yapı oluşuyordu. Kullanıcıdan bu karmaşıklığı gizlemek ve sistemi daha kolay kullanılabilir hale getirmek için Facade yapısı oluşturuldu.

### Ne Kazandırdı?
    Kullanım kolaylığı sağlandı, sistem tek bir sınıf üzerinden kontrol edilebilir hale geldi, bağımlılıklar azaldı ve kod okunabilirliği arttı. Kullanıcı artık alt sistemleri bilmeden şifreleme işlemini gerçekleştirebilir hale geldi.