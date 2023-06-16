import cv2 # Görüntü işleme kütüphanesi
import numpy as np # Matematiksel işlemler için kütüphane
import time # Zaman kütüphanesi
import serial # Ardunio ile seri haberleşme kütüphanesi
from pyzbar import pyzbar # QR kod okuma kütüphanesi	

"""
if 1 == 1
   
#Ardunio Mega'ya baplancak seri portun bilgileri
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.reset_input_buffer()
    while True:
        x = "126;-126:"
        time.sleep(1)
        ser.write(x.encode())
        
        line =ser.readline().decode('utf-8').rstrip()
        print(line)
"""
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
ser.reset_input_buffer()
# Kamera başlatma
cap = cv2.VideoCapture(0)
cozunurluk=(640,480)
cozX=cozunurluk[0]
cozY=cozunurluk[1]

""" QR Kod Okuma Fonksiyonu """

def qrOku(frame):
    # QR kodu tara
    barcodes = pyzbar.decode(frame)

    # QR kodu bulunduysa içeriğini döndür
    if len(barcodes) > 0:
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            print(barcodeData)
            return barcodeData
        
    # QR kodu bulunamadıysa boş bir string döndür
    else:
        return ""


def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def yonMesafeHesapla(yatay,derinlik,renk):
    str_deger=""
    if yatay > (cozX/2)+(0.5*(cozX/2)):
        #print("SOLLL!")
        deger = map_range(yatay,int((cozX/2)+(0.5*(cozX/2))),cozX,0,127)
        str_deger = str(deger)
        str_deger = str_deger + ";"
        
        
    elif yatay < (cozX/2) - (0.5*(cozX/2)):
        #print("SAĞĞĞ!")
        deger = map_range(yatay,int((cozX/2)-(0.5*(cozX/2))),cozX-cozX,0,-127)
        #print(deger)
        str_deger = str(deger)
        str_deger = str_deger + ";"
    else:
        str_deger = "0;"   
        
        
    if renk == "red" and derinlik>100:
        str_deger = str_deger + "127:"  
    elif renk == "green" and derinlik < 100:
        str_deger = str_deger + "-127:"
    elif renk == "blue":
        pass
    

    
    print(str_deger)
    ser.write(str_deger.encode())
        
    line =ser.readline().decode('utf-8').rstrip()
    print(line)
"""
def mesafeHesapla(derinlik,renk):
    if renk == "red" and derinlik>100:
        
        
    elif renk == "green" and derinlik < 100:
        
    elif renk == "blue":
        print("İLGİLENMİYOR...")
  """      
    
