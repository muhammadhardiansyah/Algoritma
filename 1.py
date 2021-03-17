tkt_dewasa = 225000
tkt_anak = 150000
tkt_infant= 25000

while True:
    print("A. Beli tiket")
    print("B. Keluar")
    pilih = input("Pilihan : ")
    if (pilih == 'A') or (pilih == 'a'):
        dewasa = int(input("Jumlah orang dewasa : "))
        anak   = int(input("Jumlah anak-anak    : "))
        infant = int(input("Jumlah infant       : "))
        if (dewasa > 4):
            harga_real = (dewasa * tkt_dewasa) + (anak * tkt_anak) + (infant * tkt_infant)
            diskon = harga_real * 20 / 100 
            harga = harga_real - diskon
            print ("Biaya : Rp.", harga_real)
            print ("Diskon: Rp.",diskon)
            print("Biaya keseluruhan : Rp.",harga)
            
        else:
            harga_real = (dewasa * tkt_dewasa) + (anak * tkt_anak) + (infant * tkt_infant)
            diskon = 0
            harga = harga_real - diskon
            print ("Biaya : Rp.", harga_real)
            print ("Diskon: Rp.",diskon)
            print("Biaya keseluruhan : Rp.",harga)
    else:
        break

