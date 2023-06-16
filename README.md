# Goruntu_Isleme_Hexapod
 Sistem Analizi ve Tasarımı II Vize - Final
 
![image](https://github.com/Atakan-Demir/Goruntu_Isleme_Hexapod/assets/101272960/c352a729-a8be-4cfe-a5b3-7280aa8852a3)

![image](https://github.com/Atakan-Demir/Goruntu_Isleme_Hexapod/assets/101272960/812f8fba-ab8c-437d-8db8-96c091c8e219)

![image](https://github.com/Atakan-Demir/Goruntu_Isleme_Hexapod/assets/101272960/6dd2884c-a7ac-44c5-baa0-bddcd67497d5)

### Referanslar

https://markwtech.com/robots/hexapod/
https://docs.opencv.org/4.x/index.html


### PROJE GİRİŞİ

Bu projede, Arduino Mega mikrodenetleyici ve Python programlama dili kullanılarak 
gerçekleştirilen bir Hexapod geliştirilmiştir. Sistem, Arduino Mega ve bir Raspberry Pi 3 
Model B+ arasında seri iletişim kurarak, kamera üzerinden renkleri takip etmektedir.

Projenin Amacı: Bu projenin temel amacı, Arduino Mega mikrodenetleyiciyi kullanarak 
gerçek zamanlı veri alışverişi sağlamak ve kamera üzerinden renk tespiti yapmaktır. Arduino Mega, seri iletişim protokolünü kullanarak Raspberry veri gönderirken, Python programı bu veriyi almakta ve görüntü işleme teknikleriyle renkleri tespit etmektedir. Renklerin tespiti yapıldıktan sonra, Arduino Mega'ya uygun komutlar gönderilerek belirli işlemler gerçekleştirilir.

QR kod okuma işlemi için https://pypi.org/project/pyzbar/ kaynak alınarak pyzbar Kütüphanesi kullanılmıştır.

Projenin Özellikleri:

•	Arduino Mega ile seri iletişim kurma: Arduino Mega, Raspberry Pi 3 Model B+ ile seri bağlantı kurarak veri alışverişinde bulunur. Seri iletişim protokolü kullanılarak mikrodenetleyiciye komutlar gönderilir ve veri alınır.

•	Görüntü işleme ve renk tespiti: Python programlama dili kullanılarak görüntü işleme işlemleri gerçekleştirilir. Kamera üzerinden alınan görüntü üzerinde renk tespiti yapılır. Kırmızı, yeşil ve mavi renkler için ayrı maskeler oluşturulur ve nesne tespiti yapılır.

•	Hareket kontrolü: Renk tespiti sonucunda elde edilen bilgilere dayanarak, Arduino Mega üzerinde belirli hareket kontrol işlemleri gerçekleştirilir. Nesnenin yatay konumu ve derinlik değeri kullanılarak hareket yönü ve mesafe hesaplanır. Arduino Mega'ya uygun komutlar gönderilerek belirli hareketler gerçekleştirilir.

Bu projenin sonuçları, gerçek zamanlı veri alışverişi, görüntü işleme ve hareket kontrolü gibi konularda uygulama geliştirme ve teknoloji entegrasyonu becerilerini geliştirmek için kullanılabilir. Ayrıca, Arduino tabanlı projelerde mikrodenetleyici ve bilgisayar arasında seri iletişimi kullanma konusunda da faydalı bir deneyim sunmaktadır.


Bu proje aşağıdaki ana adımları içermektedir:

1.	Donanımın Kurulumu: Arduino Mega mikrodenetleyicisi, Raspberry Pi 3 Model B+ ve kamera arasında bağlantıların sağlanması için gerekli donanım kurulumu gerçekleştirilir. Arduino Mega, bilgisayara USB kablosuyla bağlanır ve kamera sisteme entegre edilir.

2.	Seri İletişim Protokolünün Kurulması: Arduino Mega, Raspberry Pi 3 Model B+ ile seri iletişim kurmak için uygun protokolleri kullanır. Raspberry Pi 3 Model B+, Python programı aracılığıyla Arduino'ya komutlar gönderir ve veri alır.

3.	Görüntü İşleme ve Renk Tespiti: Python programı, kamera üzerinden alınan görüntüyü işleyerek renk tespiti yapar. Görüntü işleme teknikleri kullanılarak kırmızı, yeşil ve mavi renkler için ayrı maskeler oluşturulur ve nesnelerin konumları tespit edilir.

4.	Hareket Kontrolü: Renk tespiti sonucunda elde edilen bilgilere dayanarak, Arduino Mega üzerinde belirli hareket kontrol işlemleri gerçekleştirilir. Nesnenin yatay konumu ve derinlik değeri kullanılarak hareket yönü ve mesafe hesaplanır. Arduino Mega'ya uygun komutlar gönderilerek belirli hareketler gerçekleştirilir.


5.	Veri Analizi ve Sonuçlar: Projenin veri analizi aşamasında, elde edilen sonuçlar incelenir ve değerlendirilir. Renk tespiti doğruluk oranı, hareket kontrolünün hassasiyeti ve sistem tepki süreleri gibi faktörler değerlendirilerek proje performansı değerlendirilir.

Bu proje, robotik sistemlerde renk tabanlı görüntü işleme ve hareket kontrolü uygulamaları için bir temel oluşturmayı hedeflemektedir. Ayrıca, Arduino ve Python gibi popüler platformları kullanarak gerçek zamanlı veri alışverişi ve teknoloji entegrasyonu konularında pratik deneyim kazanılmıştır.




### Python Kod Raporu

Kod Hakkında:

Python kodu, OpenCV, numpy, time ve serial kütüphanelerini kullanarak Arduino Mega ile seri iletişim kurmayı ve kamera üzerinden renkleri takip etmeyi sağlar. Renkler arasında KIRMIZI>YEŞİL>MAVİ hiyerarşisi vardır. Kamerada KIRMIZI bir nesne var ise YEŞİL ve MAVİ nesneler göz ardı edilir.  

Kullanılan Kütüphaneler:

- cv2 (OpenCV): Görüntü işleme ve kamera yakalama işlemleri için kullanılır.
- numpy: Dizi işlemleri ve matematiksel işlemler için kullanılır.
- time: Zaman gecikmesi için kullanılır.
- serial: Arduino ile seri iletişim sağlamak için kullanılır.

Kod Açıklaması:

1. İlk olarak, gerekli kütüphaneler import edilir ve Arduino Mega ile seri bağlantı kurulur.

2. Arduino’ya veri göndermek için belirli bir veri (x) oluşturulur ve encode edilerek seri porta gönderilir.

3. Seri porttan veri okunur ve ekrana yazdırılır.

4. Kamera başlatılır ve görüntü çözünürlüğü belirlenir.

5. 'map_range' fonksiyonu, bir değeri bir aralıktan başka bir aralığa yeniden eşlemek için kullanılır.

6. 'yonMesafeHesapla' fonksiyonu, nesnenin yatay konumunu ve derinlik (boyut) değerini alır. Ardından, bu bilgilere dayanarak hareket yönünü ve mesafeyi hesaplar ve Arduino’ya gönderir.

7. Sonsuz döngü içinde, kameradan görüntü okunur ve renk tespiti yapılır. Kırmızı, yeşil ve mavi renkler için ayrı maskeler oluşturulur ve nesne tespiti yapılır.

8. Nesnelerin konumları, boyutları ve renkleri çerçeve üzerinde görselleştirilir. Arduino’ya gönderilecek veri hesaplanır ve gönderilir.

9. Görüntüler ekranda gösterilir.

10. 'q' tuşuna basıldığında program sonlandırılır.

11. Kullanılan kaynaklar serbest bırakılır ve program kapatılır.

Bu projenin sonuçları, renk tabanlı görüntü işleme ve hareket kontrolü uygulamalarında kullanılan yöntemlerin etkinliğini ve doğruluğunu değerlendirmek açısından da önemlidir. Bazı problemlere rağmen proje, renk tespiti doğruluk oranı, hareket kontrolünün hassasiyeti, sistem tepki süreleri gibi faktörler üzerinde değerlendirme yapılmasını sağlayacaktır.






-Atakan Demir (Görüntü İşleme ve Arduino)

-Ahmet Emral Özcan (Mekanik, Elektronik ve Ardunio)

