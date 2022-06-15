
class menunasi:
     def __init__(self, nasi):
         self.nasi = nasi


p1 =menunasi("nasi jagung : Rp 7000")
p2 =menunasi("nasi goreng : RP 10.000")
p3 =menunasi("nasi rames : Rp 8000")

print('selamat menikmati!')
while True:
    print('---menu---')
    print('1.nasi jagung')
    print('2.nasi goreng')
    print('3.nasi rames')

    menu = int(input('Pilih Menu: '))
    jumlahpesan=int(input("masukkan jumlah pesanan : "))


    if menu == 1:
        print(p1.nasi)
        harga = 7000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
    
    elif menu == 2:
        print(p2.nasi)
        harga = 10.000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
    
    elif menu == 3:
        print(p3.nasi)
        harga = 8000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
      
