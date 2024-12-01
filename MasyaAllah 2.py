import csv
import os
import datetime as dt

def clear():
    os.system("cls"if os.name == "nt" else "clear")

def garis(a, b=114):
    print(a * b)

def cover(b=114):
    garis("₊˚ʚ 🌱 ₊˚✧ ﾟ.", b)
    print("".center(b))
    print("██████╗  ██████╗ ██████╗ ██╗██████╗ ███████╗███╗   ██╗████████╗".center(b))
    print("██╔══██╗██╔════╝ ██╔══██╗██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝".center(b))
    print("███████║██║  ███╗██████╔╝██║██████╔╝█████╗  ██╔██╗ ██║   ██║   ".center(b))
    print("██╔══██║██║   ██║██╔══██╗██║██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ".center(b))
    print("██║  ██║╚██████╔╝██║  ██║██║██║  ██║███████╗██║ ╚████║   ██║   ".center(b))
    print("╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝".center(b))
    print("".center(b))
    garis("₊˚ʚ 🌱 ₊˚✧ ﾟ.", b)

def enter(a=""):
    input(f"{a}tekan [ENTER] untuk melanjutkan >> ")

# Fungsi menu awal
def halaman_awal():
    clear()
    cover()
    print("""
                                                1. REGISTRASI
                                                2. LOGIN SEBAGAI ADMIN
                                                3. LOGIN SEBAGAI PENYEWA
                                                4. EXIT
""")
    garis("=")
    while True :
        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                clear()
                registrasi_penyewa()
                break
            elif pilih == 2:
                clear()
                login_admin()
            elif pilih == 3:
                clear()
                login_penyewa()
            elif pilih == 4:
                exit_program()
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")
            halaman_awal ()

# Fungsi registrasi untuk penyewa
def registrasi_penyewa():
    while True:
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        
        # Validasi NIK
        while True:
            nik = input("Masukkan NIK (16 digit): ")
            if len(nik) == 16 and nik.isdigit():
                break
            else:
                print("NIK harus berupa 16 digit angka. Silakan coba lagi.")
        
        # Validasi Nomor Telepon
        nomor_telepon = input("Masukkan Nomor Telepon: ")

        # Periksa duplikasi data
        if cek_duplikasi('datapenyewa.csv', username, nik, nomor_telepon):
            print("\nPendaftaran gagal. Username, NIK, atau Nomor Telepon sudah terdaftar.\n")
        else:
            # Simpan data jika tidak ada duplikasi
            simpan_data('datapenyewa.csv', [username, password, nik, nomor_telepon])
            print("\nPendaftaran berhasil. Silakan login.\n")
            
            # Tampilkan menu login khusus penyewa setelah registrasi
            while True:
                clear()
                print("""
                                                1. LOGIN SEBAGAI PENYEWA
                                                2. EXIT
                """)
                garis("=")
                try:
                    pilih = int(input("Pilih Opsi yang tersedia >> "))
                    if pilih == 1:
                        clear()
                        login_penyewa()
                    elif pilih == 2:
                        exit_program()
                    else:
                        print("Opsi yang Anda pilih tidak tersedia.")
                except ValueError:
                    print("Masukkan input dalam bentuk angka.")
            break

# Fungsi login untuk admin
def login_admin():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if cek_login('dataadmin.csv', username, password):
        print("Login berhasil sebagai Admin.")
    else:
        print("Login gagal. Username atau password salah.")

# Fungsi login untuk penyewa
def login_penyewa():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if cek_login('datapenyewa.csv', username, password):
            print("Login berhasil sebagai Penyewa.")
            while True:
                clear()
                print(f"Selamat datang, {username}!")
                beranda_penyewa(username)
                break  # Kembali ke menu login utama setelah logout
            break  # Setelah login berhasil, keluar dari loop login
        else:
            print("Login gagal. Username atau password salah.")
            continue  # Mengulang input jika login gagal

