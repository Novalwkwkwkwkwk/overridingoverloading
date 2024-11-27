class Buah:
    Rasa = ""
    Warna = ""

    def Nama(self):
        print("Buah Apel")

class Jenis(Buah):
    
    def Lokal(self):

        print ("Rasanya Enak,",self.Rasa,"&", self.Warna)
    

labrador = Jenis()

labrador .Rasa = "Manis" 
labrador .Warna = "Merah"
labrador .Nama()

labrador .Lokal()





