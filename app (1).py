import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os

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

# Inisialisasi status login panel Zefanya
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

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

# 3. VIDEO UCAPAN YOUTUBE
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

# 4. PESAN PENTING BUAT IRMA (Sudah diperbarui sesuai gaya bahasa & tambahan tujuan)
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='color: #374151; margin-top: 0; font-size: 1.15em;'>💌 Pesan Penting Buat Irma</h3>
            <div class='message-box'>
                ""Ir, ehmm... sebenarnya aku udah mikirin hal ini dari kemarin-kemarin dan bolak-balik ragu mau mulai ngomongnya dari mana. Aku pengen banget ngajak kam makan bareng, luangin waktu sebentar aja. Untuk tempat makannya, tenang aja, aku udah tau tempatnya dan makanan di situ pasti kam suka atau pernah makan sebelumnya, walau mungkin tempatnya baru buat kam.

Jujur, dari kemarin aku mikir panjang karena sempat takut kam nolak atau risih, tapi setelah kupikir-pikir lagi, daripada aku penasaran dan nggak pernah nyoba ngomong, ya udah aku nekat bikin ini. Duh, ngetik atau ngomong gini aja rasanya deg-degan kali... Soalnya aku jujur ngarep kali kam mau terima ajakannya dan nemenin aku sebentar. Tapi tenang ya, aku hargai apapun keputusan kam, jadi semua balik ke kam lagi kok 🥺🤍"        </div>
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

# 7. PANEL PENUTUP & TOMBOL SIMPAN KE DATABASE (Fokus Database Saja)
with st.container():
    st.markdown("""
        <div class='gray-card' style='text-align: center;'>
            <p style='color: #1f2937; font-size: 1.05em; line-height: 1.5; font-weight: 500;'>
                "Terima kasih ya Ir, pilihan kam aku hargain kok, kalau mau aku senang banget tapi semisal kam ga mau gak papa 🥺"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    jawaban_final = pilihan if pilihan != "✨ Belum memilih (Silakan klik salah satu)" else "Belum memilih"
    waktu_final = waktu_pilihan if waktu_pilihan else "Tidak diisi"
    
    if st.button("💾 Kirim & Simpan Jawabannya"):
        if jawaban_final == "Belum memilih":
            st.warning("⚠️ Pilih dulu salah satu jawabannya ya sebelum dikirim! 😄")
        else:
            # Simpan langsung ke database SQLite
            save_response("Pilihan Ajakan Makan", jawaban_final)
            save_response("Jadwal Luang", f"Tanggal: {tanggal_pilihan} | Waktu: {waktu_final}")
            
            st.success("🎉 Terima kasih ya, Ir! Jawabannya sudah berhasil dikirim dan tersimpan rapi.")
            st.balloons()

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA
# ==========================================
st.markdown("<br><hr>", unsafe_allow_html=True)
with st.expander("🔒 Panel Khusus Zefanya"):
    if not st.session_state.authenticated:
        st.markdown("Masukkan PIN rahasia:")
        pin_input = st.text_input("PIN Rahasia:", type="password", key="pin_input_box")
        PIN_RAHASIA = "2021" 
        
        if pin_input == PIN_RAHASIA:
            st.session_state.authenticated = True
            st.rerun()
        elif pin_input:
            st.error("PIN salah.")
    else:
        st.success("PIN benar! Selamat datang, Bos.")
        if st.button("🔒 Kunci Kembali Panel"):
            st.session_state.authenticated = False
            st.rerun()
            
        df_data = get_responses()
        if not df_data.empty:
            st.dataframe(df_data, use_container_width=True)
            
            st.markdown("---")
            st.markdown("📊 **Grafik Statistik Respons Irma:**")
            topic_counts = df_data['topik'].value_counts()
            st.bar_chart(topic_counts)
            
            st.markdown("---")
            st.markdown("🗑️ **Hapus Jawaban Berdasarkan ID:**")
            id_to_delete = st.number_input("Masukkan Nomor ID:", min_value=1, step=1, key="del_id_input")
            if st.button("❌ Hapus Jawaban Ini"):
                if id_to_delete in df_data['id'].values:
                    delete_response(id_to_delete)
                    st.success(f"ID {id_to_delete} berhasil dihapus dari database!")
                    st.rerun()
                else:
                    st.error("ID tidak ditemukan dalam database.")
        else:
            st.info("Belum ada data respons tersimpan di database.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 🎂💙</p>", unsafe_allow_html=True)
