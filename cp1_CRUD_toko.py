#Tugas Capstone Project 1
#Nama   : Gede Sariasa
#ID     : JCDSOL-009-002
#Kelas  : JCDSOL-09 (WA)

katalog = {
'kode' : ["PF4-6128Gn","PF4-6128Ba","PF4-8256Si","PF4-8256Gn","PF4-8256Ba","PM5-464Ba","PM5-464Gn","PM5-464Ye","PM5-4128Ba","PM5-4128Gn","PM5-4128Ye","X12T-8256Ba","X12T-8256Bu","N11P-8128Bu","N11P-8128Gy"],
'seri' : ["POCO","POCO","POCO","POCO","POCO","POCO","POCO","POCO","POCO","POCO","POCO","Xiaomi","Xiaomi","Redmi","Redmi"],
'tipe' : ["POCO F4","POCO F4","POCO F4","POCO F4","POCO F4","POCO M5","POCO M5","POCO M5","POCO M5","POCO M5","POCO M5","Xiaomi 12T","Xiaomi 12T","Note 11 Pro","Note 11 Pro"],
'ram' : [6,6,8,8,8,4,4,4,4,4,4,8,8,8,8],
'internal' : [128,128,256,256,256,64,64,64,128,128,128,256,256,128,128],
'warna' : ["Green","Black","Silver","Green","Black","Black","Green","Yellow","Black","Green","Yellow","Black","Blue","Blue","Gray"],
'stok' : [3,10,2,8,0,6,3,0,6,8,6,9,9,3,4],
'harga' : [5200,5200,5700,5700,5700,2100,2100,2100,2400,2400,2400,6600,6600,4100,4100]
};

kata_sandi = 'admin' #kata sandi tersimpan

#List-list sementara
list_add = []
keranjang = []

#Menu untuk admin
def admin_menu(sandi) :
    if(sandi == kata_sandi) : #autentikasi sandi umtuk mengakses menu
        while True :
            pilihanMenu = input('''
Menu Toko HP Xiaomi
1. Tampilkan Katalog Toko
2. Tambah Data ke Katalog
3. Ubah Data di Katalog
4. Hapus Data dari Katalog
5. Kembali ke Homepage

Masukkan pilihan : ''')

            if(pilihanMenu == '1') :
                menu_list()
            elif(pilihanMenu == '2') :
                menu_add()
            elif(pilihanMenu == '3') :
                menu_edit()
            elif(pilihanMenu == '4') :
                menu_delete()
            elif(pilihanMenu == '5') :
                break
            else :
                print("\n****Pilihan yang Anda Masukkan Salah****")
    else :
        print("\n****Sandi Salah****")

#Tampilan menu katalog - untuk admin
def menu_list() :
    while True :
        pilihanMenu = input('''
Katalog Produk
1. Tampilan Katalog
2. Cari HP
3. Kembali ke Menu

Masukkan pilihan : ''')

        if(pilihanMenu == '1') :
            show_list()
        elif(pilihanMenu == '2') :
            find_phone()
        elif(pilihanMenu == '3') :
            break
        else :
            print("\n****Pilihan yang Anda Masukkan Salah****")

#Menu tambah data - untuk admin
def menu_add() :
    while True :
        pilihanMenu = input('''
Menambah Data
1. Tambah Data ke Katalog
2. Kembali ke Menu2

Masukkan pilihan : ''')

        if(pilihanMenu == '1') :
            add_phone()
        elif(pilihanMenu == '2') :
            break
        else :
            print("\n****Pilihan yang Anda Masukkan Salah****")

#Menu ubah data - untuk admin
def menu_edit() :
    while True :
        pilihanMenu = input('''
Mengubah Data
1. Ubah Data di Katalog
2. Kembali ke Menu

Masukkan pilihan : ''')

        if(pilihanMenu == '1') :
            edit_phone()
        elif(pilihanMenu == '2') :
            break
        else :
            print("\n****Pilihan yang Anda Masukkan Salah****")

#Menu hapus data - untuk admin
def menu_delete() :
    while True :
        pilihanMenu = input('''
    Menghapus Data HP
    1. Hapus Data HP
    2. Kembali ke Menu Utama

    Masukkan pilihan : ''')

        if(pilihanMenu == '1') :
            delete_phone()
        elif(pilihanMenu == '2') :
            break
        else :
            print("\n****Pilihan yang Anda Masukkan Salah****")

