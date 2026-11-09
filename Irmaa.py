import streamlit as st
import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="Misi Ajak Irma Makan Bareng 🍽️",
    page_icon="🍽️",
    layout="centered"
)

# Custom CSS Tema Abu-Abu Putih (Gray & White Theme) dengan perbaikan warna teks radio
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
        color: #1f2937;
        font-family: 'Inter', sans-serif;
    }
    .gray-card {
        background: #ffffff !important;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #d1d5db;
        margin-bottom: 20px;
    }
    .main-title {
        text-align: center;
        color: #111827;
        font-weight: 800;
        font-size: 1.7em;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #4b5563;
        font-style: italic;
        margin-bottom: 20px;
    }
    /* Memastikan teks pilihan radio menjadi hitam pekat dan jelas */
    .stRadio label p, .stRadio div {
        color: #111827 !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
    }
    div.stButton > button {
        background: #374151;
        color: #ffffff !important;
        border-radius: 8px;
        font-weight: 600;
        padding: 10px 20px;
        border: none;
        width: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background: #111827;
    }
    </style>
"""
st.markdown(css_template, unsafe_allow_html=True)

# Inisialisasi Session State di awal jika belum ada
if 'radio_jawaban' not in st.session_state:
    st.session_state.radio_jawaban = "Mauuu"
if 'input_tanggal' not in st.session_state:
    st.session_state.input_tanggal = datetime.date.today()
if 'input_waktu' not in st.session_state:
    st.session_state.input_waktu = ""
if 'input_catatan' not in st.session_state:
    st.session_state.input_catatan = ""

# 1. UCAPAN TERIMA KASIH DI AWAL SEBELUM JUDUL
st.markdown("""
    <div style="text-align: center; color: #4b5563; font-size: 0.95em; margin-bottom: 12px; font-weight: 600;">
        ✨ Hai Ir, makasih banyak ya udah mau nyempetin waktu buat membuka link ini... ✨
    </div>
""", unsafe_allow_html=True)

# 2. JUDUL UTAMA YANG LUCU
st.markdown("<h1 class='main-title'>🚨 SITUASI DARURAT: Misi Nekat Ajak Bu Guru Makan Bareng 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Tolong dibaca sampai habis ya, jangan di-skip! 😆</p>", unsafe_allow_html=True)

# 3. PANEL MASUK TEGANG & VIDEO YOUTUBE
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0;'>🎵 Suasana Hati Saat Ini</h3>
            <p style='color: #4b5563; font-weight: 600;'>Disini aku yang tegang nunggu jawabannya...</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.video("https://youtu.be/OPhoNbL7kJc?si=U8tZ9whkI3IscVXA")

st.markdown("<br>", unsafe_allow_html=True)

# 4. PANEL KALIMAT AJAKAN JUMPA
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0;'>💌 Pesan Penting Buat Irma</h3>
            <p style='color: #1f2937; line-height: 1.6; font-size: 1.05em; font-weight: 500;'>
                "Ir, ehmm aku mau ajak kam makan bareng, untuk tempat makannya udah tau dan ini kam pernah makan, sebenarnya aku dari kemaren mikirin ini tapi takut kam ga mau tapi setelah kupikir-pikir daripada belum kucoba, gimana ya bilangnya aku deg-degan........ soalnya aku ngarep kali kam mau tapi kembali ke kam 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)

# 5. PANEL PILIHAN TOMBOL JAWABAN
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0;'>👇 Silakan Pilih Jawabannya di Bawah Ya:</h3>
        </div>
    """, unsafe_allow_html=True)
    
    pilihan = st.radio(
        "Pilih jawaban:",
        ("Mauuu", "Gak mau kalau ga jadi", "Yaudah iya"),
        key="radio_jawaban",
        label_visibility="collapsed"
    )

st.markdown("<br>", unsafe_allow_html=True)

# 6. PANEL WAKTU NGEDATE
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0;'>📅 Atur Jadwal Kapan Kamu Bisa</h3>
            <p style='color: #4b5563; font-size: 0.95em;'>Kapan pun waktu luangmu (jam pulang sekolah atau weekend), silakan isi di bawah ya:</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        tanggal_pilihan = st.date_input("Pilih Tanggal:", key="input_tanggal")
    with col2:
        waktu_pilihan = st.text_input("Pilih Waktu (misal: Selesai jam sekolah / Sore):", key="input_waktu", placeholder="Contoh: Selesai jam sekolah")
    
    catatan_tempat = st.text_input("Catatan / usulan tempat (opsional):", key="input_catatan", placeholder="Contoh: Tempat biasa / cafe X")

st.markdown("<br>", unsafe_allow_html=True)

# 7. PANEL PENUTUP & KIRIM KE WHATSAPP
with st.container():
    st.markdown("""
        <div class='gray-card' style='text-align: center;'>
            <p style='color: #1f2937; font-size: 1.05em; line-height: 1.5; font-weight: 500;'>
                "Terima kasih ya Ir, pilihan kam aku hargain kok, kalau mau aku senang banget tapi semisal kam ga mau gak papa 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    nomor_wa = "6281216464994"
    waktu_final = waktu_pilihan if waktu_pilihan else "Tidak diisi"
    catatan_final = catatan_tempat if catatan_tempat else "-"
    pesan_wa = f"Halo Zefanya, aku udah baca webnya nih. Jawabanku: {pilihan}. Jadwal luangku: {tanggal_pilihan} ({waktu_final}). Catatan: {catatan_final}"
    link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"
    
    st.markdown(f"""
        <a href="{link_wa}" target="_blank">
            <button style="width: 100%; background-color: #374151; color: white; padding: 12px 20px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 15px; text-align: center; display: block; text-decoration: none; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                📲 Kirim Jawaban & Jadwal ke WhatsApp Zefanya
            </button>
        </a>
    """, unsafe_allow_html=True)

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA
# ==========================================
st.markdown("<br><hr>", unsafe_allow_html=True)
with st.expander("🔒 Panel Khusus Zefanya (Hasil Pilihan & Jadwal Irma)"):
    st.markdown("Masukkan PIN rahasia untuk melihat jawaban Irma:")
    pin_input = st.text_input("PIN Rahasia:", type="password")
    PIN_RAHASIA = "2021" 
    
    if pin_input == PIN_RAHASIA:
        st.success("PIN benar! Berikut adalah respons yang terekam:")
        st.write(f"👉 **Pilihan Jawaban Irma:** {st.session_state.get('radio_jawaban', 'Belum memilih')}")
        st.write(f"📅 **Tanggal yang Dipilih:** {st.session_state.get('input_tanggal', '-')}")
        st.write(f"⏰ **Waktu yang Dipilih:** {st.session_state.get('input_waktu', '-') if st.session_state.get('input_waktu') else '(Kosong)'}")
        st.write(f"📍 **Catatan / Tempat:** {st.session_state.get('input_catatan', '-') if st.session_state.get('input_catatan') else '(Kosong)'}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tombol untuk mereset data dengan menghapus key dari session_state secara aman
        if st.button("🗑️ Hapus / Reset Jawaban Ini"):
            for key in ['radio_jawaban', 'input_tanggal', 'input_waktu', 'input_catatan']:
                if key in st.session_state:
                    del st.session_state[key]
            st.success("Data jawaban berhasil dihapus/direset!")
            st.rerun()
            
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 💙</p>", unsafe_allow_html=True)
