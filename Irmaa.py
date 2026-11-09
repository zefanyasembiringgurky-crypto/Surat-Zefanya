import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os

# --- ZONA WAKTU WIB (UTC+7) ---
wib_offset = datetime.timezone(datetime.timedelta(hours=7))

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
    waktu_str = datetime.datetime.now(wib_offset).strftime("%d %B %Y - %H:%M:%S WIB")
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
    page_title="Yok Makan Bareng Ir 🍽️",
    page_icon="🍽️",
    layout="centered"
)

# Inisialisasi status login panel Zefanya & sambutan balon pertama kali
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state.welcomed = True

# Custom CSS Tema Biru Navy Elegan (Navy Blue Theme)
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 1-0%, #1e293b 100%), #0f172a;
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    .gray-card {
        background: #1e293b !important;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155;
        margin-bottom: 20px;
    }
    .main-title {
        text-align: center;
        color: #f8fafc;
        font-weight: 800;
        font-size: 1.6em;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-style: italic;
        margin-bottom: 24px;
        font-size: 0.95em;
    }
    .stRadio label p {
        color: #f8fafc !important;
        font-weight: 600 !important;
        font-size: 1.05em !important;
        padding: 4px 0;
    }
    div.stButton > button {
        background: #3b82f6;
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 600;
        padding: 12px 20px;
        border: none;
        width: 100%;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #2563eb;
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.5);
    }
    .welcome-note {
        text-align: center;
        color: #e2e8f0;
        font-size: 0.95em;
        margin-bottom: 16px;
        font-weight: 600;
        background: #334151;
        padding: 8px 16px;
        border-radius: 20px;
        display: inline-block;
        width: 100%;
        border: 1px solid #475569;
    }
    .message-box {
        background-color: #0f172a;
        border: 2px solid #475569;
        border-radius: 12px;
        padding: 18px;
        margin-top: 10px;
        margin-bottom: 10px;
        text-align: left;
        color: #f8fafc !important;
        font-size: 1.05em;
        font-weight: 500;
        line-height: 1.6;
    }
    h3, h4, p, label {
        color: #f8fafc !important;
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

# 3. VIDEO BACKSOUND TEGANG
url_video_ucapan = "https://youtu.be/OPhoNbL7kJc?si=U8tZ9whkI3IscVXA" 

with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='margin-top: 0; font-size: 1.15em;'>🎵 Suasana Hati Saat Ini</h3>
            <p style='color: #94a3b8; font-weight: 500; margin-bottom: 15px;'>Disini aku yang tegang nunggu jawaban kam...</p>
        </div>
    """, unsafe_allow_html=True)
    st.video(url_video_ucapan)

st.markdown("<br>", unsafe_allow_html=True)

# 4. PESAN PENTING BUAT IRMA
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='margin-top: 0; font-size: 1.15em;'>💌 Pesan Penting Buat Irma</h3>
            <div class='message-box'>
                "Ir, ehmm... sebenarnya aku udah mikirin hal ini dari kemarin-kemarin dan bolak-balik ragu mau mulai ngomongnya dari mana. Aku pengen banget ngajak kam makan bareng, luangin waktu sebentar aja. Untuk tempat makannya, tenang aja, aku udah tau tempatnya dan makanan di situ pasti kam suka atau pernah makan sebelumnya, walau mungkin tempatnya baru buat kam.<br><br>
                Oh iya, tujuan atau alasan aku ngajak kam makan bareng nanti bakal aku kasih tahu kalau kam mau ya! 😉<br><br>
                Jujur, dari kemarin aku mikir panjang karena sempat takut kam nolak atau risih, tapi setelah kupikir-pikir lagi, daripada aku penasaran dan nggak pernah nyoba ngomong, ya udah aku nekat bikin ini. Duh, ngetik atau ngomong gini aja rasanya deg-degan kali... Soalnya aku jujur ngarep kali kam mau terima ajakannya dan nemenin aku sebentar. Tapi tenang ya, aku hargai apapun keputusan kam, jadi semua balik ke kam lagi kok 🥺🤍"
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. PANEL PILIHAN TOMBOL JAWABAN
with st.container():
    st.markdown("""
        <div class='gray-card'>
            <h3 style='margin-top: 0; font-size: 1.15em;'>👇 Pilih ya Ir:</h3>
        </div>
    """, unsafe_allow_html=True)
    
    pilihan_list = ["✨ Belum memilih (Silakan klik salah satu)", "Mauuu", "Gak mau", "Yaudah iya"]
    
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
            <h3 style='margin-top: 0; font-size: 1.15em;'>📅 Pilih waktu kapan kam bisa Ir</h3>
            <p style='color: #94a3b8; font-size: 0.95em;'>waktu kam, silakan isi di bawah ya:</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        tanggal_pilihan = st.date_input("Pilih Tanggal:", key="input_tanggal")
    with col2:
        waktu_pilihan = st.text_input("Pilih Waktu:", key="input_waktu", placeholder="Contoh: Selesai jam sekolah")

st.markdown("<br>", unsafe_allow_html=True)

# 7. PANEL PENUTUP & TOMBOL SIMPAN KE DATABASE
with st.container():
    st.markdown("""
        <div class='gray-card' style='text-align: center;'>
            <p style='font-size: 1.05em; line-height: 1.5; font-weight: 500;'>
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
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.8em;'>Dibuat dengan penuh ketegangan dan ketulusan khusus buat Irma 🎂💙</p>", unsafe_allow_html=True)
