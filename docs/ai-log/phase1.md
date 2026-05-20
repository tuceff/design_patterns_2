# Phase-1

## PROMPT:
    "Bu kodu gözden geçir. Hangi yaratımsal örüntü hataları var ve bunları çözmek için hangi yöntemleri kullanmalıyım."

## AI cevabının özeti:
    Tasarımsal Problemler
        1. Object Creation (Nesne Oluşturma) Kontrolsüz
        2. Algoritma Seçimi if-elif ile Yapılıyor
        3. Nesne Üretimi Soyutlanmamış

    Kullanılması Gereken Creational Pattern’lar
        1. Factory Method Pattern (En Önemli Çözüm)
        2. Singleton Pattern (RSA Key Yönetimi İçin)
        3. Builder Pattern (Opsiyonel Ama Güzel İyileştirme)

## Ben ne uyguladım?
    Factory Method ve singleton ile ilerlemeyi yeterli buldum. Bu yüzden uygun nesneyi üretmesi için factory method ve tek nesne üretmesi için de singeton kullandım.