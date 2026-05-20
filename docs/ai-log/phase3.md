# Phase-3 Pair Programming Oturumu

## Başlangıç

Bu fazda sistemin mevcut yapısını bozmadan yeni davranışlar eklemek için hangi Behavioral Design Patternlerin uygun olabileceğini AI ile tartıştım.

İlk olarak mevcut mimariyi anlattım. Factory Method, Singleton, Decorator, Facade örüntülerinin zaten kullanıldığını söyledim ve sistemi daha genişletilebilir hale getirmek istediğimi belirttim.


## Tartışılan İlk Konu: Hangi Behavioral Patternler Uygun?

### Benim Sorularım
- Bu projeye hangi behavioral örüntüler uygun olur?
- OCP prensibini en iyi hangi örüntü sağlar?
- Gereksiz karmaşıklık oluşturmadan sistemi nasıl genişletebilirim?

### AI'ın Önerileri
AI şu örüntüleri önerdi:
- Strategy
- Observer
- Command
- State

Her örüntünün ne işe yaradığını açıkladı.

## Strategy Pattern Tartışması

AI, şifreleme algoritmalarının runtime’da değişebilmesi için Strategy Pattern kullanılmasını önerdi. Başta Factory Method zaten bulunduğu için Strategy gerekli mi diye düşündüm ve AI'a şunu sordum: Factory ve strategy arasındaki farklar neler? AI'ın cevabı: 
- Factory nesneyi oluşturuyor
- Strategy ise davranışı runtime değiştirmeyi kolaylaştırıyor

Bu farkı anlayınca Strategy Pattern eklemeye karar verdim.

## Observer Pattern Tartışması

Daha sonra sistemde loglama ve olay takibi yapmak istediğimi söyledim. AI Observer Pattern önerdi.Şifreleme başladığında, Şifreleme tamamlandığında, Hata oluştuğunda farklı gözlemcilerin tetiklenebileceğini açıkladı.Bu fikir mantıklı geldi çünkü mevcut şifreleyici kodlarını değiştirmeden yeni davranış eklenebiliyordu.

## Uygulamadığım Öneriler

### Command Pattern
AI işlemleri komut nesneleri olarak tutabileceğimi söyledi. Ancak projede undo/redo sistemi, görev kuyruğu ve işlem geçmişi ihtiyacı yoktu. Bu nedenle gereksiz abstraction olacağını düşündüm.

### State Pattern
AI durum yönetimi için State Pattern önerdi. Ancak sistem çok fazla state içermiyordu, karmaşık geçişler barındırmıyordu. Bu nedenle projeye doğal oturmadığını düşündüm.

## Kodlama Süreci

Birlikte şu adımları planladık:

1. Strategy interface oluşturuldu
2. AES/RSA/Base64 stratejileri ayrıldı
3. Observer interface oluşturuldu
4. Log ve zaman gözlemcileri eklendi
5. Main dosyası güncellendi

Kodların tamamını doğrudan kopyalamadım. AI’ın önerdiği yapıyı anlayıp kendi projemin mimarisine göre düzenledim.


## Öğrendiklerim

Bu oturumda özellikle şunu daha iyi anladım:

- Factory ve Strategy benzer görünse de farklı problemleri çözüyor
- Observer Pattern mevcut sistemi değiştirmeden davranış eklemek için çok uygun
- Her pattern her projeye uygun değil
- Gereksiz abstraction projeyi karmaşıklaştırabiliyor
- AI sayesinde tartışarak kalıcı bir öğrenme sağladım.


## AI Olmadan Süre Tahmini

AI olmadan uygun pattern seçimi, mimari kararlar, behavioral patternlerin farklarını anlamak çok daha uzun sürebilirdi. Son faz diğer fazlardan daha zor olmasına rağmen AI sayesinde daha kısa sürdü. AI olmadan yaklaşık 6-10 saat süreceğini düşünüyorum.
AI ile birlikte bu süreç yaklaşık 2-3 saat içinde ilerledi.

## Sonuç

AI bu fazda özellikle pattern seçimi, mimari düşünme, OCP uyumluluğu, behavioral pattern farkları konularında yardımcı oldu. Ancak son kararları ben verdim ve yalnızca projeye gerçekten uygun olan örüntüleri uyguladım.