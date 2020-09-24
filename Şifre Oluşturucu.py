import time
from colorama import Fore, Back, Style, init
import sys
import os
init(autoreset=True)


f = open("BENİ OKU.txt", "w")
f.write("""--BU PROGRAM EMİR ALİ ATEŞ TARAFINDAN YAZILMIŞTIR--


ŞİFRELER NASIL KIRILIR?:
-Bilgisayar şifre atak programları (Brute Force Gibi) otomatik olarak şifreler oluşturarak kişisel şifrelerinizi kırabiliyor.
-Özellikle içinde ad, soyad, yaş gibi kişisel bilgiler içeren şifreleri daha kolay kırabiliyor. Hackerler biraz araştırmayla
kişisel bilgilerinize ulaşabilir ve hesaplarınızın böylelikle kendi elinizle güvenliğini düşürürsünüz.


ŞİFREYİ KENDİMLE İLGİSİ OLMAYAN RASTGELE KELİME GRUPLARIYLA YAPTIM ŞİMDİ GÜVENDE MİYİM?:
-Bazı Gelişmiş şifre atak programları malesef böyle şifreleri de bulabilmektedirler.
-Tam Güvenliğin formülü yok mu demeyin, var şifrelerin uzunluğu arttıkça yeni milyonlarca ihtimal ortaya çıkıyor. Sırada Bir tabloda
minik bir örnekle Şifre Atak Programlarının şifrelerin hane sayısı arttıkça şifrenizi kırmak için ne kadar süre harcamaları gerektiği
gösterilmiştir.


ŞİFRELERİN ŞİFRE ATAK PROGRAMLARININ ATAKLARIYLA KIRILMA SÜRESİ:
---7 HANELİ ŞİFRE:0.29 SANİYE---
---8 HANELİ: 5 SAAT---
---9 HANELİ: 5 GÜN---
---10 HANELİ: 4 AY---
---11 HANELİ: 10 YIL---
---12 HANELİ: 2 ASIR---
...


ŞİFREMİ BU UYGULAMAYLA ÜST DÜZEY GÜVENLİKLİ BİR HALE GETİRDİM ŞİMDİ ŞİFRELERİM ASLA ÇALINMAYACAK MI?:
-Şifrelerinizin hala çalınma ihtimalleri var ancak bu çalma yöntemlerinden birini bu uygulamayla men ettiniz.Ancak şifreleriniz Hala çalınabilir.
-Bunun en yaygın yöntemi Bilgisayar Virüsleri Ve Phishing Saldırıları.


BİLGİSAYAR VİRÜSLERİ VE PHİSHİNG SALDIRILARINDAN NASIL KORUNULUR?:
-Bilgisayar Virüslerinden Korunmanızın yolu basittir. İnternetten kaynağına güvenmediğiniz dosyaları indirmemeniz ve kaynağına güvenmediğiniz
sitelere girmemenizdir. Aynı zamanda Okul, Hastahane Gibi Bilgisayardan Bilgisayara Takılan Harici Diskleri(USB BELLEKLER) Bilgisayarınıza takmamanız gerekir.
Topluma Açık Wİ-Fİ ağlarına bağlanmamanız gerekir.
-Phishing Saldırıları nedir diye bir alt başlık açabiliriz: Phishing Saldırılarının en yaygın yapılanı Size bir Vaatte bulunulup bir websitesine girmenize ya da
bir dosya indirmenize sebep olunabilir. Böylece sizin şifrelerinizi ele geçirebilirler.
-Phishing Saldırılarından Korunmak Basittir. Gelen e-postalardaki eklere ve linklere tıklamamak bu saldırılardan korunmanın en iyi yoludur

**ŞİFRELERİNİZ ŞİFRELER.txt DOSYASININ İÇİNE KAYDEDİLECEKTİR**

""")


print(Fore.RED+"EMYOUNOONE Tarafından Kodlanmıştır")
time.sleep(2)
input("Şifre Oluşturucu Programına Hoş Geldiniz...\n \nDevam Etmek İçin Enter'e Basınız..\n")
print(Fore.RED+"BİLMENİZ GEREKEN HER ŞEY PROGRAMI KURDUĞUNUZ YERDE BENİ OKU.txt DOSYASININ İÇİNDE..\n")
os.system('cls' if os.name=='nt' else 'clear')
time.sleep(3)
print("YÜKLENİYOR...\n\n")
print("##########")

time.sleep(1)
print("##################")

time.sleep(1)
print("##########################")

time.sleep(1)
print("########################################")

      




while True:
    f = open("ŞİFRELER.txt", "a")

    import random
    şifre_oluşturucu="""abcçdfegğhıijklmnoöprsştuüvyzxwq\
ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXQW\
1234567890\
!'^+%&/()=?}][{#£><.,-"$*:;|_"""
    print("Şifrenin maximum uzunluğu 30 minimum uzunluğu 1 olmalı.")
    uzunluk=int(input("Şifreniz için bir uzunluk belirtin :"))
    kayıt=input("Şifrenizi Ne Olarak Kayıt Edelim :")
    if uzunluk == (1):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (2):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (3):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (5):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (6):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (7):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (8):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (9):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" =" + password+"\n" )
    elif uzunluk == (10):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (11):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (12):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" =" + password+"\n" )
    elif uzunluk == (13):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (14):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (15):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (16):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (17):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (18):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (19):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (20):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (21):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (22):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (23):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (24):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (25):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (26):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (27):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (28):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (29):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (30):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\n\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    else:
        print("Lütfen Geçerli Bir uzunluk Giriniz..")
    soru=int(input("\n\nYeniden Oluşturmak için 1'e, Çıkmak İçin 2'ye Basınız :"))
    if soru == (1):
        continue
    elif soru == (2):
        break
        quit()
    else:
        print("Lütfen Geçerli Bir Kod Giriniz")
                


    
                
        
        
