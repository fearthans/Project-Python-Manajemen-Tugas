class Tugasin:
    def __init__(self, name, deadline, priority, status):
        self.nama = name
        self.tenggat = deadline
        self.prioritas = priority
        self.status = status

    def __str__(self):
        line_length = 122
        hiasan = "-" * line_length  

        return f"\t\t\t\t\t\t| \t   {self.nama}\t\t | \t   {self.tenggat}\t\t\t| \t{self.prioritas}\t\t\t | \t{self.status}\t |\n" \
            f"\t\t\t\t\t\t{hiasan}"
    
class ManajemenTugas:
    def __init__(self):
        self.tugas = []
        self.tugas_selesai = []
        self.kategori = set()
        self.riwayat = []
        self.terurut = [] 
    
    def tambahtugas(self, name, deadline, priority, status):
        tugasku = Tugasin(name, deadline, priority, status)
        self.tugas.append(tugasku)
        self.kategori.add(status)

    def tugasselesai(self, task_name):
        for tugask in self.tugas:
            if tugask.nama == task_name:
                tugask.status = "S"
                self.tugas_selesai.append(tugask)
                self.riwayat.append(tugask)
                self.kategori.add("S")
                self.tugas.remove(tugask)
                break

    def mencaritugas(self, task_name):
        for tugas in self.tugas:
            if tugas.nama == task_name:
                return tugas
        return None

    def berprioritas(self):
        self.terurut = [] 
        terurut_p = []
        terurut_kp = []
        terurut_tp = [] 
        for tugas in self.tugas:
            if tugas.prioritas == "A":
                terurut_p.append(tugas)
            elif tugas.prioritas == "K":
                terurut_kp.append(tugas)
            elif tugas.prioritas == "T":
                terurut_tp.append(tugas)
        self.terurut = terurut_p + terurut_kp + terurut_tp
        n = len(self.terurut)
        for i in range(1, n):
            x = self.terurut[i]
            j = i - 1
            while j >= 0 and self.terurut[j].prioritas > x.prioritas:
                self.terurut[j + 1] = self.terurut[j]
                j -= 1
            self.terurut[j + 1] = x
        return self.terurut

    def tampilkantugas(self):
        if self.terurut:
            for tugas in self.terurut:
                print(tugas)
        else:
            for tugas in self.tugas:
                print(tugas)

    def tugasterselesaikan(self):
        if self.tugas_selesai:
            daftartugas()
            for tugasin in self.tugas_selesai:
                print(tugasin)
        else:
            print("Tidak ada tugas selesai.")

    def tampilkanriwayat(self):
        if self.riwayat:
            print("Riwayat Tugas")
            daftartugas()
            for tugasin in self.riwayat + self.tugas_selesai:
                print(tugasin)
        else:
            print("Tidak Ada Riwayat")

def menutugas() :
    print("""
    \t\t\t\t\t\t\t========================================= UNLIMITED PRODUCTIVITY =================================
    \t\t\t\t\t\t\t================================================ LIMITY ==========================================
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \tKODE\t | \t\t\t\tPERINTAH\t\t\t\t\t |
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \t1\t | \t\tMENAMBAHKAN TUGAS\t\t\t\t\t\t | 
    \t\t\t\t\t\t\t| \t2\t | \t\tMENANDAI TUGAS SELESAI\t\t\t\t\t\t |
    \t\t\t\t\t\t\t| \t3\t | \t\tMENCARI TUGAS\t\t\t\t\t\t\t |
    \t\t\t\t\t\t\t| \t4\t | \t\tURUTKAN TUGAS BERDASARKAN TENGGAT PRIORITAS\t\t\t | 
    \t\t\t\t\t\t\t| \t5\t | \t\tMENAMPILKAN KESELURUHAN TUGAS\t\t\t\t\t | 
    \t\t\t\t\t\t\t| \t6\t | \t\tMENAMPILKAN TUGAS YANG TELAH SELESAI\t\t\t\t |
    \t\t\t\t\t\t\t| \t7\t | \t\tMENAMPILKAN RIWAYAT TUGAS SELESAI\t\t\t\t |
    \t\t\t\t\t\t\t==================================================================================================
    """)

def daftartugas():
    print("""\t\t\t\t\t\t==========================================================================================================================
    \t\t\t\t\t\t| \tNAMA TUGAS\t\t | \t\tTENGGAT WAKTU\t\t| \tPRIORITAS\t\t |    STATUS\t |
    \t\t\t\t\t\t==========================================================================================================================
    """)

def instruksi () :
    print(""" 
    \t\t\t\t\t\t\t=====================================\t   INSTRUKSI \t==========================================
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \tKODE\t | \tPRIORITAS\t    | \t KODE\t | \t\tSTATUS\t\t\t |
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \t A\t | \tPENTING\t\t    | \t  M\t | \t\tMELAKUKAN\t\t |
    \t\t\t\t\t\t\t| \t K\t | \tKURANG PENTING\t    | \t  SB\t | \t\tSEDANG BERLANGSUNG\t |
    \t\t\t\t\t\t\t| \t T\t | \tTIDAK PENTING\t    | \t  S\t | \t\tSELESAI\t\t\t |
    \t\t\t\t\t\t\t==================================================================================================
    """)

menutugas()
instruksi()
limity = ManajemenTugas()
tekan = "y"
while tekan == "y":
    kode = int(input("Masukkan Kode Untuk Menjalankan Perintah Pada Limity: "))
    if kode == 1 :
        nama = input("Nama Tugas: ")
        tenggat = input("Tenggat Waktu: ")
        prioritas = input("Prioritas: ")
        status = input("Status: ")
        limity.tambahtugas(nama, tenggat, prioritas, status)
        print("Tugas berhasil ditambahkan")

    elif kode == 2 :
        tugasselesai = input("Nama Tugas Yang Telah Selesai: ")
        limity.tugasselesai(tugasselesai)
        print("Tugas Berhasil Ditandai")

    elif kode == 3 :
        mencari = input("Nama Tugas Yang Akan Dicari: ")
        temu = limity.mencaritugas(mencari)
        if temu :
            print("Tugas Ditemukan")
            print(temu)
        else:
            print("Tugas Tidak Ditemukan")

    elif kode == 4 :
        print("Tugas Berhasil Diurutkan Berdasarkan Prioritas")
        limity.berprioritas()
        limity.tugas = limity.terurut

    elif kode == 5:
        daftartugas()
        limity.tampilkantugas()
        print("Daftar Tugas")
        
    elif kode == 6 :
        print("Tugas Yang Telah Selesai")
        limity.tugasterselesaikan()
    
    elif kode == 7:
        limity.tampilkanriwayat()

    else :
       break
    tekan = input("Tekan Y untuk melanjutkan: ")