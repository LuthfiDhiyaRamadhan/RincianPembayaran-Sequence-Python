print("Program Rincian Pembayaran")
print("=========================================================")

total_bayar = int(input("Total Yang Harus Di Bayar : Rp. "))
besar_bayar = int(input("Besar Bayar               : Rp. "))

kembalian = besar_bayar - total_bayar
print (f"Kembalian : Rp. {kembalian}")
print ("Rincian Kembalian :")
lembar50 = kembalian // 50000
print (f"Rp. 50.000 : {lembar50} Lembar")
kembalian = kembalian % 50000
lembar20 = kembalian // 20000
print (f"Rp. 20.000 : {lembar20} Lembar")
kembalian = kembalian % 20000
lembar10 = kembalian // 10000
print (f"Rp. 10.000 : {lembar10} Lembar")
kembalian = kembalian % 10000
lembar5 = kembalian // 5000
print (f"Rp. 5.000 : {lembar5} Lembar")
kembalian = kembalian % 5000
lembar2 = kembalian // 2000
print (f"Rp. 2.000 : {lembar2} Lembar")
kembalian = kembalian % 2000
lembar1 = kembalian // 1000
print (f"Rp. 1.000 : {lembar1} Lembar")