while True:

    
    # Görüntüyü okuma
    ret, frame = cap.read()
    
    # Görüntüyü boyutlandırma
    frame = cv2.resize(frame, cozunurluk)
    #cv2.rectangle(frame, (int((cozX/2)-(0.5*(cozX/2))), int((cozY/2) - (0.5*(cozY/2)))), (int((cozX/2)+(0.5*(cozX/2))), int((cozY/2) + (0.5*(cozY/2)))), (255, 40, 255), 2)
    # Görüntüyü BGR renk uzayından HSV renk uzayına dönüştürme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # QR kodunu tara ve içeriğini al
    qr_code_icerik = qrOku(gray)

    """
    all_low=np.array([0, 0, 0])
    all_up=np.array([255, 255, 255])
    all_mask = cv2.inRange(hsv, all_low, all_up)
    alanlar, _ = cv2.findContours(all_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for alan in alanlar:
        
        kx, ky, kw, kh = cv2.boundingRect(alan/2)
        cv2.rectangle(frame, (kx, ky), (kx+kw, ky+kh), (255, 0, 255), 2)
    """
    
    
    # Kırmızı renk aralığı
    lower_red1 = np.array([0, 100, 100]) #[0, 50, 50]
    upper_red1 = np.array([3, 255, 255]) #[10, 255, 255]
    lower_red2 = np.array([175, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    

    
    # Kırmızı renk maskesi oluşturma
    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    
    # Yeşil renk aralığı
    lower_green = np.array([40, 100, 40]) #[40, 50, 50]
    upper_green = np.array([80, 255, 255])
    
    # Yeşil renk maskesi oluşturma
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Mavi renk aralığı
    lower_blue = np.array([78, 158, 124]) #[78, 158, 124] [80, 110, 90]
    upper_blue = np.array([130, 255, 255]) # [138, 255, 255] [130, 255, 255]
    
    # Mavi renk maskesi oluşturma
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Maskeyi uygulama
    red_res = cv2.bitwise_and(frame, frame, mask=red_mask)
    green_res = cv2.bitwise_and(frame, frame, mask=green_mask)
    blue_res = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    is_red = np.sum(red_mask)
    is_green = np.sum(green_mask)
    is_blue = np.sum(blue_mask)

    """ Eğer qr kod tespit edilirse selam ver """
    if qr_code_icerik != "":
        # qr kod içeriği ekran üzerinde gösterme
        if qr_code_icerik =="Selam Ver!":
            str_deger = "-:"
            ser.write(str_deger.encode())
        
            line =ser.readline().decode('utf-8').rstrip()
            print(line)
            cv2.putText(frame, qr_code_icerik, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            print(qr_code_icerik)
            time.sleep(5)
        print(qr_code_icerik)
        
      

    elif is_red > 100000:
        # Nesne tespiti ve kare çizme
        #print("KIRMIZI")
        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Kırmızı renk için nesne takibi
        for contour in contours:
            # Contour alanına göre filtreleme
            if cv2.contourArea(contour) > 200:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                z=(w + h) // 2
                yonMesafeHesapla(x,z,"red")
                
                # Nesnenin merkezini hesaplama
                center_x = x + w // 2
                center_y = y + h // 2
                center_z = (w + h) // 2  # Basit bir yaklaşımla, genişlik ve yükseklikten ortalama bir değer
                # Kutucuğun üstüne koordinatları yazdırma
                cv2.putText(frame, f'X: {center_x}, Y: {center_y}, Z: {center_z}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
                

    elif is_green > 100000:
        
        #print("YEŞİL")
        contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Yeşil renk için nesne takibi
        for contour in contours:
            # Contour alanına göre filtreleme
            if cv2.contourArea(contour) > 250:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                z=(w + h) // 2
                yonMesafeHesapla(x,z,"green")
                
                # Nesnenin merkezini hesaplama
                center_x = x + w // 2
                center_y = y + h // 2
                center_z = (w + h) // 2  # Basit bir yaklaşımla, genişlik ve yükseklikten ortalama bir değer
                # Kutucuğun üstüne koordinatları yazdırma
                cv2.putText(frame, f'X: {center_x}, Y: {center_y}, Z: {center_z}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        
    
    elif is_blue > 100000:    
        #print("MAVİ")
        contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Mavi renk için nesne takibi
        for contour in contours:
            # Contour alanına göre filtreleme
            if cv2.contourArea(contour) > 250:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                z=(w + h) // 2
                yonMesafeHesapla(x,z,"blue")
                
                # Nesnenin merkezini hesaplama
                center_x = x + w // 2
                center_y = y + h // 2
                center_z = (w + h) // 2  # Basit bir yaklaşımla, genişlik ve yükseklikten ortalama bir değer
                # Kutucuğun üstüne koordinatları yazdırma
                cv2.putText(frame, f'X: {center_x}, Y: {center_y}, Z: {center_z}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
    
    else:
        #print("Tespit YOK!")
        pass

    # Görüntüyü ekranda gösterme
    cv2.imshow('frame', frame)
    cv2.imshow('green_res', green_res)
    cv2.imshow("red_res",red_res)
    cv2.imshow("blue_res",blue_res)
    
    # Çıkış için 'q' tuşuna basılmasını kontrol etme
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Gerekli kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()
