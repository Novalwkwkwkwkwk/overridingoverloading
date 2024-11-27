class Buah:
    Rasa = ""
    Manfaat = ""

    def Nama(self):
        print()

class Jenis(Buah):
    def Nama(self, nama_buah=None):
        # Overloading metode Nama dengan parameter opsional
        if nama_buah:
            print(f"Buah {nama_buah}")
        else:
            super().Nama()  # Memanggil metode Nama dari kelas Buah

    def Lokal(self):
        print("Rasanya Enak,", self.Rasa, "&", self.Manfaat)


labrador = Jenis()

labrador.Rasa = "Manis"
labrador.Manfaat = "Segar"

labrador.Nama("Apel")

labrador.Nama("Jeruk")

labrador.Lokal()
