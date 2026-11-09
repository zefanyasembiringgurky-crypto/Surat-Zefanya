import streamlit as st
import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="Misi Ajak Irma Makan Bareng 🍽️",
    page_icon="🍽️",
    layout="centered"
)

# --- INISIALISASI SESSION STATE UNTUK RIWAYAT JAWABAN ---
if 'riwayat_jawaban' not in st.session_state:
    st.session_state.riwayat_jawaban = []

# Custom CSS Tema Abu-Abu Putih Super Elegan & Estetis
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        color: #1e293b;
        font-family: 'Inter', sans-serif;
    }
    .gray-card {
        background: #ffffff !important;
        padding: 26px;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
        border: 1px solid #cbd5e1;
        margin-bottom: 22px;
    }
    .main-title {
        text-align: center;
        color: #0f172a;
        font-weight: 800;
        font-size: 1.65em;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        font-style: italic;
        margin-bottom: 28px;
        font-size: 0.95em;
    }
    /* Mempercantik tampilan pilihan radio */
    .stRadio label p {
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 1.05em !important;
        padding: 6px 0;
    }
    div.stButton > button {
        background: #334155;
        color: #ffffff !important;
        border-radius: 12px;
        font-weight: 600;
        padding: 12px 24px;
        border: none;
        width: 100%;
        box-shadow: 0 4px 12px rgba(51, 65, 85, 0.2);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #0f172a;
        box-shadow: 0 6px 16px rgba(15, 23, 42, 0.3);
    }
    .welcome-badge {
        text-align: center;
        color: #475569;
        font-size: 0.9em;
        margin-bottom: 20px;
        font-weight: 600;
        background: #e2e8f0;
        padding: 8px 18px;
        border-radius: 30px;
        display: inline-block;
        width: 100%;
        border: 1px solid #cbd5e1;
    }
    .history-item {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        padding: 14px 18px;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    </style>
"""
st.markdown(css_template, unsafe_allow_html=True)

# 1. UCAPAN TERIMA KASIH DI AWAL
st.markdown("""
    <div style="text-align: center;">
        <span class="welcome-badge">✨ Hai Ir, makasih banyak ya udah mau nyempetin waktu buat membuka link ini... ✨</span>
    </div>
""", unsafe_allow_html=True)

# 2. JUDUL UTAMA
st.markdown("<h1 class='main-title'>🚨 SITUASI DARURAT: Misi Nekat Ajak Bu Guru Makan Bareng 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Tolong dibaca sampai habis ya, jangan di-skip! 😆</p>", unsafe_allow_html=True)

# 3. PANEL MASUK TEGANG & VIDEO YOUTUBE
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #334155; margin-top: 0; font-size: 1.15em; font-weight: 700;'>🎵 Suasana Hati Saat Ini</h3>
            <p style='color: #64748b; font-weight: 500; margin-bottom: 16px;'>Disini aku yang tegang nunggu jawabannya...</p>
        </div>
    """, unsafe_allow_html=True)
    st.video("https://youtu.be/OPhoNbL7kJc?si=U8tZ9whkI3IscVXA")

st.markdown("<br>", unsafe_allow_html=True)

# 4. PANEL KALIMAT AJAKAN JUMPA
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #334155; margin-top: 0; font-size: 1.15em; font-weight: 700;'>💌 Pesan Penting Buat Irma</h3>
            <p style='color: #1e293b; line-height: 1.65; font-size: 1.05em; font-weight: 500;'>
                "Ir, ehmm aku mau ajak kam makan bareng, untuk tempat makannya udah tau dan ini kam pernah makan, sebenarnya aku dari kemaren mikirin ini tapi takut kam ga mau tapi setelah kupikir-pikir daripada belum kucoba, gimana ya bilangnya aku deg-degan........ soalnya aku ngarep kali kam mau tapi kembali ke kam 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)

# 5. PANEL PILIHAN TOMBOL JAWABAN
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #334155; margin-top: 0; font-size: 1.15em; font-weight: 700;'>👇 Silakan Pilih Jawabannya di Bawah Ya:</h3>
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
            <h3 style='color: #334155; margin-top: 0; font-size: 1.15em; font-weight: 700;'>📅 Atur Jadwal Kapan Kamu Bisa</h3>
            <p style='color: #64748b; font-size: 0.95em; margin-bottom: 15px;'>Kapan pun waktu luangmu (jam pulang sekolah atau weekend), silakan isi di bawah ya:</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        tanggal_pilihan = st.date_input("Pilih Tanggal:", key="input_tanggal")
    with col2:
        waktu_pilihan = st.text_input("Pilih Waktu (misal: Selesai jam sekolah / Sore):", key="input_waktu", placeholder="Contoh: Selesai jam sekolah")

