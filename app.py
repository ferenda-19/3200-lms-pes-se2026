import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN
# ---------------------------------------------------------
st.set_page_config(
    page_title="MOOC Pelatihan Petugas PES SE2026",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling CSS (Kontras Tinggi & Warna Judul Konsisten)
st.markdown("""
    <style>
    .main-title {
        color: #FBBF24;
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #F3F4F6;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# URL GOOGLE APPS SCRIPT WEB APP & SPREADSHEET CSV READ
# ---------------------------------------------------------
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwNeU_2Hi2pfbzedgoN-kRnsyqlKP8nwbIwLSqkpsRUf4Hr5s5Rw2cV-8iyhe1JdbvN/exec"

SPREADSHEET_ID = "1JOudkfgyJrlc2iTlsKofHNja3Xkn2NgLV4D1k-_9jd4"
CSV_READ_ABSENSI_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv"
CSV_READ_KUIS_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet=Nilai%20Kuis"

def load_data_absensi():
    try:
        df = pd.read_csv(CSV_READ_ABSENSI_URL)
        return df.dropna(how="all")
    except Exception:
        return pd.DataFrame()

def load_data_kuis():
    try:
        df = pd.read_csv(CSV_READ_KUIS_URL)
        return df.dropna(how="all")
    except Exception:
        return pd.DataFrame()

# ---------------------------------------------------------
# NAVIGATION / SIDEBAR
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/000000/google-classroom.png", width=80)
st.sidebar.title("MOOC PES SE2026")
st.sidebar.caption("Sensus Ekonomi 2026 - BPS Provinsi Jawa Barat")

menu = st.sidebar.radio(
    "Navigasi Menu:",
    [
        "🏠 Homepage", 
        "📅 Jadwal MOOC (2 Hari)", 
        "📂 Bahan & Materi", 
        "📝 Absensi Harian", 
        "✏️ Kuis Asynchronous"
    ]
)

st.sidebar.divider()
st.sidebar.info("💡 **Petunjuk:** Pastikan Anda mengisi absensi setiap hari dan menyelesaikan kuis sesuai jadwal.")

# ---------------------------------------------------------
# 1. HOMEPAGE
# ---------------------------------------------------------
if menu == "🏠 Homepage":
    st.markdown("<div class='main-title'>Selamat Datang di MOOC Pelatihan Petugas PES SE2026</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Portal Pembelajaran Mandiri (MOOC) Petugas Pendataan Post Enumeration Survey Sensus Ekonomi 2026</div>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 👋 Halo, Calon Petugas PES SE2026!
        Selamat datang di platform *Massive Open Online Course* (MOOC). Pelatihan ini dirancang untuk membekali Anda dengan pengetahuan dasar, metodologi, serta tata cara pendataan lapangan Post Enumeration Survey Sensus Ekonomi 2026.
        
        #### 📌 Alur Pelatihan (2 Hari):
        1. **Mempelajari Jadwal & Materi:** Unduh pedoman dan paparan materi di menu yang tersedia.
        2. **Mengisi Absensi:** Wajib dilakukan setiap hari pada menu **Absensi Harian**.
        3. **Mengerjakan Kuis Asynchronous:** Selesaikan kuis evaluasi Hari 1 & Hari 2 untuk mengukur pemahaman Anda.
        """)
        
        st.info("🔔 **Pengumuman:** Pastikan koneksi internet stabil saat mengunduh materi dan mengerjakan kuis Asynchronous.")

    with col2:
        st.markdown("### 📊 Ringkasan Pelatihan")
        st.metric(label="Durasi Pelatihan", value="2 Hari (Asynchronous)")
        st.metric(label="Metode", value="Mandiri / MOOC")
        st.metric(label="Status Pendaftaran", value="Aktif", delta="Terverifikasi")

# ---------------------------------------------------------
# 2. JADWAL MOOC (2 HARI)
# ---------------------------------------------------------
elif menu == "📅 Jadwal MOOC (2 Hari)":
    st.markdown("<div class='main-title'>📅 Jadwal Pelatihan MOOC PES SE2026</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Jadwal Pelaksanaan Mandiri (Asynchronous) 2 Hari Pelatihan</div>", unsafe_allow_html=True)
    st.divider()

    tab1, tab2 = st.tabs(["📌 Hari 1", "📌 Hari 2"])

    jadwal_hari1 = [
        {"Waktu (WIB)": "08.00 - 08.30", "Sesi": "Sesi 1", "Materi / Kegiatan": "Penjelasan Umum & Organisasi Lapangan PES SE2026", "Durasi": "30 Menit"},
        {"Waktu (WIB)": "08.30 - 09.15", "Sesi": "Sesi 2", "Materi / Kegiatan": "Metodologi & Mekanisme Pencacahan Lapangan", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "09.15 - 10.45", "Sesi": "Sesi 3", "Materi / Kegiatan": "Pemutakhiran E-Form PES.SE2026.P", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "10.45 - 11.00", "Sesi": "Istirahat", "Materi / Kegiatan": "Istirahat / Coffee Break", "Durasi": "15 Menit"},
        {"Waktu (WIB)": "11.00 - 11.45", "Sesi": "Sesi 4", "Materi / Kegiatan": "Tata Cara Bertanya & Teknik Wawancara Responden", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "11.45 - 13.00", "Sesi": "ISHOMA", "Materi / Kegiatan": "Istirahat, Sholat, & Pengisian Absensi Hari 1", "Durasi": "75 Menit"},
        {"Waktu (WIB)": "13.00 - 15.00", "Sesi": "Sesi 5", "Materi / Kegiatan": "Pencacahan E-Form PES.SE2026.L dan L.UB", "Durasi": "120 Menit"},
        {"Waktu (WIB)": "15.00 - 16.30", "Sesi": "Sesi 6", "Materi / Kegiatan": "Pengerjaan Kuis Asynchronous Hari 1", "Durasi": "90 Menit"}
    ]

    jadwal_hari2 = [
        {"Waktu (WIB)": "08.00 - 09.30", "Sesi": "Sesi 1", "Materi / Kegiatan": "Pengawasan, Pemeriksaan, & Penjaminan Kualitas Data", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "09.30 - 11.00", "Sesi": "Sesi 2", "Materi / Kegiatan": "Penanganan Kasus Batas (Boundary Cases) Lapangan", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "11.00 - 11.15", "Sesi": "Istirahat", "Materi / Kegiatan": "Istirahat / Coffee Break", "Durasi": "15 Menit"},
        {"Waktu (WIB)": "11.15 - 12.15", "Sesi": "Sesi 3", "Materi / Kegiatan": "Instalasi, Penggunaan CAPI, & Webmonitoring (Webmon)", "Durasi": "60 Menit"},
        {"Waktu (WIB)": "12.15 - 13.30", "Sesi": "ISHOMA", "Materi / Kegiatan": "Istirahat, Sholat, & Pengisian Absensi Hari 2", "Durasi": "75 Menit"},
        {"Waktu (WIB)": "13.30 - 14.30", "Sesi": "Sesi 4", "Materi / Kegiatan": "Rekonsiliasi Lapangan (E-Form RL)", "Durasi": "60 Menit"},
        {"Waktu (WIB)": "14.30 - 15.15", "Sesi": "Sesi 5", "Materi / Kegiatan": "Pendalaman & Penegasan Materi PES SE2026", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "15.15 - 16.30", "Sesi": "Sesi 6", "Materi / Kegiatan": "Pengerjaan Kuis Asynchronous Hari 2", "Durasi": "75 Menit"}
    ]

    with tab1:
        st.subheader("📋 Tabel Jadwal — Hari 1")
        df_h1 = pd.DataFrame(jadwal_hari1)
        st.dataframe(df_h1, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("📋 Tabel Jadwal — Hari 2")
        df_h2 = pd.DataFrame(jadwal_hari2)
        st.dataframe(df_h2, use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# 3. BAHAN & MATERI
# ---------------------------------------------------------
elif menu == "📂 Bahan & Materi":
    st.markdown("<div class='main-title'>📂 Bahan & Materi Pelatihan PES SE2026</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Unduh dan Pelajari Pustaka Resmi Pelatihan Mandiri (MOOC)</div>", unsafe_allow_html=True)
    st.divider()

    st.subheader("1. 📖 Buku Pedoman")
    st.markdown("""
    * **Buku 1 Pedoman Teknis PES SE2026** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1tXg_Lk232xKc3Lr6R52H3JLAkN0YS_4j/view?usp=drivesdk)
    * **Buku 2 Pedoman Innas PES SE2026** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1xDsrcrRmA9KQPxerE2if6bwoEvcymnom/view?usp=drivesdk)
    * **Buku 3 Pedoman Pemeriksa PES SE2026** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1VGoGgHk0_ikOdNUnYC1BVvHo_Mmb0z45/view?usp=drivesdk)
    """)

    st.divider()

    st.subheader("2. 🖥️ Bahan Ajar / Slide Paparan")
    st.markdown("""
    Akses seluruh slide paparan materi pelatihan (PowerPoint & PDF) melalui link utama berikut:
    
    👉 **[📂 Folder Utama Bahan Ajar & Slide Paparan PES SE2026](https://drive.google.com/drive/folders/1mL0bUSazXbfNwDRAS1NQsykPIaZ4q-FJ)**
    """)

    st.divider()

    st.subheader("3. 📋 Kuesioner & Instrumen Lapangan")
    st.markdown("""
    * **Kuesioner PES SE2026-L** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1B6ds_IlmN03IJo9JuLAh6k1gvF6kR0eo/view?usp=drivesdk)
    * **Kuesioner PES SE2026-L.UB** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1SyMtU1KNmdlfLyXkLMM4fqLil52nMWyW/view?usp=drivesdk)
    * **Kuesioner PES.SE2026-RLK** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1VtbdUEfdYaU2vWRSqHotjAMxJV_z53NH/view?usp=drivesdk)
    * **Kuesioner PES.SE2026-RLU** — [📄 Akses / Unduh File](https://drive.google.com/file/d/1ZV52vwxlao9HL-RHuvwdka3bAtG7U8aO/view?usp=drivesdk)
    * **Kuesioner PES.SE2026-RLAK** — [📄 Akses / Unduh File](https://drive.google.com/file/d/18mOfU_mJa0jJavsXfGTq3b5vXG80bEyI/view?usp=drivesdk)
    """)

# ---------------------------------------------------------
# 4. ABSENSI HARIAN (VIA HTTP POST GOOGLE APPS SCRIPT)
# ---------------------------------------------------------
elif menu == "📝 Absensi Harian":
    st.markdown("<div class='main-title'>📝 Form Absensi Kehadiran Petugas</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Silakan Isi Formulir Kehadiran pada Setiap Hari Pelaksanaan MOOC</div>", unsafe_allow_html=True)
    st.divider()

    tab_peserta, tab_panitia = st.tabs(["✍️ Form Absensi Petugas", "📊 Rekap Absensi (Khusus Panitia)"])

    daftar_kab_kota = [
        "Kabupaten Bogor", "Kabupaten Sukabumi", "Kabupaten Cianjur", "Kabupaten Bandung",
        "Kabupaten Garut", "Kabupaten Tasikmalaya", "Kabupaten Ciamis", "Kabupaten Kuningan",
        "Kabupaten Cirebon", "Kabupaten Majalengka", "Kabupaten Sumedang", "Kabupaten Indramayu",
        "Kabupaten Subang", "Kabupaten Purwakarta", "Kabupaten Karawang", "Kabupaten Bekasi",
        "Kabupaten Bandung Barat", "Kabupaten Pangandaran", "Kota Bogor", "Kota Sukabumi",
        "Kota Bandung", "Kota Cirebon", "Kota Bekasi", "Kota Depok", "Kota Cimahi",
        "Kota Tasikmalaya", "Kota Banjar"
    ]

    with tab_peserta:
        st.subheader("Formulir Presensi Harian")
        with st.form(key="form_absensi", clear_on_submit=True):
            nama = st.text_input("Nama Lengkap Petugas *")
            id_petugas = st.text_input("ID Petugas / NIP *")
            kab_kota = st.selectbox("Kabupaten/Kota Tugas *", daftar_kab_kota)
            hari_absensi = st.selectbox("Absensi Untuk Hari Ke- *", ["Hari 1", "Hari 2"])
            catatan = st.text_area("Catatan / Kendala Harian (Opsional)")
            
            submit_absensi = st.form_submit_button("Kirim Absensi Kehadiran")

        if submit_absensi:
            if nama and id_petugas:
                waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                payload = {
                    "waktu_absen": waktu_sekarang,
                    "nama": nama,
                    "id_petugas": id_petugas,
                    "kab_kota": kab_kota,
                    "hari_absensi": hari_absensi,
                    "catatan": catatan if catatan else "-"
                }
                
                try:
                    res = requests.post(WEB_APP_URL, json=payload, timeout=5)
                    if res.status_code == 200:
                        st.success(f"✅ Terima kasih **{nama}**, absensi **{hari_absensi}** berhasil tersimpan langsung ke Google Sheets pada {waktu_sekarang}!")
                    else:
                        st.error("❌ Gagal mengirimkan absensi. Silakan coba lagi.")
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan: {e}")
            else:
                st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan absensi.")

    with tab_panitia:
        st.subheader("🔒 Akses Panitia & Rekap Kehadiran Real-Time")
        pin_panitia = st.text_input("Masukkan PIN Akses Panitia:", type="password", key="pin_absensi")
        
        if pin_panitia == "3200":
            st.success("🔓 Akses Panitia Diterima.")
            df_rekap = load_data_absensi()
            
            st.write(f"Total Kehadiran Tercatat: **{len(df_rekap)} Peserta**")
            st.dataframe(df_rekap, use_container_width=True, hide_index=True)
            
            csv_data = df_rekap.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Rekap Absensi (CSV / Excel)",
                data=csv_data,
                file_name=f"Rekap_Absensi_PES_SE2026_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        elif pin_panitia != "":
            st.error("❌ PIN Akses Salah! Gunakan PIN **3200**.")

# ---------------------------------------------------------
# 5. KUIS ASYNCHRONOUS (TERMASUK TAB REKAP NILAI KUIS)
# ---------------------------------------------------------
elif menu == "✏️ Kuis Asynchronous":
    st.markdown("<div class='main-title'>✏️ Kuis Evaluasi Asynchronous</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Uji Pemahaman Mandiri Hari 1 & Hari 2 PES SE2026 (20 Soal per Hari, 5 Poin/Soal)</div>", unsafe_allow_html=True)
    st.divider()

    tab_kuis_peserta, tab_kuis_panitia = st.tabs(["✍️ Pengerjaan Kuis", "📊 Rekap Nilai Kuis (Khusus Panitia)"])

    daftar_kab_kota = [
        "Kabupaten Bogor", "Kabupaten Sukabumi", "Kabupaten Cianjur", "Kabupaten Bandung",
        "Kabupaten Garut", "Kabupaten Tasikmalaya", "Kabupaten Ciamis", "Kabupaten Kuningan",
        "Kabupaten Cirebon", "Kabupaten Majalengka", "Kabupaten Sumedang", "Kabupaten Indramayu",
        "Kabupaten Subang", "Kabupaten Purwakarta", "Kabupaten Karawang", "Kabupaten Bekasi",
        "Kabupaten Bandung Barat", "Kabupaten Pangandaran", "Kota Bogor", "Kota Sukabumi",
        "Kota Bandung", "Kota Cirebon", "Kota Bekasi", "Kota Depok", "Kota Cimahi",
        "Kota Tasikmalaya", "Kota Banjar"
    ]

    with tab_kuis_peserta:
        pilihan_kuis = st.radio(
            "Pilih Kuis Evaluasi:",
            ["Kuis Hari 1: Konsep, Metodologi & Pencacahan Lapangan (20 Soal)", "Kuis Hari 2: Pengawasan, Kasus Batas & CAPI/Webmon (20 Soal)"],
            horizontal=True
        )

        # ---------------------------------------------------------
        # KUIS HARI 1 (20 SOAL, DEFAULT KOSONG)
        # ---------------------------------------------------------
        if pilihan_kuis == "Kuis Hari 1: Konsep, Metodologi & Pencacahan Lapangan (20 Soal)":
            st.subheader("📝 Kuis Evaluasi Hari 1 (Soal MOOC PES SE2026)")
            st.caption("Total: 20 Soal | Bobot: 5 Poin / Soal | Nilai Kelulusan Minimal: 70")
            
            with st.form("kuis_hari_1"):
                st.markdown("##### 👤 Data Peserta")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    nama_kuis = st.text_input("Nama Lengkap Petugas *")
                with col_b:
                    id_kuis = st.text_input("ID Petugas / NIP *")
                with col_c:
                    kab_kota_kuis = st.selectbox("Kabupaten/Kota Tugas *", daftar_kab_kota, key="kab_h1")
                
                st.divider()
                st.markdown("##### 📋 Soal Evaluasi Hari 1")

                q1_1 = st.radio('1. [Kode 1] Berikut adalah tujuan dari kegiatan PES SE2026, kecuali:',
                    ['a) Mendapatkan informasi untuk perencanaan sensus dan survei di masa mendatang', 'b) Melakukan perbaikan data SE2026 agar dihasilkan pendataan yang lebih akurat dan sesuai kondisi lapangan', 'c) Memberikan pandangan tentang kualitas dan keterbatasan data SE2026', 'd) Mengukur kesalahan cakupan (coverage error), kesalahan isian (content error), serta kesalahan responden (respons error) pencacahan SE2026'], index=None)

                q1_2 = st.radio('2. [Kode 1] Berikut pernyataan terkait PES SE2026 di bawah ini yang benar, kecuali:',
                    ['a) Petugas lapangan PES SE2026 terdiri dari Petugas Pendataan Lapangan, Petugas Pemeriksaan Lapangan, dan Petugas Rekonsiliasi Lapangan', 'b) Pada kegiatan PES SE2026 unit yang akan dicakup meliputi usaha/perusahaan berskala mikro, kecil, menengah, dan besar', 'c) Pada pelaksanaan PES SE2026, dilakukan pengambilan titik koordinat (Geotagging) lokasi bangunan', 'd) PES SE2026 dilaksanakan di 38 provinsi'], index=None)

                q1_3 = st.radio('3. [Kode 2] Berikut ini adalah pernyataan yang benar terkait desain sampel PES SE2026, kecuali',
                    ['a) Cakupan wilayah PES SE2026 adalah di 266 kabupaten/kota sehinggal level estimasinya adalah provinsi', 'b) Jumlah sampel SLS di kegiatan PES SE2026 non UB adalah 7.408 SLS', 'c) Cakupan wilayah PES SE2026 adalah di 266 kabupaten/kota sehinggal level estimasinya adalah kabupaten/kota', 'd) Jumlah sampel UB di kehiatan PES SE2026 adalah 7.703 UB'], index=None)

                q1_4 = st.radio('4. [Kode 2] Identifikasi unit usaha yang akan didata dalam PES SE2026 yaitu',
                    ['a) Pendekatan izin usaha, pendekatan lokasi usaha, dan pendekatan laporan/catatan keuangan', 'b) Pendekatan kepemilikan, pendekatan lokasi usaha, dan pendekatan laporan/catatan keuangan', 'c) Pendekatan kepemilikan, pendekatan jumlah pendapatan, dan pendekatan laporan/catatan keuangan', 'd) Pendekatan total aset, pendekatan lokasi usaha, dan pendekatan laporan/catatan keuangan'], index=None)

                q1_5 = st.radio('5. [Kode 3] Bagaimana bahasa yang sebaiknya digunakan Petugas saat berkomunikasi dengan responden?',
                    ['a) Bahasa teknis yang sulit dipahami', 'b) Bahasa yang selalu sama tanpa menyesuaikan responden', 'c) Bahasa singkatan agar wawancara cepat', 'd) Bahasa yang sederhana dan dimengerti oleh responden'], index=None)

                q1_6 = st.radio('6. [Kode 3] Kapan probing atau pertanyaan penelusuran dilakukan?',
                    ['a) Untuk mengarahkan responden pada jawaban tertentu', 'b) Setiap kali responden menjawab dengan benar', 'c) Ketika jawaban responden tidak jelas, tidak wajar, atau tidak sesuai pertanyaan', 'd) Hanya setelah wawancara selesai'], index=None)

                q1_7 = st.radio('7. [Kode 4.1] PPL door-to-door menemukan bangunan yang tidak ada di prelist dan terdapat usaha di dalamnya. Tindakan yang benar adalah',
                    ['a) Menambahkan assignment baru dan melanjutkan pendataan sampai kuesioner PES.SE2026-L', 'b) Menambahkan assignment baru dan melanjutkan pendataan hanya sampai kuesioner PES.SE2026-P', 'c) Mengabaikan bangunan tersebut karena bangunan tidak dicatat dalam PES SE2026', 'd) Langsung melaporkan ke PML'], index=None)

                q1_8 = st.radio('8. [Kode 4.1] pada saat door to door, PPL menemukan bangunan dalam kondisi rusak berat/terbengkalai/tidak lagi digunakan untuk tempat tinggal maupun tempat usaha. Bangunan tersebut belum ada di prelist. Apa yang harus dilakukan oleh PPL?',
                    ['a) Memutakhirkan Bangunan tersebut dengan PES.SE2026-P', 'b) Melaporkan ke PML untuk melakukan pengusulan penghapusan assignment FASIH', 'c) Menambahkan bangunan tersebut sebagai "Bangunan Lainnya" lalu mengisi kode penggunaan bangunan sebagai "Kode 6. Bangunan Lainnya yang tidak tercakup"', 'd) Tidak perlu menambahkan assignment baru. '], index=None)

                q1_9 = st.radio('9. [Kode 4.1] Apabila PPL menemukan bangunan tempat tinggal pada wilayah tugas SLS/non-SLS/sub-SLS nya apa yang pertama kalii dilakukan?',
                    ['a) Melakukan pengecekan pada daftar prelist berdasarkan nama kepala keluarga, jika sudah ada dilakukan pemutakhiran, jika belum ada dilakukan penambahan keluarga baru', 'b) Melakukan penambahan assignment bangunan khusus usaha', 'c) Melakukan penambahan assignment bangunan tempat tinggal', 'd) Melewati bangunan tempat tinggal tersebut dan melanjutkan ke bangunan tempat tinggal berikutnya'], index=None)

                q1_10 = st.radio('10. [Kode 4.1] Pada saat melakukan pemutakhiran instrumen apa yang perlu digunakan untuk mengetahui satuan wilayah terkecil yang menjadi tugas PPL?',
                    ['a) Peta WB', 'b) Peta WA', 'c) Peta WS/WSS', 'd) PES.SE2026-P'], index=None)

                q1_11 = st.radio('11. [Kode 4.1] Apabila pada saat melakukan pemutakhiran PPL menemukan bangunan pemerintah apa yang harus dilakukan?',
                    ['a) Melewatkan bangunan tersebut karena bukan cakupan pendataan PES SE2026', 'b) Melakukan pengecekan pada prelist apabila bangunan tersebut sudah ada, dan memastikan apakah terdapat usaha/bangunan usaha di dalamnya.', 'c) Menambahkan bangunan tersebut pada daftar pemutakhiran', 'd) Menambahkan bangunan tersebut pada daftar pemutakhiran dengan kode 5, kemudian langsung melanjutkan ke bangunan berikutnya.'], index=None)

                q1_12 = st.radio('12. [Kode 4.2] PPL menemukan sebuah bangunan ruko yang ternyata digunakan sepenuhnya sebagai tempat tinggal keluarga tanpa ada kegiatan usaha. Bagaimana kode penggunaan bangunan yang harus diisikan?',
                    ['a) Kode 3. Bangunan Tempat Tinggal', 'b) Kode 9. Non Respon', 'c) Kode 2. Bangunan Campuran', 'd) Kode 1. Bangunan Khusus Usaha'], index=None)

                q1_13 = st.radio('13. [Kode 4.2] Saat memutakhirkan keluarga pada PES.SE2026-P, indikator utama yang menentukan bahwa keluarga tersebut lanjut ke pendataan usaha (PES.SE2026-L Blok II) adalah:',
                    ['a) Seluruh anggota keluarga bekerja/sebagai buruh', 'b) Salah satu anggota keluarga mengelola usaha pertanian maupun non pertanian', 'c) Kepala keluarga berstatus buruh tetap BUMN', 'd) Keluarga memilki aset berupa lahan kosong'], index=None)

                q1_14 = st.radio('14. [Kode 5.1] Bagaimana pencatatan terkait jaringan usaha (Rincian 10.1) untuk pedagang keripik tempe di pasar yang mana keripik tempe tersebut di produksi di rumahnya.',
                    ['a) Cabang', 'b) Unit penunjang', 'c) Kantor Pusat', 'd) Tunggal'], index=None)

                q1_15 = st.radio('15. [Kode 5.1] Berikut merupakan penulisan nama usaha yang benar pada rincian 8.a, kecuali ',
                    ['a) SINAR JAYA, PO', 'b) PERSEWAAN KAMAR KOS\n(AGUNG)', 'c) CV MAJU JAYA', 'd) PRATAMA MAJU, TB'], index=None)

                q1_16 = st.radio('16. [Kode 5.3] Profesi pekerjaan utama ditanyakan untuk kepala/anggota rumah tangga yang berumur?',
                    ['a) berusia 10 tahun ke atas', 'b) Berusia 15 tahun ke atas', 'c) Berusia 17 tahun ke atas', 'd) Berusia 5 tahun ke atas'], index=None)

                q1_17 = st.radio('17. [Kode 5.3] Yang bukan contoh berusaha dibantu buruh tidak tetap/pekerja keluarga/tidak dibayar, yaitu',
                    ['a) Kepala keluarga/anggota keluarga sebagai pemilik toko yang mempekerjakan satu atau lebih buruh tetap dan dibayar.', 'b) Kepala keluarga/anggota keluarga sebagai petani yang mengusahakan lahan pertaniannya dengan dibantu pekerja tak dibayar. Walaupun pada waktu panen peserta tersebut memberikan hasil bagi panen (bawon), permanen tidak dianggap sebagai buruh tetap. ', 'c) Kepala keluarga/anggota keluarga sebagai pedagang keliling yang dibantu pekerja atau orang lain yang diberi upah pada saat membantu saja. ', 'd) Kepala keluarga/anggota keluarga sebagai pengusaha warung/toko yang dibantu anggota keluarga lain/pekerja tak dibayar dan/atau dibantu pegawai tidak tetap yang diberi upah berdasarkan hari masuk kerja. '], index=None)

                q1_18 = st.radio('18. [Kode 4.1] PPL door-to-door menemukan bangunan yang tidak ada di prelist dan terdapat usaha di dalamnya. Tindakan yang benar adalah',
                    ['a) Menambahkan assignment baru dan melanjutkan pendataan hanya sampai kuesioner PES.SE2026-P', 'b) Langsung melaporkan ke PML', 'c) Mengabaikan bangunan tersebut karena bangunan tidak dicatat dalam PES SE2026', 'd) Menambahkan assignment baru dan melanjutkan pendataan sampai kuesioner PES.SE2026-L'], index=None)

                q1_19 = st.radio('19. [Kode 4.5] Apa langkah pertama yang wajib dilakukan petugas lapangan sebelum memasuki wilayah blok sensus tugasnya?',
                    ['a) Mengirimkan hasil pendataan ke server pusat.', 'b) Mengisi kuesioner dengan data perkiraan.', 'c) Langsung menguji coba aplikasi pendataan.', 'd) Melapor dan berkoordinasi dengan ketua SLS / pengurus lokal setempat.'], index=None)

                q1_20 = st.radio('20. [Kode 4.6] Jika responden menolak untuk diwawancarai pada kunjungan pertama, apa tindakan yang paling tepat dilakukan oleh petugas?',
                    ['a) Langsung melaporkan responden ke pihak kepolisian.', 'b) Memaksa responden saat itu juga.', 'c) Bersikap sopan, mencatat alasan penolakan, dan menjadwalkan ulang kunjungan bersama PML.', 'd) Membiarkan data kosong dan mengganti dengan tetangga.'], index=None)

                submit_kuis1 = st.form_submit_button("📤 Kirim & Lihat Nilai Kuis Hari 1")

                if submit_kuis1:
                    if nama_kuis and id_kuis:
                        jawaban_benar = 0
                        if q1_1 and q1_1.startswith("b)"): jawaban_benar += 1
                        if q1_2 and q1_2.startswith("b)"): jawaban_benar += 1
                        if q1_3 and q1_3.startswith("c)"): jawaban_benar += 1
                        if q1_4 and q1_4.startswith("b)"): jawaban_benar += 1
                        if q1_5 and q1_5.startswith("d)"): jawaban_benar += 1
                        if q1_6 and q1_6.startswith("c)"): jawaban_benar += 1
                        if q1_7 and q1_7.startswith("a)"): jawaban_benar += 1
                        if q1_8 and q1_8.startswith("d)"): jawaban_benar += 1
                        if q1_9 and q1_9.startswith("a)"): jawaban_benar += 1
                        if q1_10 and q1_10.startswith("c)"): jawaban_benar += 1
                        if q1_11 and q1_11.startswith("b)"): jawaban_benar += 1
                        if q1_12 and q1_12.startswith("a)"): jawaban_benar += 1
                        if q1_13 and q1_13.startswith("b)"): jawaban_benar += 1
                        if q1_14 and q1_14.startswith("d)"): jawaban_benar += 1
                        if q1_15 and q1_15.startswith("c)"): jawaban_benar += 1
                        if q1_16 and q1_16.startswith("a)"): jawaban_benar += 1
                        if q1_17 and q1_17.startswith("a)"): jawaban_benar += 1
                        if q1_18 and q1_18.startswith("d)"): jawaban_benar += 1
                        if q1_19 and q1_19.startswith("d)"): jawaban_benar += 1
                        if q1_20 and q1_20.startswith("c)"): jawaban_benar += 1

                        skor = jawaban_benar * 5
                        status_lulus = "LULUS" if skor >= 70 else "TIDAK LULUS"
                        waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        payload_kuis = {
                            "type": "kuis",
                            "waktu_selesai": waktu_selesai,
                            "nama": nama_kuis,
                            "id_petugas": id_kuis,
                            "kab_kota": kab_kota_kuis,
                            "jenis_kuis": "Kuis Hari 1",
                            "skor": skor,
                            "status": status_lulus
                        }
                        try:
                            requests.post(WEB_APP_URL, json=payload_kuis, timeout=5)
                        except Exception:
                            pass

                        st.balloons()
                        st.success(f"🎉 Selamat **{nama_kuis}**, Kuis Hari 1 Selesai! Jawaban Benar: **{jawaban_benar} / 20 Soal**.")
                        st.metric(label="Nilai Akhir Kuis Hari 1", value=f"{skor} / 100")
                        if skor >= 70:
                            st.info(f"🏆 **Status:** LULUS Evaluasi Hari 1 (Skor: {skor})")
                        else:
                            st.warning(f"⚠️ **Status:** Belum Memenuhi Nilai Kelulusan Minimal 70 (Skor: {skor}). Pelajari kembali materi Hari 1.")
                    else:
                        st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan kuis.")

        # ---------------------------------------------------------
        # KUIS HARI 2 (20 SOAL, DEFAULT KOSONG)
        # ---------------------------------------------------------
        elif pilihan_kuis == "Kuis Hari 2: Pengawasan, Kasus Batas & CAPI/Webmon (20 Soal)":
            st.subheader("📝 Kuis Evaluasi Hari 2 (Soal MOOC PES SE2026 + Tambahan)")
            st.caption("Total: 20 Soal | Bobot: 5 Poin / Soal | Nilai Kelulusan Minimal: 70")

            with st.form("kuis_hari_2"):
                st.markdown("##### 👤 Data Peserta")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    nama_kuis = st.text_input("Nama Lengkap Petugas *")
                with col_b:
                    id_kuis = st.text_input("ID Petugas / NIP *")
                with col_c:
                    kab_kota_kuis = st.selectbox("Kabupaten/Kota Tugas *", daftar_kab_kota, key="kab_h2")

                st.divider()
                st.markdown("##### 📋 Soal Evaluasi Hari 2")

                q2_1 = st.radio('1. [Kode 6] Pada pelaksanaan lapangan PES SE2026 di bulan Oktober-November 2026, berikut yang bukan merupakan fungsi PML adalah:',
                    ['a) Fungsi koordinasi', 'b) Fungsi pemeriksaan hasil', 'c) Fungsi pengawasan', 'd) Fungsi rekonsiliasi lapangan'], index=None)

                q2_2 = st.radio('2. [Kode 6] Berikut yang merupakan tugas dan tanggung jawab PML, kecuali:',
                    ['a) Melakukan sosialisasi kegiatan PES SE2026 dengan perangkat desa/kelurahan dan ketua SLS', 'b) Membagi wilayah kerja dan menentukan alokasi PPL', 'c) Memeriksa isian e-form PES.SE2026-L dan melakukan approval atau reject', 'd) Mendistribusikan instrumen dan perlengkapan pendataan kepada PPL'], index=None)

                q2_3 = st.radio('3. [Kode 7] Pernyataan berikut yang tidak benar terkait tujuan rekosiliasi lapangan adalah:',
                    ['a) Mengklarifikasi di lapangan mana yang benar hasil pendataan SE2026 atau pendataan PES SE2026', 'b) Menentukan status pencacahan SE2026 untuk usaha/keluarga/individu yang tercatat di SE2026 tetapi tidak tercatat di PES SE2026', 'c) Mengklarifikasi kasus yang meragukan atau kasus dengan informasi tidak jelas atau tidak cukup lengkap dalam rangka menentukan status match akhir', 'd) Menentukan status pencacahan SE2026 untuk usaha yang tercatat di PES SE2026 tetapi tidak tercatat di SE2026'], index=None)

                q2_4 = st.radio('4. [Kode 7] Instrumen yang digunakan pada saat rekonsiliasi lapangan yaitu:',
                    ['a) E-form PES.SE2026-L dan peta WS/WSS', 'b) E-form PES.SE2026-RLU dan peta WA', 'c) E-form PES.SE2026-RLK dan peta WA', 'd) E-form PES.SE2026-RLAK dan peta WS/WSS'], index=None)

                q2_5 = st.radio('5. [Kode 8] Usaha membuat dan menjual roti kemasan di satu lokasi yang sama masuk ke KBLI kategori?',
                    ['a) I. Penyediaan Makanan dan Minuman', 'b) A. Pertanian, Kehutanan, dan Perikanan', 'c) C. Industri', 'd) G. Perdagangan Besar dan Eceran'], index=None)

                q2_6 = st.radio('6. [Kode 8] Sebuah rumah dihuni oleh 1 keluarga dengan 3 orang anggota keluarga (termasuk kepala keluarga). Mereka memperkerjakan seorang pembantu (ART) dan memberikannya kamar untuk ditinggali setiap hari. ART pulang setiap 1 bulan sekali di weekend. Berapa keluarga yang dicatat yang tinggal di rumah tersebut?',
                    ['a) 3', 'b) 2', 'c) 1', 'd) 0'], index=None)

                q2_7 = st.radio('7. [Kode 8] Apabila Anto ditemukan rajin investasi dari sisa uang bulanannya (jika ada) dengan membeli obligasi, usaha Anto masuk ke kategori apa?',
                    ['a) G. Perdagangan Besar dan Eceran', 'b) L. Aktivitas Keuangan dan Asuransi', 'c) Bukan usaha', 'd) O. Aktivitas Administratif dan Penunjang Usaha'], index=None)

                q2_8 = st.radio('8. [Kode 9] Kode hasil pemeriksaan pengawas terhadap data sampel dapat berupa:',
                    ['a) Submit atau complete', 'b) Edited atau revoked', 'c) Open atau submitted', 'd) Approve atau reject'], index=None)

                q2_9 = st.radio('9. [Kode 9] Dashboard PES SE2026 digunakan terutama untuk:',
                    ['a) Menginstal FASIH Mobile dan FASIH SM', 'b) Monitoring dan evaluasi', 'c) Menyusun kuesioner', 'd) Mendaftarkan akun SOBAT'], index=None)

                q2_10 = st.radio('10. [Soal 2.1] Dalam pengisian alur kuesioner, apa yang harus dipastikan petugas sebelum berpindah ke halaman/blok pertanyaan berikutnya?',
                    ['a) Menghapus rincian jawaban jika terlalu panjang', 'b) Membiarkan peringatan error pada aplikasi', 'c) Semua pertanyaan wajib telah terisi lengkap dan konsisten', 'd) Mengosongkan jawaban yang dirasa sulit'], index=None)

                q2_11 = st.radio('11. [Soal 2.2] Apa kriteria utama suatu kegiatan dapat dicatat sebagai usaha/perusahaan pada SE2026?',
                    ['a) Memiliki karyawan minimal 10 orang', 'b) Memiliki izin resmi dari pemerintah saja', 'c) Harus memiliki tempat fisik yang luas', 'd) Ada kegiatan ekonomi yang menghasilkan barang/jasa dengan tujuan komersial/dijual'], index=None)

                q2_12 = st.radio('12. [Soal 2.3] Jika suatu bangunan digunakan sekaligus sebagai tempat tinggal dan tempat usaha toko kelontong, bagaimana pencatatannya?',
                    ['a) Dicatat dua kali sebagai tempat usaha terpisah', 'b) Dicatat sebagai tempat tinggal dan dicatat keberadaan usahanya', 'c) Tidak perlu dicatat sama sekali', 'd) Dicatat hanya sebagai tempat tinggal'], index=None)

                q2_13 = st.radio('13. [Soal 2.4] Apa fungsi utama dari Peta Blok Sensus (Wilkerstat) yang dipegang oleh petugas lapangan?',
                    ['a) Untuk diserahkan kepada responden', 'b) Sebagai syarat pencairan honor', 'c) Hanya sebagai pelengkap berkas', 'd) Sebagai penanda batas wilayah tugas agar tidak terjadi penumpukan/lewat batas pendataan'], index=None)

                q2_14 = st.radio('14. [Soal 2.5] Apabila ditemukan usaha online (e-commerce) yang dijalankan dari rumah tanpa papan nama usaha, apakah tetap didata?',
                    ['a) Ya, tetap didata sesuai keberadaan domisili/operasional usahanya', 'b) Hanya didata jika memiliki izin usaha formal', 'c) Tidak, karena tidak ada bangunan fisiknya', 'd) Ditunda sampai memiliki toko fisik'], index=None)

                q2_15 = st.radio('15. [Soal 2.6] Periode rujukan data pendapatan/omzet yang ditanyakan kepada responden umumnya mengacu pada periode...',
                    ['a) Bebas tergantung kemauan responden', 'b) 10 tahun terakhir', 'c) Periode rujukan waktu yang ditentukan dalam juknis (misal: setahun terakhir/sebulan terakhir)', 'd) Perkiraan 5 tahun ke depan'], index=None)

                q2_16 = st.radio('16. [Soal 2.7] Apa yang harus dilakukan petugas jika koordinat GPS yang ditangkap aplikasi belum akurat/presisi?',
                    ['a) Berada di area terbuka di titik lokasi usaha dan menunggu hingga indikator GPS akurat', 'b) Mematikan HP dan pulang', 'c) Mengisi titik koordinat secara manual dari tempat lain', 'd) Mengosongkan data koordinat'], index=None)

                q2_17 = st.radio('17. [Soal 2.8] Pembina/Pemeriksa lapangan yang bertugas mendampingi dan mengawasi PPL di lapangan disebut...',
                    ['a) Responden', 'b) PML (Pemeriksa Lapangan)', 'c) Koseka', 'd) BPS Pusat'], index=None)

                q2_18 = st.radio('18. [Soal 2.9] Mengapa persetujuan dan partisipasi responden sangat penting dalam pendataan SE2026?',
                    ['a) Agar petugas bisa cepat selesai', 'b) Hanya untuk formalitas laporan', 'c) Untuk menjamin keakuratan dan kualitas data statistik nasional', 'd) Untuk pembagian hadiah dari petugas'], index=None)

                q2_19 = st.radio('19. [Soal 2.10] Jika terdapat perbedaan data antara keterangan ketua RT dengan kondisi riil di lapangan, informasi mana yang digunakan?',
                    ['a) Hasil verifikasi dan konfirmasi langsung di lapangan', 'b) Menggunakan data tahun lalu', 'c) Dibiarkan kosong', 'd) Keterangan ketua RT tanpa verifikasi'], index=None)

                q2_20 = st.radio('20. [Soal 2.11] Sebelum melakukan finalisasi/submit data dokumen pada aplikasi pendataan, tindakan apa yang wajib dilakukan PPL?',
                    ['a) Memeriksa kembali seluruh rincian jawaban agar tidak ada yang terlewat (validasi mandiri)', 'b) Menghapus cache aplikasi tanpa kirim data', 'c) Langsung mematikan aplikasi', 'd) Mengubah jawaban responden sesuai keinginan sendiri'], index=None)

                submit_kuis2 = st.form_submit_button("📤 Kirim & Lihat Nilai Kuis Hari 2")

                if submit_kuis2:
                    if nama_kuis and id_kuis:
                        jawaban_benar = 0
                        if q2_1 and q2_1.startswith("d)"): jawaban_benar += 1
                        if q2_2 and q2_2.startswith("b)"): jawaban_benar += 1
                        if q2_3 and q2_3.startswith("a)"): jawaban_benar += 1
                        if q2_4 and q2_4.startswith("d)"): jawaban_benar += 1
                        if q2_5 and q2_5.startswith("c)"): jawaban_benar += 1
                        if q2_6 and q2_6.startswith("b)"): jawaban_benar += 1
                        if q2_7 and q2_7.startswith("c)"): jawaban_benar += 1
                        if q2_8 and q2_8.startswith("d)"): jawaban_benar += 1
                        if q2_9 and q2_9.startswith("b)"): jawaban_benar += 1
                        if q2_10 and q2_10.startswith("c)"): jawaban_benar += 1
                        if q2_11 and q2_11.startswith("d)"): jawaban_benar += 1
                        if q2_12 and q2_12.startswith("b)"): jawaban_benar += 1
                        if q2_13 and q2_13.startswith("d)"): jawaban_benar += 1
                        if q2_14 and q2_14.startswith("a)"): jawaban_benar += 1
                        if q2_15 and q2_15.startswith("c)"): jawaban_benar += 1
                        if q2_16 and q2_16.startswith("a)"): jawaban_benar += 1
                        if q2_17 and q2_17.startswith("b)"): jawaban_benar += 1
                        if q2_18 and q2_18.startswith("c)"): jawaban_benar += 1
                        if q2_19 and q2_19.startswith("a)"): jawaban_benar += 1
                        if q2_20 and q2_20.startswith("a)"): jawaban_benar += 1

                        skor = jawaban_benar * 5
                        status_lulus = "LULUS" if skor >= 70 else "TIDAK LULUS"
                        waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        payload_kuis = {
                            "type": "kuis",
                            "waktu_selesai": waktu_selesai,
                            "nama": nama_kuis,
                            "id_petugas": id_kuis,
                            "kab_kota": kab_kota_kuis,
                            "jenis_kuis": "Kuis Hari 2",
                            "skor": skor,
                            "status": status_lulus
                        }
                        try:
                            requests.post(WEB_APP_URL, json=payload_kuis, timeout=5)
                        except Exception:
                            pass

                        st.balloons()
                        st.success(f"🎉 Selamat **{nama_kuis}**, Kuis Hari 2 Selesai! Jawaban Benar: **{jawaban_benar} / 20 Soal**.")
                        st.metric(label="Nilai Akhir Kuis Hari 2", value=f"{skor} / 100")
                        if skor >= 70:
                            st.info(f"🏆 **Status:** LULUS Evaluasi Hari 2 (Skor: {skor})")
                        else:
                            st.warning(f"⚠️ **Status:** Belum Memenuhi Nilai Kelulusan Minimal 70 (Skor: {skor}). Pelajari kembali materi Hari 2.")
                    else:
                        st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan kuis.")

    # ---------------------------------------------------------
    # TAB REKAP NILAI KUIS (KHUSUS PANITIA)
    # ---------------------------------------------------------
    with tab_kuis_panitia:
        st.subheader("🔒 Akses Panitia & Rekap Nilai Kuis Real-Time")
        pin_panitia_kuis = st.text_input("Masukkan PIN Akses Panitia:", type="password", key="pin_kuis")
        
        if pin_panitia_kuis == "3200":
            st.success("🔓 Akses Panitia Diterima.")
            df_rekap_kuis = load_data_kuis()
            
            st.write(f"Total Pengerjaan Kuis Tercatat: **{len(df_rekap_kuis)} Peserta**")
            st.dataframe(df_rekap_kuis, use_container_width=True, hide_index=True)
            
            csv_data_kuis = df_rekap_kuis.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Rekap Nilai Kuis (CSV / Excel)",
                data=csv_data_kuis,
                file_name=f"Rekap_Nilai_Kuis_PES_SE2026_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        elif pin_panitia_kuis != "":
            st.error("❌ PIN Akses Salah! Gunakan PIN **3200**.")

# Footer Teks Sederhana
st.divider()
st.caption("© 2026 BPS Provinsi Jawa Barat — Post Enumeration Survey Sensus Ekonomi 2026")