#Fungsi untuk menampilkan data sementara
def print_temp(a,b,c,d,e,f,g,h) :
            print('\nKode\t\t: {kode}\nSeri\t\t: {seri}\nTipe\t\t: {tipe}\nRAM \t\t: {ram}GB\nInternal\t: {internal}GB\nWarna\t\t: {warna}\nStok\t\t: {stok}\nHarga\t\t: {harga}k'.format(kode=a,seri=b,tipe=c,ram=d,internal=e,warna=f,stok=g,harga=h))

def show_list() :
    print('Katalog Toko\n')
    print('| Nomor\t| Kode\t\t|Seri\t|  Tipe  \t| RAM \t|    Internal\t| Warna\t\t| Stok\t| Harga\t|')
    for i in range(len(katalog['kode'])) :
        print('|  {nomor}\t| {kode} \t|{seri}\t| {tipe}\t| {ram}GB\t|     {internal}GB \t| {warna}  \t|  {stok}\t| {harga}k\t|'
        .format(nomor=i+1,kode=katalog['kode'][i],seri=katalog['seri'][i],tipe=katalog['tipe'][i],ram=katalog['ram'][i],internal=katalog['internal'][i],warna=katalog['warna'][i],stok=katalog['stok'][i],harga=katalog['harga'][i]))
        #nomor = index +1 untuk penomoran, agar tidak dimulai dari nol

def find_phone() :
    kode_cari = input('Masukkan kode produk : ')
    if kode_cari in katalog['kode']:
        i = katalog['kode'].index(kode_cari)
        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
    else:
        print('\n****Tidak ada produk yang sesuai****')

def add_phone() :
    while True :
        kode_tambah = input('Masukkan kode produk : ')
        if kode_tambah.replace('-','').isalnum() :
            if kode_tambah in katalog['kode']:       
                print('\n****Data sudah ada****')
            else :
                while True : #Seri
                    seri_add = input('\n1. POCO\n2. Xiaomi\n3. Redmi \nPilih seri : ').lower()
                    if seri_add in ['1','poco'] :
                        seri_add = 'POCO'
                        break
                    elif seri_add in ['2','xiaomi'] :
                        seri_add = 'Xiaomi'
                        break
                    elif seri_add in ['3','redmi'] :
                        seri_add = 'Redmi'
                        break
                    else :
                        print('\n****Pilihan seri salah!****')
                while True : #Tipe
                    tipe_add = input('Tipe : ')
                    if tipe_add.replace(' ','').isalnum() :
                        break
                    else :
                        print('\n****Tipe hanya boleh berisi alfanumerik dan spasi( )****')
                while True : #RAM
                    ram_add = input('Ukuran RAM (GB) : ')
                    if ram_add.isdigit() :
                        ram_add = int(ram_add)
                        break
                    else :
                        print('\n****Ukuran RAM harus angka positif****')
                while True : #Internal
                    internal_add = input('Ukuran memori internal (GB) : ')
                    if internal_add.isdigit() :
                        internal_add = int(internal_add)
                        break
                    else :
                        print('\n****Ukuran memori internal harus angka positif****')
                while True : #Warna
                    warna_add = input('Warna : ')
                    if warna_add.isalpha() :
                        break
                    else :
                        print('\n****Warna hanya boleh berisi alfabet****')
                while True : #Stok
                    stok_add = input('Jumlah stok : ')
                    if stok_add.isdigit() :
                        stok_add = int(stok_add)
                        break
                    else :
                        print('\n****Jumlah stok harus angka positif****')
                while True : #Harga
                    harga_add = input('Harga satuan (IDR) : ')
                    if harga_add.isdigit() :
                        harga_add = int(int(harga_add)/1000) #Mengubah ke ribuan
                        break
                    else :
                        print('\n****Harga harus angka positif****')

                while True : #Verifikasi
                    print('\nPreview data baru')
                    print_temp(kode_tambah,seri_add,tipe_add,ram_add,internal_add,warna_add,stok_add,harga_add)
                    verif_add = input('\nApakah data sudah benar? (Y/N) : ').lower()
                    if verif_add in ['y','n'] :
                        break
                    
                if verif_add == 'y' :
                    list_add = [kode_tambah,seri_add,tipe_add,ram_add,internal_add,warna_add,stok_add,harga_add] #list sementara
                    for key,value in zip(katalog.keys(), list_add) : #Memasukkan data baru ke katalog
                        katalog[key].append(value)
                    print('\n****Data {} berhasil ditambahkan****'.format(kode_tambah))
                else :
                    list_add = []
                    print('\n****Tidak ada data yang ditambahkan****')
            break
        else :
            print('\n****Kode hanya boleh berisi alfanumerik dan tanda strip(-)****')

