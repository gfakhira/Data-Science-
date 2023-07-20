import datetime

List_layanan_service = [{"Nomor Member" : 2202185, "Nama" : "Tinky Winky", "Tanggal Pelaporan" : datetime.date(2022,1,5), "Status" : "OPEN"},
                        {"Nomor Member" : 2202301, "Nama" : "Dipsy", "Tanggal Pelaporan" : datetime.date(2022,1,6), "Status" : "OPEN"},
                        {"Nomor Member" : 2203033, "Nama" : "Lala", "Tanggal Pelaporan" : datetime.date(2022, 1, 12), "Status" : "OPEN"},
                        {"Nomor Member" : 2203055, "Nama" : "Asep", "Tanggal Pelaporan" : datetime.date(2022,1,14), "Status" : "OPEN"},
                        {"Nomor Member" : 2204055, "Nama" : "Tabi", "Tanggal Pelaporan" : datetime.date(2022,1,17), "Status" : "OPEN"}]

# Menu 1 Menampilkan Daftar Customer
def menudaftar():
    print("\nDaftar Customer: \n")
    print("Nomor Member \t| Nama Customer \t| Tanggal Pelaporan \t| Status")
    for a in range(len(List_layanan_service)) :
        for a in range(0, 5):
            print('{} \t| {}  \t\t| {} \t\t| {}'.format(List_layanan_service[a]["Nomor Member"], 
                                              List_layanan_service[a]["Nama"], 
                                              List_layanan_service[a]["Tanggal Pelaporan"],
                                              List_layanan_service[a]["Status"]))
        return menudaftar


# Menu 2; Menambahkan Data Customer dengan Registrasi
def menuregis():
    while True:
        regisnomember = input("\nRegistrasi \nInput Nomor Member: \t")
        regisnama = input("Input Nama Customer: \t\t")
        registanggal = datetime.date.today()
        regisstatus = "OPEN"

        List_layanan_service.append({ "Nomor Member" : regisnomember, 
                                     "Nama" : regisnama, 
                                     "Tanggal Pelaporan": registanggal, 
                                     "Status": regisstatus})

        print('{} \t| {} \t| {} \t| {}'.format("Nomor Member", "Nama Customer", "Tanggal Pelaporan", "Status"))
        for a in range(len(List_layanan_service)) :
            print('{} \t| {}  \t\t| {} \t\t| {}'.format(List_layanan_service[a]["Nomor Member"], 
                                              List_layanan_service[a]["Nama"], 
                                              List_layanan_service[a]["Tanggal Pelaporan"],
                                              List_layanan_service[a]["Status"]))
            
        checkpoint = input("\nRegistrasi Lagi? (Ya = y /Tidak = n): \t")
        if checkpoint == "n":
            print("\nData Berhasil Diinput")
            break
    return menuutama


# Menu 3; Menghapus Data Customer dengan Pembatalan
def menubatal():
    print("\nStatus Pelayanan Service: \n")
    print('{} \t| {} \t| {} \t| {} \t| {}'.format("Index", "Nomor Member", "Nama Customer", "Tanggal Pelaporan", "Status"))
    for index, item in enumerate(List_layanan_service):
        print(f"{index} \t| {item['Nomor Member']}  \t| {item['Nama']}  \t\t| {item['Tanggal Pelaporan']} \t\t| {item['Status']}")
        
    hapus_data = int(input("\nMasukkan Index Data Customer Yang Ingin Dibatalkan: \t"))

  
    if hapus_data < len(List_layanan_service):

        List_layanan_service.pop(hapus_data)

        print('{} \t| {} \t| {} \t| {}'.format("Nomor Member", "Nama Customer", "Tanggal Pelaporan", "Status"))
        for a in range(len(List_layanan_service)) :
            print('{} \t| {}  \t\t| {} \t\t| {}'.format(List_layanan_service[a]["Nomor Member"], 
                                                        List_layanan_service[a]["Nama"], 
                                                        List_layanan_service[a]["Tanggal Pelaporan"],
                                                        List_layanan_service[a]["Status"]))
        print("\nPelayanan Service Berhasil Dibatalkan")

    else:
        print(f"Index {hapus_data} Pada Data Tidak Ditemukan")


# Menu 4; Menampilkan Jadwal Pelaksanaan Service 
def menujadwal():              
    print("\nDaftar Pelayanan Service: ")
    print('{} \t| {} \t| {} \t| {} \t| {}'.format("Index", "Nomor Member", "Nama Customer", "Tanggal Pelaporan", "Status"))
    for index, item in enumerate(List_layanan_service):
        print(f"{index} \t| {item['Nomor Member']}  \t| {item['Nama']}  \t\t| {item['Tanggal Pelaporan']} \t\t| {item['Status']}")
    

    print("\nPenjadwalan Pelayanan Service: ")
    print('{} \t| {} \t| {} \t| {} \t| {}'.format("Index", "Nomor Member", "Nama Customer", "Tanggal Service", "Status"))
    for index, item in enumerate(List_layanan_service):
        tanggal = item["Tanggal Pelaporan"]+ datetime.timedelta(days=2)
        print(f"{index} \t| {item['Nomor Member']}  \t| {item['Nama']}  \t\t| {tanggal} \t\t| {item['Status']}")

def exit():
    print("\nTerima Kasih dan Sampai Jumpa!")


def menuutama():
    while True:
        inputmenuservice = input('''
Selamat Datang Di Jasa Service Tubbies
                        
Jasa Pelayanan:
1. Daftar Customer
2. Registrasi Pelayanan Service
3. Pembatalan Pelayanan Service
4. Penjadwalan Service 
5. EXIT

Masukkan Pilihan Angka Untuk Jenis Pelayanan Anda: \t''')
    
        if inputmenuservice == "1":
            menudaftar()
        elif inputmenuservice == "2":
            menuregis()
        elif inputmenuservice == "3":
            menubatal()
        elif inputmenuservice == "4":
            menujadwal()
        elif inputmenuservice == "5":
            exit()
            break

menuutama()
