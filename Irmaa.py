import streamlit as st
import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="Misi Ajak Irma Makan Bareng 🍽️",
    page_icon="🍽️",
    layout="centered"
)

# --- PENANGANAN RESET STATE DI AWAL (Mencegah Error) ---
if st.session_state.get('do_reset', False):
    for key in ['radio_jawaban', 'input_tanggal', 'input_waktu']:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.do_reset = False
    st.rerun()

# Custom CSS Tema Abu-Abu Putih yang Lebih Cantik & Elegan
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
        color: #1f2937;
        font-family: 'Inter', sans-serif;
    }
    .gray-card {
        background: #ffffff !important;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
        border: 1px solid #d1d5db;
        margin-bottom: 20px;
    }
    .main-title {
        text-align: center;
        color: #111827;
        font-weight: 800;
        font-size: 1.6em;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }
    .subtitle {
        text-align: center;
        color: #4b5563;
        font-style: italic;
        margin-bottom: 24px;
        font-size: 0.95em;
    }
    /* Mempercantik tampilan pilihan radio agar lebih rapi dan elegan */
    .stRadio label p {
        color: #1f2937 !important;
        font-weight: 600 !important;
        font-size: 1.05em !important;
        padding: 4px 0;
    }
    div.stButton > button {
        background: #374151;
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 600;
        padding: 12px 20px;
        border: none;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #111827;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }
    .welcome-note {
        text-align: center;
        color: #4b5563;
        font-size: 0.95em;
        margin-bottom: 16px;
        font-weight: 600;
        background: #e5e7eb;
        padding: 8px 16px;
        border-radius: 20px;
        display: inline-block;
        width: 100%;
    }
    </style>
"""
st.markdown(css_template, unsafe_allow_html=True)

# 1. UCAPAN TERIMA KASIH DI AWAL SEBELUM JUDUL
st.markdown("""
    <div style="text-align: center;">
        <span class="welcome-note">✨ Hai Ir, makasih banyak ya udah mau nyempetin waktu buat membuka link ini... ✨</span>
    </div>
""", unsafe_allow_html=True)

# 2. JUDUL UTAMA
st.markdown("<h1 class='main-title'>🚨 SITUASI DARURAT: Misi Nekat Ajak Bu Guru Makan Bareng 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Tolong dibaca sampai habis ya, jangan di-skip! 😆</p>", unsafe_allow_html=True)

# 3. PANEL MASUK TEGANG & VIDEO YOUTUBE
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>🎵 Suasana Hati Saat Ini</h3>
            <p style='color: #4b5563; font-weight: 500; margin-bottom: 15px;'>Disini aku yang tegang nunggu jawabannya...</p>
        </div>
    """, unsafe_allow_html=True)
    st.video("https://youtu.be/OPhoNbL7kJc?si=U8tZ9whkI3IscVXA")

st.markdown("<br>", unsafe_allow_html=True)

# 4. PANEL KALIMAT AJAKAN JUMPA
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>💌 Pesan Penting Buat Irma</h3>
            <p style='color: #1f2937; line-height: 1.6; font-size: 1.05em; font-weight: 500;'>
                "Ir, ehmm aku mau ajak kam makan bareng, untuk tempat makannya udah tau dan ini kam pernah makan, sebenarnya aku dari kemaren mikirin ini tapi takut kam ga mau tapi setelah kupikir-pikir daripada belum kucoba, gimana ya bilangnya aku deg-degan........ soalnya aku ngarep kali kam mau tapi kembali ke kam 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)

# 5. PANEL PILIHAN TOMBOL JAWABAN (Tanpa langsung terpilih di awal)
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>👇 Silakan Pilih Jawabannya di Bawah Ya:</h3>
        </div>
    """, unsafe_allow_html=True)
    
    pilihan_list = ["✨ Belum memilih (Silakan klik salah satu)", "Mauuu", "Gak mau kalau ga jadi", "Yaudah iya"]
    
    pilihan = st.radio(
        "Pilih jawaban:",
        pilihan_list,
        key="radio_jawaban",
        label_visibility="collapsed"
    )

st.markdown("<br>", unsafe_allow_html=True)

# 6. PANEL WAKTU NGEDATE
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>📅 Atur Jadwal Kapan Kamu Bisa</h3>
            <p style='color: #4b5563; font-size: 0.95em;'>Kapan pun waktu luangmu (jam pulang sekolah atau weekend), silakan isi di bawah ya:</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        tanggal_pilihan = st.date_input("Pilih Tanggal:", key="input_tanggal")
    with col2:
        waktu_pilihan = st.text_input("Pilih Waktu (misal: Selesai jam sekolah / Sore):", key="input_waktu", placeholder="Contoh: Selesai jam sekolah")

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
    jawaban_final = pilihan if pilihan != "✨ Belum memilih (Silakan klik salah satu)" else "Belum memilih"
    waktu_final = waktu_pilihan if waktu_pilihan else "Tidak diisi"
    pesan_wa = f"Halo Zefanya, aku udah baca webnya nih. Jawabanku: {jawaban_final}. Jadwal luangku: {tanggal_pilihan} ({waktu_final})."
    link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"
    
    st.markdown(f"""
        <a href="{link_wa}" target="_blank">
            <button style="width: 100%; background-color: #374151; color: white; padding: 12px 20px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 15px; text-align: center; display: block; text-decoration: none; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
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
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tombol untuk mereset data
        if st.button("🗑️ Hapus / Reset Jawaban Ini"):
            st.session_state.do_reset = True
            st.rerun()
            
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 💙</p>", unsafe_allow_html=True)