def edit_phone() :
    show_list()
    while True :
        kode_edit = input('Masukkan kode produk : ')
        if kode_edit.replace('-','').isalnum() :
            if kode_edit in katalog['kode']:       
                i = katalog['kode'].index(kode_edit)
                print_temp(kode_edit,katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                
                while True : #Cek field yang dimasukkan
                    pilihan_key = input('\nData apa yang ingin diubah? : ').lower()
                    if pilihan_key in katalog.keys() :

                        #Ubah kode
                        if pilihan_key == 'kode' :
                            while True :
                                new_value = input('\nMasukkan kode yang baru : ')
                                if new_value.replace('-','').isalnum() :
                                    while True : #Verifikasi ubah data
                                        print_temp(new_value,katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Kode hanya boleh berisi alfanumerik dan tanda strip(-)****')                        

                        #Ubah seri
                        elif pilihan_key == 'seri' :
                            while True :
                                new_value = input('\n1. POCO\n2. Xiaomi\n3. Redmi \nPilih seri baru : ').lower()
                                if new_value in ['1','poco'] :
                                    new_value = 'POCO'
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],new_value,katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                elif new_value in ['2','xiaomi'] :
                                    new_value = 'Xiaomi'
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],new_value,katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                elif new_value in ['3','redmi'] :
                                    new_value = 'Redmi'
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],new_value,katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Pilihan seri salah!****')

                        #Ubah tipe
                        elif pilihan_key == 'tipe' :
                            while True :
                                new_value = input('Masukkan tipe yang baru : ')
                                if new_value.replace(' ','').isalnum() :
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],new_value,katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Tipe hanya boleh berisi alfanumerik dan spasi( )****')

                        #Ubah RAM
                        elif pilihan_key == 'ram' :
                            while True :
                                new_value = input('Ukuran RAM (GB) : ')
                                if new_value.isdigit() :
                                    new_value = int(new_value)
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],new_value,katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')

                                    break
                                else :
                                    print('\n****Ukuran RAM harus angka positif****')
                        
                        #Ubah Internal
                        elif pilihan_key == 'internal' :
                            while True : #Internal
                                new_value = input('Ukuran memori internal (GB) : ')
                                if new_value.isdigit() :
                                    new_value = int(new_value)
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],new_value,katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Ukuran memori internal harus angka positif****')
                        
                        #Ubah warna
                        elif pilihan_key == 'warna' :
                            while True :
                                new_value = input('Warna : ')
                                if new_value.isalpha() :
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],new_value,katalog['stok'][i],katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Warna hanya boleh berisi alfabet****')

                        #Ubah stok
                        elif pilihan_key == 'stok' :
                            while True : #Stok
                                new_value = input('Jumlah stok : ')
                                if new_value.isdigit() :
                                    new_value = int(new_value)
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],new_value,katalog['harga'][i])
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Jumlah stok harus angka positif****')

                        #Ubah harga
                        elif pilihan_key == 'harga' :
                            while True : #Harga
                                new_value = input('Harga satuan (IDR) : ')
                                if new_value.isdigit() :
                                    new_value = int(int(new_value)/1000) #Mengubah ke ribuan
                                    while True : #Verifikasi ubah data
                                        print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],new_value)
                                        verif_edit = input('\nApakah data sudah benar? (Y/N) : ').lower()
                                        if verif_edit in ['y','n'] :
                                            break
                                        
                                    if verif_edit == 'y' :
                                        katalog[pilihan_key][i] = new_value
                                        print('\n****Data berhasil diubah****')
                                    else :
                                        print('\n****Perubahan dibatalkan****')
                                    break
                                else :
                                    print('\n****Harga harus angka positif****')
                        break
                    else :
                        print('\n****Harap memasukkan kategori field yang ada****')
            break
        else :
            print('\n****Kode hanya boleh berisi alfanumerik dan tanda strip(-)****')

