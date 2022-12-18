print("""**********************
Kullanıcı Girişi
**********************""")

sys_kullanıcıadı ="polohan"
sys_kullanıcıparola ="12345"

kullanıcı_adı = input("Kullanıcı Adınızı Giriniz : ")
kullanıcı_parola = input("Kullanıcı Parolasını Giriniz :")

if (kullanıcı_adı == sys_kullanıcıadı and sys_kullanıcıparola != kullanıcı_parola):
    print("Parola Yanlış")

elif (kullanıcı_adı != sys_kullanıcıadı and sys_kullanıcıparola == kullanıcı_parola):
    print("Kullanıcı Adı Yanlış")

elif (kullanıcı_adı != sys_kullanıcıadı and sys_kullanıcıparola != kullanıcı_parola):
    print("Kullanıcı Adı Yanlış Ve Parola Yanlış")
else :
    print("Giriş Başarılı")