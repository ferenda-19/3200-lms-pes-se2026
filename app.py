import streamlit as st
import pandas as pd
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

# Custom Styling CSS (Kontras Tinggi & Responsif)
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
        3. **Mengerjakan Kuis Asynchronous:** Selesaikan kuis evaluasi Harian 1 & Harian 2 untuk mengukur pemahaman Anda.
        """)
        
        st.info("🔔 **Pengumuman:** Pastikan koneksi internet stabil saat mengunduh materi dan mengerjakan kuis Asynchronous.")

    with col2:
        st.markdown("### 📊 Ringkasan Pelatihan")
        st.metric(label="Durasi Pelatihan", value="2 Hari (Asynchronous)")
        st.metric(label="Pelaksanaan", value="23 - 24 Sept 2026")
        st.metric(label="Status Pendaftaran", value="Aktif", delta="Terverifikasi")

# ---------------------------------------------------------
# 2. JADWAL MOOC (2 HARI - TABEL DINAMIS)
# ---------------------------------------------------------
elif menu == "📅 Jadwal MOOC (2 Hari)":
    st.title("📅 Jadwal Pelatihan MOOC PES SE2026")
    st.caption("Jadwal Pelaksanaan Mandiri (Asynchronous) | 23 - 24 September 2026")
    st.write("Silakan cermati struktur jadwal pembelajaran mandiri berikut:")

    tab1, tab2 = st.tabs(["📌 Hari 1 (23 September 2026)", "📌 Hari 2 (24 September 2026)"])

    # Data Jadwal Hari 1
    jadwal_hari1 = [
        {"Waktu (WIB)": "08.00 - 08.30", "Sesi": "Sesi 1", "Materi / Kegiatan": "Penjelasan Umum & Organisasi Lapangan PES SE2026", "Durasi": "30 Menit"},
        {"Waktu (WIB)": "08.30 - 09.15", "Sesi": "Sesi 2", "Materi / Kegiatan": "Metodologi & Mekanisme Pencacahan Lapangan", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "09.15 - 10.45", "Sesi": "Sesi 3", "Materi / Kegiatan": "Pemutakhiran E-Form PES.SE2026.P", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "10.45 - 11.00", "Sesi": "Istirahat", "Materi / Kegiatan": "Istirahat / Coffee Break", "Durasi": "15 Menit"},
        {"Waktu (WIB)": "11.00 - 11.45", "Sesi": "Sesi 4", "Materi / Kegiatan": "Tata Cara Bertanya & Teknik Wawancara Responden", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "11.45 - 13.00", "Sesi": "ISHOMA", "Materi / Kegiatan": "Istirahat, Sholat, & Pengisian Absensi Hari 1", "Durasi": "75 Menit"},
        {"Waktu (WIB)": "13.00 - 15.00", "Sesi": "Sesi 5", "Materi / Kegiatan": "Pencacahan E-Form PES.SE2026.L dan L.UB", "Durasi": "120 Menit"},
        {"Waktu (WIB)": "15.00 - 16.30", "Sesi": "Sesi 6", "Materi / Kegiatan": "Pengerjaan Tugas Asynchronous 1 & Kuis Hari 1", "Durasi": "90 Menit"}
    ]

    # Data Jadwal Hari 2
    jadwal_hari2 = [
        {"Waktu (WIB)": "08.00 - 09.30", "Sesi": "Sesi 1", "Materi / Kegiatan": "Pengawasan, Pemeriksaan, & Penjaminan Kualitas Data", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "09.30 - 11.00", "Sesi": "Sesi 2", "Materi / Kegiatan": "Penanganan Kasus Batas (Boundary Cases) Lapangan", "Durasi": "90 Menit"},
        {"Waktu (WIB)": "11.00 - 11.15", "Sesi": "Istirahat", "Materi / Kegiatan": "Istirahat / Coffee Break", "Durasi": "15 Menit"},
        {"Waktu (WIB)": "11.15 - 12.15", "Sesi": "Sesi 3", "Materi / Kegiatan": "Instalasi, Penggunaan CAPI, & Webmonitoring (Webmon)", "Durasi": "60 Menit"},
        {"Waktu (WIB)": "12.15 - 13.30", "Sesi": "ISHOMA", "Materi / Kegiatan": "Istirahat, Sholat, & Pengisian Absensi Hari 2", "Durasi": "75 Menit"},
        {"Waktu (WIB)": "13.30 - 14.30", "Sesi": "Sesi 4", "Materi / Kegiatan": "Rekonsiliasi Lapangan (E-Form RL)", "Durasi": "60 Menit"},
        {"Waktu (WIB)": "14.30 - 15.15", "Sesi": "Sesi 5", "Materi / Kegiatan": "Pendalaman & Penegasan Materi PES SE2026", "Durasi": "45 Menit"},
        {"Waktu (WIB)": "15.15 - 16.30", "Sesi": "Sesi 6", "Materi / Kegiatan": "Pengerjaan Tugas Asynchronous 2 & Post Test", "Durasi": "75 Menit"}
    ]

    with tab1:
        st.subheader("📋 Tabel Jadwal — Hari 1 (Rabu, 23 September 2026)")
        df_h1 = pd.DataFrame(jadwal_hari1)
        st.dataframe(df_h1, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("📋 Tabel Jadwal — Hari 2 (Kamis, 24 September 2026)")
        df_h2 = pd.DataFrame(jadwal_hari2)
        st.dataframe(df_h2, use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# 3. BAHAN & MATERI
# ---------------------------------------------------------
elif menu == "📂 Bahan & Materi":
    st.title("📂 Bahan & Materi Pelatihan")
    st.write("Unduh bahan pustaka dan materi paparan resmi di bawah ini:")

    col_mat1, col_mat2 = st.columns(2)

    with col_mat1:
        st.subheader("📖 Buku Pedoman")
        st.markdown("""
        * **Pedoman Umum Petugas PES SE2026**
          * *Deskripsi:* Panduan lengkap tata tertib, tugas, dan tanggung jawab petugas.
          * [📄 Unduh Pedoman Umum (PDF)](https://example.com/pedoman-umum.pdf)
        * **Pedoman Konsep & Definisi Lapangan**
          * *Deskripsi:* Penjelasan variabel kuesioner dan batasan sektor usaha.
          * [📄 Unduh Pedoman Kondef (PDF)](https://example.com/pedoman-kondef.pdf)
        """)

    with col_mat2:
        st.subheader("🖥️ Slide Paparan Materi")
        st.markdown("""
        * **Materi Hari 1: Metodologi & Konsep Usaha**
          * [📊 Unduh Slide Hari 1 (PPTX/PDF)](https://example.com/materi-hari-1.pdf)
        * **Materi Hari 2: Identifikasi & Tata Cara Wawancara**
          * [📊 Unduh Slide Hari 2 (PPTX/PDF)](https://example.com/materi-hari-2.pdf)
        """)

# ---------------------------------------------------------
# 4. ABSENSI HARIAN
# ---------------------------------------------------------
elif menu == "📝 Absensi Harian":
    st.title("📝 Form Absensi Kehadiran Petugas")
    st.write("Isi formulir kehadiran ini pada setiap hari pelaksanaan MOOC.")

    with st.form(key="form_absensi"):
        nama = st.text_input("Nama Lengkap Petugas *")
        id_petugas = st.text_input("ID Petugas / NIP *")
        kab_kota = st.selectbox("Kabupaten/Kota Tugas", ["Kota Bandung", "Kab. Garut", "Kab. Subang", "Kab. Tasikmalaya", "Lainnya"])
        hari_absensi = st.selectbox("Absensi Untuk Hari Ke-", ["Hari 1 (23 Sept)", "Hari 2 (24 Sept)"])
        catatan = st.text_area("Catatan / Kendala Harian (Opsional)")
        
        submit_absensi = st.form_submit_button("Kirim Absensi Kehadiran")

    if submit_absensi:
        if nama and id_petugas:
            st.success(f"✅ Terima kasih {nama}, absensi {hari_absensi} berhasil dicatat!")
        else:
            st.error("❌ Harap isi Nama dan ID Petugas sebelum mengirimkan absensi.")

# ---------------------------------------------------------
# 5. KUIS ASYNCHRONOUS
# ---------------------------------------------------------
elif menu == "✏️ Kuis Asynchronous":
    st.title("✏️ Kuis Evaluasi Asynchronous")
    st.write("Pilih kuis harian yang ingin Anda kerjakan. Anda hanya dapat mengirimkan jawaban 1 kali.")

    pilihan_kuis = st.radio("Pilih Kuis:", ["Kuis Hari 1: Metodologi & Pencacahan", "Kuis Hari 2: Pengawasan & CAPI"], horizontal=True)

    if pilihan_kuis == "Kuis Hari 1: Metodologi & Pencacahan":
        st.subheader("📝 Kuis Hari 1 (23 September 2026)")
        with st.form("kuis_hari_1"):
            nama_kuis = st.text_input("Nama Lengkap *")
            id_kuis = st.text_input("ID Petugas *")
            
            q1 = st.radio(
                "1. Apa cakupan utama pendataan Post Enumeration Survey Sensus Ekonomi 2026?",
                ["Hanya usaha skala besar", "Seluruh aktivitas ekonomi non-pertanian", "Hanya sektor perdagangan e-commerce", "Sektor pertanian skala mikro"]
            )
            q2 = st.radio(
                "2. Kriteria utama penetapan bangunan sebagai tempat usaha adalah?",
                ["Memiliki papan nama usaha", "Terdapat kegiatan transaksi/produksi barang & jasa", "Bangunan permanen bertingkat", "Memiliki izin legalitas PT/CV"]
            )
            
            submit_kuis1 = st.form_submit_button("Kirim Jawaban Kuis Hari 1")
            
            if submit_kuis1:
                if nama_kuis and id_kuis:
                    skor = 0
                    if q1 == "Seluruh aktivitas ekonomi non-pertanian": skor += 50
                    if q2 == "Terdapat kegiatan transaksi/produksi barang & jasa": skor += 50
                    
                    st.balloons()
                    st.success(f"🎉 Kuis Berhasil Dikirim! Skor Anda: **{skor} / 100**")
                else:
                    st.error("❌ Harap isi Nama dan ID Petugas.")

    elif pilihan_kuis == "Kuis Hari 2: Pengawasan & CAPI":
        st.subheader("📝 Kuis Hari 2 (24 September 2026)")
        with st.form("kuis_hari_2"):
            nama_kuis = st.text_input("Nama Lengkap *")
            id_kuis = st.text_input("ID Petugas *")
            
            q1 = st.radio(
                "1. Jika ditemukan usaha mikro yang tidak memiliki catatan keuangan resmi, tindakan petugas adalah?",
                ["Langsung mengosongkan kuesioner", "Melakukan teknik estimasi pendekatan pendapatan/pengeluaran", "Menghentikan wawancara", "Meminta responden membuat pembukuan dulu"]
            )
            q2 = st.radio(
                "2. Pengisian status keberadaan usaha yang telah pindah alamat dicatat sebagai?",
                ["Aktif di lokasi lama", "Pindah / Tidak Ditemukan", "Tutup Permanen", "Diabaikan"]
            )
            
            submit_kuis2 = st.form_submit_button("Kirim Jawaban Kuis Hari 2")
            
            if submit_kuis2:
                if nama_kuis and id_kuis:
                    skor = 0
                    if q1 == "Melakukan teknik estimasi pendekatan pendapatan/pengeluaran": skor += 50
                    if q2 == "Pindah / Tidak Ditemukan": skor += 50
                    
                    st.balloons()
                    st.success(f"🎉 Kuis Berhasil Dikirim! Skor Anda: **{skor} / 100**")
                else:
                    st.error("❌ Harap isi Nama dan ID Petugas.")

# Footer Teks Sederhana
st.divider()
st.caption("© 2026 BPS Provinsi Jawa Barat — Post Enumeration Survey Sensus Ekonomi 2026")