def delete_phone() :
    show_list()
    kode_hapus = input('\nMasukkan kode HP yang ingin dihapus? : ')
    if kode_hapus in katalog['kode']:
        i = katalog['kode'].index(kode_hapus)
        while True : #Verifikasi
            print_temp(katalog['kode'][i],katalog['seri'][i],katalog['tipe'][i],katalog['ram'][i],katalog['internal'][i],katalog['warna'][i],katalog['stok'][i],katalog['harga'][i])
            verif_delete = input('\nYakin ingin menghapus data ini? (Y/N) : ').lower()
            if verif_delete in ['y','n'] :
                break

        if verif_delete == 'y' :
            for key in katalog.keys() :
                del katalog[key][i]
        print('****Data {} sudah terhapus****'.format(kode_hapus))
    else:
        print('****Data tidak ada****')
    
def sell_phone() :
    while True :
        show_list()
        while True :
            i = input('HP nomor berapa yang ingin dibeli? : ')
            if i.isdigit() :
                i = int(i)
                if i <= len(katalog['kode']) :
                    i = int(i)-1 #convert nomor ke index
                    break
                else :
                    print('\n****Nomor tidak ada di katalog****')
            else :
                print('\n****Hanya menerima input angka positif****')
        while True :
            qty = input('Berapa banyak? : ')
            if qty.isdigit() :
                qty = int(qty)
                if qty > katalog['stok'][i] :
                    print('Stok tidak cukup, stok {tipe} tinggal {stok}'.format(tipe=katalog['tipe'][i],stok=katalog['stok'][i]))
                else :
                    harga_total = qty * katalog['harga'][i] #untuk satu barang
                    keranjang.append([katalog['tipe'][i], qty, katalog['harga'][i], harga_total, katalog['kode'][i]])
                    print('Isi Keranjang :')
                    print('|Nama\t\t| Qty\t| Harga\t| Total\t|')
                    for item in keranjang :
                        print('|{tipe}\t| {qty}\t| {harga}k\t| {total}k\t|'.format(tipe=item[0], qty=item[1], harga=item[2], total=item[3]))
                    break
            else :
                print('\n****Hanya menerima input angka positif****')

        while True :
            lagi = input('\nMau beli yang lain? (Y/N) : ').lower()
            if lagi in ['y','n'] :
                break

        if lagi == 'n' : #stop looping saat tidak ingin menambah keranjang belanja lagi
            break
  
    print('Daftar Belanja :')
    print('|Nama\t\t| Qty\t| Harga\t| Total\t|')
    harga_final = 0 #Total semua barang
    for item in keranjang :
        print('|{tipe}\t| {qty}\t| {harga}k\t| {total}k\n|'.format(tipe=item[0], qty=item[1], harga=item[2], total=item[3]))
        harga_final += item[3]
    while True :
        print('\nTotal Yang Harus Dibayar = {}k'.format(harga_final))
        while True : #Harga
            jumlah_uang = input('Masukkan jumlah uang (IDR) : ')
            if jumlah_uang.isdigit() :
                jumlah_uang = int(int(jumlah_uang)/1000) #Mengubah ke ribuan
                break
            else :
                print('\n****Jumlah uang harus angka positif****')

        if(jumlah_uang > harga_final) :
            kembali = jumlah_uang - harga_final
            print('\n****Terima kasih, uang kembalian anda : {}k****'.format(kembali))
            for item in keranjang :
                i_stok = katalog['kode'].index(item[4])
                katalog['stok'][i_stok] -= item[1]
            keranjang.clear()
            break
        elif(jumlah_uang == harga_final) :
            print('\n****Terima kasih****')
            for item in keranjang :
                i_stok = katalog['kode'].index(item[4])
                katalog['stok'][i_stok] -= item[1]
            keranjang.clear()
            break
        else :
            kekurangan = harga_final - jumlah_uang
            print('****Uang anda kurang sebesar {}k****'.format(kekurangan))

#Menu Utama
while True :
    pilihanMenu = input('''
Selamat Datang di Toko HP Xiaomi
    1. Penjualan
    2. Menu Admin
    3. Keluar Aplikasi

Masukkan pilihan : ''')

    if(pilihanMenu == '1') :
        sell_phone()
    elif(pilihanMenu == '2') :
        input_sandi = input('Masukkan kata sandi :') #input sandi dari user
        admin_menu(input_sandi)
    elif(pilihanMenu == '3') :
        break
    else :
        print("\n****Pilihan yang Anda Masukkan Salah****")