st.markdown("<br>", unsafe_allow_html=True)

# 7. PANEL PENUTUP & TOMBOL KIRIM / SIMPAN JAWABAN
with st.container():
    st.markdown("""
        <div class='gray-card' style='text-align: center;'>
            <p style='color: #1e293b; font-size: 1.05em; line-height: 1.6; font-weight: 500; margin-bottom: 20px;'>
                "Terima kasih ya Ir, pilihan kam aku hargain kok, kalau mau aku senang banget tapi semisal kam ga mau gak papa 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    nomor_wa = "6281216464994"
    jawaban_final = pilihan if pilihan != "✨ Belum memilih (Silakan klik salah satu)" else "Belum memilih"
    waktu_final = waktu_pilihan if waktu_pilihan else "Tidak diisi"
    
    # Tombol Simpan ke Riwayat & Kirim ke WhatsApp
    if st.button("📲 Simpan Jawaban & Kirim ke WhatsApp Zefanya"):
        if jawaban_final == "Belum memilih":
            st.warning("⚠️ Hei, pilih dulu salah satu jawabannya ya sebelum dikirim! 😄")
        else:
            # Simpan data ke dalam daftar riwayat (history)
            data_baru = {
                "pilihan": jawaban_final,
                "tanggal": str(tanggal_pilihan),
                "waktu": waktu_final,
                "timestamp": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            }
            st.session_state.riwayat_jawaban.append(data_baru)
            
            # Buat link WhatsApp
            pesan_wa = f"Halo Zefanya, aku udah baca webnya nih. Jawabanku: {jawaban_final}. Jadwal luangku: {tanggal_pilihan} ({waktu_final})."
            link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"
            
            st.success("🎉 Jawaban berhasil direkam dan dikirim! Terima kasih ya, Ir!")
            st.markdown(f"""
                <script>
                    window.open('{link_wa}', '_blank');
                </script>
                <div style="text-align: center; margin-top: 15px;">
                    <a href="{link_wa}" target="_blank">
                        <button style="background-color: #16a34a; color: white; padding: 10px 20px; border-radius: 10px; font-weight: bold; border: none; cursor: pointer;">
                            Klik di Sini Jika WhatsApp Tidak Terbuka Otomatis 🟢
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA (DENGAN PILIHAN HAPUS PER ITEM)
# ==========================================
st.markdown("<br><hr>", unsafe_allow_html=True)
with st.expander("🔒 Panel Khusus Zefanya (Riwayat Pilihan & Jadwal Irma)"):
    st.markdown("Masukkan PIN rahasia untuk melihat semua riwayat jawaban Irma:")
    pin_input = st.text_input("PIN Rahasia:", type="password")
    PIN_RAHASIA = "2021" 
    
    if pin_input == PIN_RAHASIA:
        st.success("PIN benar! Berikut adalah daftar riwayat respons yang terekam:")
        
        if len(st.session_state.riwayat_jawaban) == 0:
            st.info("Belum ada respons atau jawaban yang tersimpan di riwayat.")
        else:
            st.markdown(f"**Total Respons Masuk: {len(st.session_state.riwayat_jawaban)}**")
            
            # Tampilkan setiap item riwayat dengan tombol hapus masing-masing
            for idx, item in enumerate(st.session_state.riwayat_jawaban):
                st.markdown(f"""
                    <div class='history-item'>
                        <b>Respon ke-{idx + 1}</b> ({item['timestamp']})<br>
                        👉 <b>Pilihan:</b> {item['pilihan']}<br>
                        📅 <b>Tanggal:</b> {item['tanggal']}<br>
                        ⏰ <b>Waktu:</b> {item['waktu']}
                    </div>
                """, unsafe_allow_html=True)
                
                # Tombol hapus spesifik untuk item ini
                if st.button(f"🗑️ Hapus Respons #{idx + 1}", key=f"del_{idx}"):
                    st.session_state.riwayat_jawaban.pop(idx)
                    st.success(f"Respons #{idx + 1} berhasil dihapus!")
                    st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🗑️ Hapus / Reset Semua Riwayat"):
                st.session_state.riwayat_jawaban = []
                st.success("Semua riwayat berhasil dikosongkan!")
                st.rerun()
                
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 💙</p>", unsafe_allow_html=True)