# Fungsi untuk menyimpan data ke CSV
def simpan_data(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Fungsi untuk memeriksa login dari CSV
def cek_login(filename, username, password):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False
    except FileNotFoundError:
        return False
    
def baca_data(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    
# Fungsi untuk mengecek apakah data sudah ada
def cek_duplikasi(filename, username, nik, nomor_telepon):
    data = baca_data(filename)
    for row in data:
        if row[0] == username or row[2] == nik or row[3] == nomor_telepon:
            return True  # Duplikasi ditemukan
    return False

# Fungsi untuk menampilkan pesan terima kasih dan keluar
def exit_program():
    clear()
    print("\n")
    print("Terima kasih telah menggunakan program ini\n\n".center(114))
    garis("=", 114)
    exit()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BERANDA PENYEWA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk beranda penyewa
def beranda_penyewa(username):
    while True:
        clear()
        print(f"Selamat datang, {username}!")
        print("""
                                                1. LIHAT STOK BARANG
                                                2. LIHAT RIWAYAT PENYEWAAN
                                                3. PENGEMBALIAN BARANG
                                                4. KEMBALI KE MENU UTAMA
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih opsi yang tersedia >> "))
            if pilihan == 1:
                lihat_stok_barang()  # Panggil fungsi stok barang
            elif pilihan == 2:
                tampilkan_riwayat_penyewaan()
            elif pilihan == 3:
                pengembalian_barang(username)
            elif pilihan == 4:
                halaman_awal()  # Kembali ke menu utama
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
                enter()
        except ValueError:
            print("Masukkan input dalam bentuk angka.")
            enter()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIHAT STOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk menampilkan stok barang
def lihat_stok_barang():
    stok_barang = baca_data_barang()
    if not stok_barang:
        print("Stok barang tidak tersedia atau file tidak ditemukan.")
        return None

    # Menampilkan tabel stok barang
    garis("=")
    print(f"{'Nama Barang':<30}{'Harga Sewa/Hari':<20}{'Total Stok':<10}")
    garis("-")
    for nama, info in stok_barang.items():
        print(f"{nama:<30}Rp {info['harga']:<19}{info['stok']:<10}")
    garis("=")

    # Menambahkan menu setelah stok barang ditampilkan
    while True:
        print("""
            1. Sewa Barang
            2. Kembali ke Menu
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih Opsi yang tersedia >> "))
            if pilihan == 1:
                sewa_barang(stok_barang)  # Panggil fungsi sewa_barang
                break
            elif pilihan == 2:
                break  # Kembali ke menu sebelumnya
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menyimpan data barang ke CSV setelah diubah
def simpan_data_barang(stok_barang):
    with open('databarang.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Barang', 'Harga Sewa', 'Total Stok'])
        for nama, info in stok_barang.items():
            writer.writerow([nama, info['harga'], info['stok']])

# Fungsi untuk menyewa barang
def sewa_barang(stok_barang):
    if not stok_barang:
        print("Stok barang tidak ditemukan.")
        return None

    while True:
        nama_barang = input("Masukkan nama barang yang ingin disewa: ").strip()
        if nama_barang in stok_barang:
            break  # Jika barang ditemukan, keluar dari loop
        else:
            print("Barang tidak ditemukan. Coba lagi.")  # Menampilkan pesan dan meminta input ulang

    try:
        # Validasi input jumlah barang yang ingin disewa
        while True:
            try:
                jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin disewa: "))
                if jumlah <= 0:
                    print("Jumlah barang yang disewa harus lebih dari 0.")
                    continue
                if jumlah > stok_barang[nama_barang]['stok']:
                    print("Stok tidak mencukupi.")
                    continue
                break  # Jika jumlah valid, keluar dari loop
            except ValueError:
                print("Jumlah barang harus berupa angka yang valid.")

        # Validasi tanggal penyewaan
        while True:
            try:
                tanggal_mulai_input = input("Masukkan tanggal penyewaan (YYYY-MM-DD): ")
                tanggal_mulai = dt.datetime.strptime(tanggal_mulai_input, "%Y-%m-%d")
                break  # Jika format tanggal benar, keluar dari loop
            except ValueError:
                print("Format tanggal salah! Pastikan format yang benar adalah YYYY-MM-DD.")
        
        # Validasi durasi penyewaan
        while True:
            try:
                durasi_hari = int(input("Masukkan durasi penyewaan (hari): "))
                if durasi_hari <= 0:
                    print("Durasi penyewaan harus lebih dari 0 hari.")
                    continue
                break  # Jika durasi valid, keluar dari loop
            except ValueError:
                print("Durasi penyewaan harus berupa angka.")

        # Menentukan tanggal kembali
        tanggal_kembali = tanggal_mulai + dt.timedelta(days=durasi_hari)
        
        # Menampilkan informasi tanggal penyewaan dan pengembalian
        print(f"Tanggal penyewaan: {tanggal_mulai.strftime('%Y-%m-%d')}")
        print(f"Tanggal pengembalian: {tanggal_kembali.strftime('%Y-%m-%d')}")

        total_harga = jumlah * stok_barang[nama_barang]['harga'] * durasi_hari

        # Mengurangi stok barang
        stok_barang[nama_barang]['stok'] -= jumlah

        # Meminta username
        username = input("Masukkan username Anda: ").strip()

        # Menambahkan status "Disewa" pada data penyewaan
        status = "Disewa"

        # Simpan perubahan ke databarang.csv
        simpan_data_barang(stok_barang)

        # Simpan transaksi ke datapenyewaan.csv dengan format yang diminta
        simpan_data('datapenyewaan.csv', [username, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai.strftime('%Y-%m-%d'), tanggal_kembali.strftime('%Y-%m-%d'), status])

        print(f"Barang berhasil disewa. Total harga: Rp {total_harga:,}")
        return username, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai, tanggal_kembali, status

    except ValueError as e:
        print("Input tidak valid. Pastikan memasukkan angka dan format tanggal yang benar.")
        return None

# Fungsi Baca data stok dari CSV
def baca_data_barang():
    try:
        stok_barang = {}
        with open('databarang.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    stok_barang[row['Nama Barang']] = {
                        "harga": int(row['Harga Sewa']),
                        "stok": int(row['Total Stok']) if row['Total Stok'] else 0  # Tangani None atau kosong
                    }
                except (ValueError, TypeError) as e:
                    print(f"Data tidak valid untuk barang '{row.get('Nama Barang', 'Unknown')}': {e}")
        return stok_barang
    except FileNotFoundError:
        print("File databarang.csv tidak ditemukan.")
        return None

# Fungsi Menyimpan perubahan ke file stok
def simpan_data_barang(stok_barang):
    with open('databarang.csv', mode='w', newline='') as file:
        fieldnames = ['Nama Barang', 'Harga Sewa', 'Total Stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for nama, info in stok_barang.items():
            writer.writerow({
                "Nama Barang": nama,
                "Harga Sewa": info['harga'],
                "Total Stok": info['stok']
            })

# Fungsi untuk melihat riwayat penyewaan
# def lihat_riwayat_penyewaan(username):
#     clear()
#     print("RIWAYAT PENYEWAAN ANDA".center(114))
#     garis("=")
#     riwayat = baca_data('riwayatpenyewaan.csv')
#     user_riwayat = [row for row in riwayat if row[0] == username]
#     if not user_riwayat:
#         print("Anda belum memiliki riwayat penyewaan.")
#     else:
#         print(f"{'Nama Barang':<30}{'Tanggal Sewa':<20}{'Tanggal Kembali':<20}{'Status':<15}")
#         garis("-")
#         for row in user_riwayat:
#             print(f"{row[1]:<30}{row[2]:<20}{row[3]:<20}{row[4]:<15}")
#     garis("=")
#     enter()

# # Fungsi untuk pengembalian barang
# def pengembalian_barang(username):
#     clear()
#     print("PENGEMBALIAN BARANG".center(114))
#     garis("=")
#     riwayat = baca_data('riwayatpenyewaan.csv')
#     barang = baca_data('databarang.csv')
#     user_riwayat = [row for row in riwayat if row[0] == username and row[4].lower() == "belum dikembalikan"]

#     if not user_riwayat:
#         print("Anda tidak memiliki barang yang harus dikembalikan.")
#     else:
#         print(f"{'No':<5}{'Nama Barang':<30}{'Tanggal Sewa':<20}")
#         garis("-")
#         for i, row in enumerate(user_riwayat, start=1):
#             print(f"{i:<5}{row[1]:<30}{row[2]:<20}")

#         try:
#             pilihan = int(input("Pilih nomor barang yang akan dikembalikan >> "))
#             if 1 <= pilihan <= len(user_riwayat):
#                 barang_dikembalikan = user_riwayat[pilihan - 1]
#                 # Update status pengembalian
#                 for row in riwayat:
#                     if row == barang_dikembalikan:
#                         row[4] = "Sudah Dikembalikan"

#                 # Update stok barang
#                 for item in barang:
#                     if item[0].lower() == barang_dikembalikan[1].lower():
#                         item[2] = str(int(item[2]) + 1)
#                         break

#                 # Simpan perubahan
#                 simpan_data_csv('riwayatpenyewaan.csv', riwayat)
#                 simpan_data_csv('databarang.csv', barang)

#                 print(f"Barang '{barang_dikembalikan[1]}' berhasil dikembalikan.")
#             else:
#                 print("Nomor barang yang Anda pilih tidak valid.")
#         except ValueError:
#             print("Masukkan input dalam bentuk angka.")
#     garis("=")
#     enter()

# Fungsi untuk menyimpan data ke file CSV (overwrite)
def simpan_data_csv(filename, data):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RIWAYAT PENYEWAAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Fungsi utama untuk menjalankan program
import csv
import datetime as dt

# def tampilkan_riwayat_penyewaan():
#     try:
#         # Menggunakan nama file langsung (relatif ke lokasi script)
#         file_name = 'datapenyewaan.csv'
#         riwayat_penyewaan = []

#         # Membaca file CSV
#         with open(file_name, 'r') as file:
#             reader = csv.reader(file)
#             header = next(reader)  # Membaca header

#             for row in reader:
#                 username = row[0]
#                 nama_barang = row[1]
#                 jumlah = int(row[2])
#                 durasi_hari = int(row[3])
#                 total_harga = int(row[4])
#                 tanggal_mulai = row[5]
#                 tanggal_kembali = row[6]
                
#                 # Menentukan status penyewaan
#                 tanggal_kembali_obj = dt.datetime.strptime(tanggal_kembali, "%Y-%m-%d")
#                 hari_ini = dt.datetime.now()
#                 status = "Selesai" if hari_ini > tanggal_kembali_obj else "Sedang Berjalan"

#                 # Menyimpan data
#                 riwayat_penyewaan.append([
#                     username, nama_barang, jumlah, durasi_hari,
#                     total_harga, tanggal_mulai, tanggal_kembali, status
#                 ])

#         # Menampilkan tabel secara manual
#         print("\nRiwayat Penyewaan Barang:")
#         print("-" * 100)
#         print(f"{'Username':<15} {'Barang':<15} {'Jumlah':<10} {'Durasi':<10} {'Total Harga':<15} {'Tgl Mulai':<12} {'Tgl Kembali':<12} {'Status':<15}")
#         print("-" * 100)

#         for row in riwayat_penyewaan:
#             print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} Rp {row[4]:<12,} {row[5]:<12} {row[6]:<12} {row[7]:<15}")

#         print("-" * 100)

#     except FileNotFoundError:
#         print("File 'datapenyewaan.csv' tidak ditemukan di direktori saat ini.")
#     except Exception as e:
#         print(f"Terjadi kesalahan: {e}")

# # Memanggil fungsi
# tampilkan_riwayat_penyewaan()

# Memanggil fungsi

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PENGEMBALIAN BARANG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk memuat data barang dari file CSV
def load_data_barang(filename):
    """Memuat data barang dari file CSV."""
    data = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                barang = row['Nama Barang'].lower()  
                harga_per_hari = int(row['Harga Sewa'])  
                data[barang] = harga_per_hari
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
    return data

# Fungsi untuk menghitung biaya pengembalian barang
def hitung_harga_pengembalian(barang, tanggal_pinjam, tanggal_kembali, harga_barang):
    """Menghitung harga pengembalian untuk barang tertentu."""
    if barang not in harga_barang:
        return None, "Barang tidak ditemukan dalam sistem."
    
    harga_per_hari = harga_barang[barang]
    tanggal_pinjam = datetime.strptime(tanggal_pinjam, "%Y-%m-%d")
    tanggal_kembali = datetime.strptime(tanggal_kembali, "%Y-%m-%d")
    jumlah_hari = (tanggal_kembali - tanggal_pinjam).days
    
    if jumlah_hari < 0:
        return None, "Error: Tanggal kembali tidak boleh lebih awal dari tanggal pinjam."
    
    total_harga = jumlah_hari * harga_per_hari
    return total_harga, None

# Fungsi untuk memproses pembayaran hingga mencukupi
def proses_pembayaran(total_harga):
    while True:
        try:
            jumlah_uang = float(input("Masukkan jumlah uang yang dibayarkan: "))
            if jumlah_uang >= total_harga:
                print("Pembayaran berhasil! Terima kasih telah menggunakan layanan kami.")
                break
            else:
                kekurangan = total_harga - jumlah_uang
                print(f"Uang Anda kurang sebesar Rp{kekurangan}. Silakan tambahkan.")
        except ValueError:
            print("Input tidak valid. Masukkan jumlah uang dalam angka.")

# # Fungsi untuk menampilkan pesan selamat datang
# def selamat_datang():
#     print("="*50)
#     print(" SELAMAT DATANG DI SISTEM PENYEWAAN ALAT PERTANIAN ")
#     print("="*50)
#     print("Silakan kembalikan barang yang telah Anda sewa.\n")

# Menjalankan sistem pengembalian barang
# selamat_datang()

# # Memuat data barang dari file CSV
# harga_barang = load_data_barang('databarang.csv')
# if not harga_barang:
#     print("Gagal memuat data barang. Pastikan file 'databarang.csv' tersedia.")
# else:
#     total_harga_semua = 0
#     print("Masukkan barang yang ingin dikembalikan (ketik 'selesai' jika sudah selesai):")
#     while True:
#         barang = input("Masukkan nama barang: ").lower()
        
#         if barang == "selesai":
#             break
        
#         if barang not in harga_barang:
#             print("Barang tidak ditemukan dalam sistem. Silakan coba lagi.")
#             continue
        
#         tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
#         tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
        
#         total_harga, error = hitung_harga_pengembalian(barang, tanggal_pinjam, tanggal_kembali, harga_barang)
        
#         if error:
#             print(error)
#         else:
#             total_harga_semua += total_harga
#             print(f"Barang: {barang.capitalize()}, Total harga: Rp{total_harga}\n")

#     if total_harga_semua > 0:
#         print(f"\nTotal harga semua barang yang harus dibayar: Rp{total_harga_semua}")
#         proses_pembayaran(total_harga_semua)
#     else:
#         print("Tidak ada barang yang dikembalikan.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BERANDA ADMIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Tambahkan fungsi beranda admin
def beranda_admin():
    while True:
        clear()
        print("""
                                                    BERANDA ADMIN
        """)
        garis("=")
        print("""
                                                1. MELIHAT STOK BARANG
                                                2. MELIHAT RIWAYAT PENYEWAAN
                                                3. KEMBALI KE MENU UTAMA
        """)
        garis("=")

        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                clear()
                menu_stok_barang()
            elif pilih == 2:
                clear()
                lihat_riwayat_penyewaan()
            elif pilih == 3:
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menu stok barang
def menu_stok_barang():
    while True:
        clear()
        print("Stok Barang Saat Ini:\n")
        garis("-")
        barang = baca_data('databarang.csv')
        if barang:
            for i, row in enumerate(barang):
                print(f"{i + 1}. Nama Barang: {row[0]} | Stok: {row[1]}")
        else:
            print("Tidak ada data stok barang.")
        garis("-")

        print("""
                                                1. TAMBAH STOK BARANG
                                                2. KEMBALI KE BERANDA ADMIN
        """)
        garis("=")
        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                tambah_stok_barang()
            elif pilih == 2:
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menambah stok barang
def tambah_stok_barang():
    # Membaca data barang dari file CSV
    barang = baca_data('databarang.csv')
    
    # Memasukkan nama barang
    nama_barang = input("Masukkan nama barang: ").strip()
    
    # Periksa apakah barang sudah ada
    barang_ditemukan = False
    for row in barang:
        # Validasi: Pastikan baris memiliki setidaknya 3 kolom
        if len(row) >= 3 and row[0].lower() == nama_barang.lower():
            try:
                jumlah_tambah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
                row[2] = str(int(row[2]) + jumlah_tambah)  # Update stok barang
                print(f"\nStok barang '{nama_barang}' berhasil ditambahkan sebanyak {jumlah_tambah}.")
                barang_ditemukan = True
                break
            except ValueError:
                print("Input jumlah stok harus berupa angka. Silakan coba lagi.")
                return

    if not barang_ditemukan:
        # Jika barang belum ada, tambahkan barang baru
        try:
            harga_barang = int(input("Masukkan harga barang: "))
            jumlah_stok = int(input("Masukkan jumlah stok barang: "))
            barang.append([nama_barang, str(harga_barang), str(jumlah_stok)])
            print(f"\nBarang baru '{nama_barang}' berhasil ditambahkan dengan harga {harga_barang} dan stok {jumlah_stok}.")
        except ValueError:
            print("Input harga dan stok harus berupa angka. Silakan coba lagi.")
            return

    # Simpan perubahan ke file CSV
    try:
        with open('databarang.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(barang)
        print("\nPerubahan telah disimpan ke dalam file.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")
    
    enter("")

# Fungsi untuk membaca data dari file CSV
def baca_data(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader if len(row) > 0]  # Hapus baris kosong
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan. Membuat file baru...")
        return []  # Kembalikan list kosong jika file tidak ditemukan


# Fungsi untuk melihat riwayat penyewaan
# def lihat_riwayat_penyewaan():
#     print("\nRiwayat Penyewaan:\n")
#     garis("-")
#     penyewaan = baca_data('riwayatpenyewaan.csv')
#     if penyewaan:
#         for row in penyewaan:
#             print(f"Penyewa: {row[0]} | Barang: {row[1]} | Tanggal: {row[2]} | NIK: {row[3]} | Nomor Telepon: {row[4]}")
#     else:
#         print("Tidak ada riwayat penyewaan.")
#     garis("-")
#     enter()

def lihat_riwayat_penyewaan():
    try:
        # Menggunakan nama file langsung (relatif ke lokasi script)
        file_name = 'datapenyewaan.csv'
        riwayat_penyewaan = []

        # Membaca file CSV
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Membaca header

            for row in reader:
                username = row[0]
                nama_barang = row[1]
                jumlah = int(row[2])
                durasi_hari = int(row[3])
                total_harga = int(row[4])
                tanggal_mulai = row[5]
                tanggal_kembali = row[6]
                
                # Menentukan status penyewaan
                tanggal_kembali_obj = dt.datetime.strptime(tanggal_kembali, "%Y-%m-%d")
                hari_ini = dt.datetime.now()
                status = "Selesai" if hari_ini > tanggal_kembali_obj else "Sedang Berjalan"

                # Menyimpan data
                riwayat_penyewaan.append([
                    username, nama_barang, jumlah, durasi_hari,
                    total_harga, tanggal_mulai, tanggal_kembali, status
                ])

        # Menampilkan tabel secara manual
        print("\nRiwayat Penyewaan Barang:")
        print("-" * 100)
        print(f"{'Username':<15} {'Barang':<15} {'Jumlah':<10} {'Durasi':<10} {'Total Harga':<15} {'Tgl Mulai':<12} {'Tgl Kembali':<12} {'Status':<15}")
        print("-" * 100)

        for row in riwayat_penyewaan:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} Rp {row[4]:<12,} {row[5]:<12} {row[6]:<12} {row[7]:<15}")

        print("-" * 100)

    except FileNotFoundError:
        print("File 'datapenyewaan.csv' tidak ditemukan di direktori saat ini.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi
lihat_riwayat_penyewaan()

# Perbarui login admin untuk menampilkan beranda admin
def login_admin():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if cek_login('dataadmin.csv', username, password):
        print("\nLogin berhasil sebagai Admin.")
        enter()
        beranda_admin()
    else:
        print("Login gagal. Username atau password salah.")
        enter()

if __name__ == "__main__":
    clear()
    cover()
    enter("SELAMAT DATANG DI TEMPAT SEWA KAMI, AGRIRENT:). ")
    halaman_awal()
    beranda_penyewa()
    tampilkan_riwayat_penyewaan()
    load_data_barang
    beranda_admin()





