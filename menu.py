class menuMinuman:
    def __init__(self, nama, deskripsi, harga,toping):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__toping = toping


mnm1 = menuMinuman('Jus Apel', 'Jus apel yang dipetik dari kebun sendiri ', 30000, 'ChocoChips')
mnm2 = menuMinuman('Jus Semangka','Jus Semangka dengan semangka premium', 20000, 'Puding')
mnm3 = menuMinuman('Orange Jus With Cookies','Orange Jus Dengan Jeruk asli', 20000, 'Puding')


pilihanMenu = [mnm1, mnm2, mnm3,]
print('\nDaftar Menu Healthy Fruits\n')

for i in pilihanMenu:
    print('{} harga Rp. {}, {} dengan toping {}'.format(i.nama, i.harga, i.deskripsi,i._menuMinuman__toping))