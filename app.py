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
# Paste URL Web App dari Apps Script di bawah ini:
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwNeU_2Hi2pfbzedgoN-kRnsyqlKP8nwbIwLSqkpsRUf4Hr5s5Rw2cV-8iyhe1JdbvN/exec"  # <--- GANTI LINK INI

# Link CSV untuk membaca data publik spreadsheet secara langsung:
SPREADSHEET_ID = "1JOudkfgyJrlc2iTlsKofHNja3Xkn2NgLV4D1k-_9jd4"
CSV_READ_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv"

def load_data_absensi():
    try:
        df = pd.read_csv(CSV_READ_URL)
        return df.dropna(how="all")
    except Exception as e:
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
                    res = requests.post(WEB_APP_URL, json=payload)
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
        pin_panitia = st.text_input("Masukkan PIN Akses Panitia:", type="password")
        
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
# 5. KUIS ASYNCHRONOUS (TERSTRUKTUR & OTOMATIS TERSIMPAN KE GOOGLE SHEETS)
# ---------------------------------------------------------
elif menu == "✏️ Kuis Asynchronous":
    st.markdown("<div class='main-title'>✏️ Kuis Evaluasi Asynchronous</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Uji Pemahaman Mandiri Hari 1 & Hari 2 PES SE2026</div>", unsafe_allow_html=True)
    st.divider()

    daftar_kab_kota = [
        "Kabupaten Bogor", "Kabupaten Sukabumi", "Kabupaten Cianjur", "Kabupaten Bandung",
        "Kabupaten Garut", "Kabupaten Tasikmalaya", "Kabupaten Ciamis", "Kabupaten Kuningan",
        "Kabupaten Cirebon", "Kabupaten Majalengka", "Kabupaten Sumedang", "Kabupaten Indramayu",
        "Kabupaten Subang", "Kabupaten Purwakarta", "Kabupaten Karawang", "Kabupaten Bekasi",
        "Kabupaten Bandung Barat", "Kabupaten Pangandaran", "Kota Bogor", "Kota Sukabumi",
        "Kota Bandung", "Kota Cirebon", "Kota Bekasi", "Kota Depok", "Kota Cimahi",
        "Kota Tasikmalaya", "Kota Banjar"
    ]

    pilihan_kuis = st.radio(
        "Pilih Kuis Evaluasi:",
        ["Kuis Hari 1: Konsep, Metodologi & Pencacahan Lapangan", "Kuis Hari 2: Pengawasan, Kasus Batas & CAPI/Webmon"],
        horizontal=True
    )

    # ---------------------------------------------------------
    # KUIS HARI 1
    # ---------------------------------------------------------
    if pilihan_kuis == "Kuis Hari 1: Konsep, Metodologi & Pencacahan Lapangan":
        st.subheader("📝 Kuis Evaluasi Hari 1")
        st.caption("Cakupan: Kode 1 (Organisasi), Kode 2 (Metodologi), Kode 3 (Wawancara), Kode 4 (Pemutakhiran P), Kode 5 (Pencacahan L)")
        
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

            q1_1 = st.radio(
                "1. [Kode 101] Apa tujuan utama dari pelaksanaan Post Enumeration Survey (PES) SE2026?",
                [
                    "a) Mengukur cakupan (coverage) dan akurasi kualitas data Sensus Ekonomi 2026",
                    "b) Mengganti seluruh data Sensus Ekonomi 2026",
                    "c) Menghitung jumlah penduduk di wilayah perkotaan saja",
                    "d) Melakukan pemungutan pajak bagi usaha mikro"
                ]
            )

            q1_2 = st.radio(
                "2. [Kode 102] Siapa saja yang menjadi target responden dalam pelaksanaan pendataan lapangan PES SE2026?",
                [
                    "a) Pelaku usaha/perusahaan non-pertanian di bangunan fisik maupun non-bangunan",
                    "b) Hanya perusahaan berbadan hukum PT/CV",
                    "c) Hanya pedagang di pasar tradisional",
                    "d) Seluruh rumah tangga tanpa kegiatan usaha"
                ]
            )

            q1_3 = st.radio(
                "3. [Soal 1.1] Apa langkah pertama yang wajib dilakukan petugas lapangan sebelum memasuki wilayah blok sensus tugasnya?",
                [
                    "a) Langsung menguji coba aplikasi pendataan.",
                    "b) Melapor dan berkoordinasi dengan ketua SLS / pengurus lokal setempat.",
                    "c) Mengisi kuesioner dengan data perkiraan.",
                    "d) Mengirimkan hasil pendataan ke server pusat."
                ]
            )

            q1_4 = st.radio(
                "4. [Soal 1.2] Jika responden menolak untuk diwawancarai pada kunjungan pertama, apa tindakan yang paling tepat dilakukan oleh petugas?",
                [
                    "a) Memaksa responden saat itu juga.",
                    "b) Membiarkan data kosong dan mengganti dengan tetangga.",
                    "c) Bersikap sopan, mencatat alasan penolakan, dan menjadwalkan ulang kunjungan bersama PML.",
                    "d) Langsung melaporkan responden ke pihak kepolisian."
                ]
            )

            submit_kuis1 = st.form_submit_button("📤 Kirim Jawaban Kuis Hari 1")

            if submit_kuis1:
                if nama_kuis and id_kuis:
                    skor = 0
                    if q1_1.startswith("a)"): skor += 25
                    if q1_2.startswith("a)"): skor += 25
                    if q1_3.startswith("b)"): skor += 25
                    if q1_4.startswith("c)"): skor += 25

                    status_lulus = "LULUS" if skor >= 70 else "TIDAK LULUS"
                    waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Kirim data ke Google Sheets
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
                        requests.post(WEB_APP_URL, json=payload_kuis)
                    except Exception as e:
                        pass

                    st.balloons()
                    st.success(f"🎉 Selamat **{nama_kuis}**, kuis Hari 1 telah terkirim dan tersimpan ke Google Sheets!")
                    st.metric(label="Nilai Akhir Kuis Hari 1", value=f"{skor} / 100")
                    if skor >= 70:
                        st.info("🏆 **Status:** LULUS Evaluasi Hari 1")
                    else:
                        st.warning("⚠️ **Status:** Belum Memenuhi Nilai Kelulusan Minimal (70). Pelajari kembali materi Hari 1.")
                else:
                    st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan kuis.")

    # ---------------------------------------------------------
    # KUIS HARI 2
    # ---------------------------------------------------------
    elif pilihan_kuis == "Kuis Hari 2: Pengawasan, Kasus Batas & CAPI/Webmon":
        st.subheader("📝 Kuis Evaluasi Hari 2")
        st.caption("Cakupan: Kode 6 (Pemeriksaan), Kode 7 (Rekonsiliasi), Kode 8 (Kasus Batas), Kode 9 (CAPI FASIH & Webmon)")

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

            q2_ex1 = st.radio(
                "1. [Kode 201] Bagaimanakah cara mencatat usaha yang memiliki lebih dari satu lokasi kegiatan (cabang)?",
                ["a) Dicatat sesuai unit usaha di masing-masing lokasi operasionalnya", "b) Hanya dicatat di kantor pusat saja", "c) Digabungkan menjadi satu tanpa rincian lokasi", "d) Tidak perlu didata jika usahanya kecil"]
            )
            q2_ex2 = st.radio(
                "2. [Kode 202] Pembina/Pemeriksa lapangan yang bertugas mendampingi, memverifikasi, dan mengawasi PPL di lapangan disebut...",
                ["a) Koseka", "b) PML (Pemeriksa Lapangan)", "c) BPS Pusat", "d) Admin Webmon"]
            )
            q2_1 = st.radio(
                "3. [Soal 2.1] Dalam pengisian alur kuesioner, apa yang harus dipastikan petugas sebelum berpindah ke halaman/blok pertanyaan berikutnya?",
                ["a) Semua pertanyaan wajib telah terisi lengkap dan konsisten", "b) Mengosongkan jawaban yang dirasa sulit", "c) Menghapus rincian jawaban jika terlalu panjang", "d) Membiarkan peringatan error pada aplikasi"]
            )
            q2_2 = st.radio(
                "4. [Soal 2.2] Apa kriteria utama suatu kegiatan dapat dicatat sebagai usaha/perusahaan pada SE2026?",
                ["a) Memiliki izin resmi dari pemerintah saja", "b) Ada kegiatan ekonomi yang menghasilkan barang/jasa dengan tujuan komersial/dijual", "c) Harus memiliki tempat fisik yang luas", "d) Memiliki karyawan minimal 10 orang"]
            )
            q2_3 = st.radio(
                "5. [Soal 2.3] Jika suatu bangunan digunakan sekaligus sebagai tempat tinggal dan tempat usaha toko kelontong, bagaimana pencatatannya?",
                ["a) Dicatat hanya sebagai tempat tinggal", "b) Dicatat sebagai tempat tinggal dan dicatat keberadaan usahanya", "c) Tidak perlu dicatat sama sekali", "d) Dicatat dua kali sebagai tempat usaha terpisah"]
            )
            q2_4 = st.radio(
                "6. [Soal 2.4] Apa fungsi utama dari Peta Blok Sensus (Wilkerstat) yang dipegang oleh petugas lapangan?",
                ["a) Sebagai penanda batas wilayah tugas agar tidak terjadi penumpukan/lewat batas pendataan", "b) Sebagai syarat pencairan honor", "c) Untuk diserahkan kepada responden", "d) Hanya sebagai pelengkap berkas"]
            )
            q2_5 = st.radio(
                "7. [Soal 2.5] Apabila ditemukan usaha online (e-commerce) yang dijalankan dari rumah tanpa papan nama usaha, apakah tetap didata?",
                ["a) Ya, tetap didata sesuai keberadaan domisili/operasional usahanya", "b) Tidak, karena tidak ada bangunan fisiknya", "c) Hanya didata jika memiliki izin usaha formal", "d) Ditunda sampai memiliki toko fisik"]
            )
            q2_6 = st.radio(
                "8. [Soal 2.6] Periode rujukan data pendapatan/omzet yang ditanyakan kepada responden umumnya mengacu pada periode...",
                ["a) 10 tahun terakhir", "b) Periode rujukan waktu yang ditentukan dalam juknis (misal: setahun terakhir/sebulan terakhir)", "c) Perkiraan 5 tahun ke depan", "d) Bebas tergantung kemauan responden"]
            )
            q2_7 = st.radio(
                "9. [Soal 2.7] Apa yang harus dilakukan petugas jika koordinat GPS yang ditangkap aplikasi belum akurat/presisi?",
                ["a) Mematikan HP dan pulang", "b) Berada di area terbuka di titik lokasi usaha dan menunggu hingga indikator GPS akurat", "c) Mengisi titik koordinat secara manual dari tempat lain", "d) Mengosongkan data koordinat"]
            )
            q2_8 = st.radio(
                "10. [Soal 2.8] Mengapa persetujuan dan partisipasi responden sangat penting dalam pendataan SE2026?",
                ["a) Agar petugas bisa cepat selesai", "b) Untuk menjamin keakuratan dan kualitas data statistik nasional", "c) Untuk pembagian hadiah dari petugas", "d) Hanya untuk formalitas laporan"]
            )
            q2_9 = st.radio(
                "11. [Soal 2.9] Jika terdapat perbedaan data antara keterangan ketua RT dengan kondisi riil di lapangan, informasi mana yang digunakan?",
                ["a) Keterangan ketua RT tanpa verifikasi", "b) Hasil verifikasi dan konfirmasi langsung di lapangan", "c) Menggunakan data tahun lalu", "d) Dibiarkan kosong"]
            )
            q2_10 = st.radio(
                "12. [Soal 2.10] Sebelum melakukan finalisasi/submit data dokumen pada aplikasi pendataan, tindakan apa yang wajib dilakukan PPL?",
                ["a) Memeriksa kembali seluruh rincian jawaban agar tidak ada yang terlewat (validasi mandiri)", "b) Langsung mematikan aplikasi", "c) Mengubah jawaban responden sesuai keinginan sendiri", "d) Menghapus cache aplikasi tanpa kirim data"]
            )

            submit_kuis2 = st.form_submit_button("📤 Kirim Jawaban Kuis Hari 2")

            if submit_kuis2:
                if nama_kuis and id_kuis:
                    skor = 0
                    total_soal = 12
                    bobot = 100 / total_soal

                    if q2_ex1.startswith("a)"): skor += bobot
                    if q2_ex2.startswith("b)"): skor += bobot
                    if q2_1.startswith("a)"): skor += bobot
                    if q2_2.startswith("b)"): skor += bobot
                    if q2_3.startswith("b)"): skor += bobot
                    if q2_4.startswith("a)"): skor += bobot
                    if q2_5.startswith("a)"): skor += bobot
                    if q2_6.startswith("b)"): skor += bobot
                    if q2_7.startswith("b)"): skor += bobot
                    if q2_8.startswith("b)"): skor += bobot
                    if q2_9.startswith("b)"): skor += bobot
                    if q2_10.startswith("a)"): skor += bobot

                    skor_akhir = round(skor)
                    status_lulus = "LULUS" if skor_akhir >= 70 else "TIDAK LULUS"
                    waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Kirim data ke Google Sheets
                    payload_kuis = {
                        "type": "kuis",
                        "waktu_selesai": waktu_selesai,
                        "nama": nama_kuis,
                        "id_petugas": id_kuis,
                        "kab_kota": kab_kota_kuis,
                        "jenis_kuis": "Kuis Hari 2",
                        "skor": skor_akhir,
                        "status": status_lulus
                    }
                    try:
                        requests.post(WEB_APP_URL, json=payload_kuis)
                    except Exception as e:
                        pass

                    st.balloons()
                    st.success(f"🎉 Selamat **{nama_kuis}**, kuis Hari 2 telah terkirim dan tersimpan ke Google Sheets!")
                    st.metric(label="Nilai Akhir Kuis Hari 2", value=f"{skor_akhir} / 100")
                    if skor_akhir >= 70:
                        st.info("🏆 **Status:** LULUS Evaluasi Hari 2")
                    else:
                        st.warning("⚠️ **Status:** Belum Memenuhi Nilai Kelulusan Minimal (70). Pelajari kembali materi Hari 2.")
                else:
                    st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan kuis.")

# Footer Teks Sederhana
st.divider()
st.caption("© 2026 BPS Provinsi Jawa Barat — Post Enumeration Survey Sensus Ekonomi 2026")
