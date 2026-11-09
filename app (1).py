import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os
import time

# --- INISIALISASI DATABASE SQLITE UNTUK IRMA ---
def init_db():
    conn = sqlite3.connect('jawaban_irma.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topik TEXT,
            jawaban TEXT,
            waktu TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def save_response(topik, jawaban):
    conn = sqlite3.connect('jawaban_irma.db', check_same_thread=False)
    c = conn.cursor()
    waktu_str = datetime.datetime.now().strftime("%d %B %Y - %H:%M:%S")
    c.execute('INSERT INTO responses (topik, jawaban, waktu) VALUES (?, ?, ?)', (topik, jawaban, waktu_str))
    conn.commit()
    conn.close()

def delete_response(resp_id):
    conn = sqlite3.connect('jawaban_irma.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('DELETE FROM responses WHERE id = ?', (resp_id,))
    conn.commit()
    conn.close()

def get_responses():
    conn = sqlite3.connect('jawaban_irma.db', check_same_thread=False)
    try:
        df_resp = pd.read_sql_query('SELECT * FROM responses ORDER BY id DESC', conn)
    except:
        df_resp = pd.DataFrame(columns=['id', 'topik', 'jawaban', 'waktu'])
    conn.close()
    return df_resp

# Konfigurasi Halaman
st.set_page_config(
    page_title="Misi Ajak Irma Makan Bareng 🍽️",
    page_icon="🍽️",
    layout="centered"
)

# Custom CSS Tema Abu-Abu Putih Elegan (Gray & White Theme)
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
    /* Mempercantik tampilan pilihan radio */
    .stRadio label p {
        color: #111827 !important;
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
    .message-box {
        background-color: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 12px;
        padding: 18px;
        margin-top: 10px;
        margin-bottom: 10px;
        text-align: left;
        color: #1f2937 !important;
        font-size: 1.05em;
        font-weight: 500;
        line-height: 1.6;
    }
    </style>
"""
st.markdown(css_template, unsafe_allow_html=True)

# 1. UCAPAN TERIMA KASIH DI AWAL
st.markdown("""
    <div style="text-align: center;">
        <span class="welcome-note">✨ Hai Ir, makasih banyak ya udah mau nyempetin waktu buat membuka link ini... ✨</span>
    </div>
""", unsafe_allow_html=True)

# 2. JUDUL UTAMA
st.markdown("<h1 class='main-title'>🚨 SITUASI DARURAT: Misi Nekat Ajak Bu Guru Makan Bareng 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Tolong dibaca sampai habis ya, jangan di-skip! 😆</p>", unsafe_allow_html=True)

# 3. VIDEO UCAPAN YOUTUBE (Sesuai link pilihanmu)
url_video_ucapan = "https://youtu.be/AEKRXpBMa2w?si=0d44nYIBrNer_yBB" 

with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>🎥 Video Ucapan & Suasana Hati</h3>
            <p style='color: #4b5563; font-weight: 500; margin-bottom: 15px;'>Disini aku yang tegang nunggu jawabannya...</p>
        </div>
    """, unsafe_allow_html=True)
    st.video(url_video_ucapan)

st.markdown("<br>", unsafe_allow_html=True)

# 4. PESAN PENTING BUAT IRMA
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>💌 Pesan Penting Buat Irma</h3>
            <div class='message-box'>
                "Ir, ehmm aku mau ajak kam makan bareng, untuk tempat makannya udah tau dan ini kam pernah makan, sebenarnya aku dari kemaren mikirin ini tapi takut kam ga mau tapi setelah kupikir-pikir daripada belum kucoba, gimana ya bilangnya aku deg-degan........ soalnya aku ngarep kali kam mau tapi kembali ke kam 🥺"
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. PANEL PILIHAN TOMBOL JAWABAN
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

# 7. PANEL PENUTUP & SIMPAN KE DATABASE + WHATSAPP
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
    
    if st.button("📲 Simpan Jawaban & Kirim ke WhatsApp Zefanya"):
        if jawaban_final == "Belum memilih":
            st.warning("⚠️ Pilih dulu salah satu jawabannya ya sebelum dikirim! 😄")
        else:
            # Simpan ke database SQLite
            save_response("Pilihan Ajakan Makan", jawaban_final)
            save_response("Jadwal Luang", f"Tanggal: {tanggal_pilihan} | Waktu: {waktu_final}")
            
            pesan_wa = f"Halo Zefanya, aku udah baca webnya nih. Jawabanku: {jawaban_final}. Jadwal luangku: {tanggal_pilihan} ({waktu_final})."
            link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"
            
            st.success("🎉 Respons dan jadwalmu berhasil direkam dan dikirim ke Zefanya! Terima kasih ya, Ir!")
            st.markdown(f"""
                <div style="text-align: center; margin-top: 15px;">
                    <a href="{link_wa}" target="_blank">
                        <button style="background-color: #22c55e; color: white; padding: 12px 20px; border-radius: 10px; font-weight: bold; border: none; cursor: pointer;">
                            Klik di Sini Jika WhatsApp Tidak Terbuka Otomatis 🟢
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA (DENGAN SQLITE, TABEL, GRAFIK, & HAPUS ID)
# ==========================================
st.markdown("<br><hr>", unsafe_allow_html=True)
with st.expander("🔒 Panel Khusus Zefanya"):
    st.markdown("Masukkan PIN rahasia:")
    pin_input = st.text_input("PIN Rahasia:", type="password")
    PIN_RAHASIA = "2021" 
    
    if pin_input == PIN_RAHASIA:
        st.success("PIN benar! Selamat datang, Bos.")
        df_data = get_responses()
        if not df_data.empty:
            st.dataframe(df_data, use_container_width=True)
            
            st.markdown("---")
            st.markdown("📊 **Grafik Statistik Respons Irma:**")
            topic_counts = df_data['topik'].value_counts()
            st.bar_chart(topic_counts)
            
            st.markdown("---")
            st.markdown("🗑️ **Hapus Jawaban Berdasarkan ID:**")
            id_to_delete = st.number_input("Masukkan Nomor ID:", min_value=1, step=1)
            if st.button("❌ Hapus Jawaban Ini"):
                if id_to_delete in df_data['id'].values:
                    delete_response(id_to_delete)
                    st.success(f"ID {id_to_delete} berhasil dihapus dari database!")
                    st.rerun()
                else:
                    st.error("ID tidak ditemukan dalam database.")
        else:
            st.info("Belum ada data respons tersimpan di database.")
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 🎂💙</p>", unsafe_allow_html=True)
