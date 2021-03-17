
belanja = int(input("Total belanja : "))
if (belanja <= 300000):
    diskon = belanja * 15 / 100
    total  = belanja - diskon
    print("Belanja    : Rp.",belanja )
    print("Diskon 15% : Rp.",diskon )
    print("Total yang harus dibayarkan : Rp.",total)
else:
    diskon = belanja * 20/100
    total  = belanja - diskon
    voucher = belanja // 300000
    dapat = voucher
    vouncher = 50000 * voucher
    print("Diskon 20% : Rp.",diskon)
    print("total      : Rp.",total)
    print("Vouncher yang didapat : ",dapat,"vouncher")
    pilih = input("Potong total harga dengan vouncher? (y/n) : ")
    if (pilih == "Y") or (pilih == "y"):
        total_bayar = total - vouncher
        print("Total nilai vouncher  : Rp",vouncher)
        print("Total yang harus dibayarkan : Rp.",total_bayar)
    else:
        print("Total nilai vouncher yang anda dapat  : Rp",vouncher)
        print("Total yang harus dibayarkan : Rp.",total)
        
