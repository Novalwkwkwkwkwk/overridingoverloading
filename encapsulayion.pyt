class Makanan:
    def __init__(self, variabel_privat, variabel_proteksi):
        self.__variabel_privat = variabel_privat  # Variabel privat
        self._variabel_proteksi = variabel_proteksi  # Variabel proteksi

    def tampilkan(self):
        # Menampilkan nilai dari variabel privat dan proteksi
        print(f"Variabel Privat: {self.__variabel_privat}")
        print(f"Variabel Proteksi: {self._variabel_proteksi}")

# Kelas Turunan di luar Kelas Makanan
class MakananTurunan(Makanan):
    def akses_proteksi(self):
        # Mengakses variabel proteksi dari kelas induk
        print(f"Mengakses Variabel Proteksi: {self._variabel_proteksi}")