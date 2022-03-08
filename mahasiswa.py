class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk,kelas):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__kelas = kelas


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020, 'D')
m2 = Mahasiswa('Bintang', '5210411185', 'Informatika', 2021,'D')
m3 = Mahasiswa('Satria', '521041164', 'Informatika', 2021,'D')


data_mahasiswa = [m1, m2, m3]

print('\nDaftar Mahasiswa\n')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim} dan masuk di Kelas {i._Mahasiswa__kelas}')