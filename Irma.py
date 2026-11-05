import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os
import time

# --- INISIALISASI DATABASE SQLITE UNTUK IRMA ---
def init_db():
    conn = sqlite3.connect('pesan_irma.db', check_same_thread=False)
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
    conn = sqlite3.connect('pesan_irma.db', check_same_thread=False)
    c = conn.cursor()
    waktu_str = datetime.datetime.now().strftime("%d %B %Y - %H:%M:%S")
    c.execute('INSERT INTO responses (topik, jawaban, waktu) VALUES (?, ?, ?)', (topik, jawaban, waktu_str))
    conn.commit()
    conn.close()

def delete_response(resp_id):
    conn = sqlite3.connect('pesan_irma.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('DELETE FROM responses WHERE id = ?', (resp_id,))
    conn.commit()
    conn.close()

def get_responses():
    conn = sqlite3.connect('pesan_irma.db', check_same_thread=False)
    try:
        df_resp = pd.read_sql_query('SELECT * FROM responses ORDER BY id DESC', conn)
    except:
        df_resp = pd.DataFrame(columns=['id', 'topik', 'jawaban', 'waktu'])
    conn.close()
    return df_resp

# Konfigurasi Halaman
st.set_page_config(
    page_title="Happy Birthday Irma Kristiani Ginting 🎂", 
    page_icon="🎉", 
    layout="centered"
)

# --- ZONA WAKTU WIB (UTC+7) ---
wib_offset = datetime.timezone(datetime.timedelta(hours=7))
now_wib = datetime.datetime.now(wib_offset)
current_hour = now_wib.hour

# Custom CSS & Tema Biru Putih yang Elegan (Proporsional & Rapi)
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 50%, #f0fdf4 100%);
        color: #0f172a;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: #0369a1;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 2.1em;
        padding-top: 10px;
        text-shadow: 0 2px 8px rgba(255,255,255,0.9);
    }
    .subtitle {
        text-align: center;
        color: #0284c7;
        font-style: italic;
        margin-bottom: 25px;
        font-weight: 700;
        font-size: 1.05em;
    }
    .love-card {
        background: #ffffff !important;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.08);
        border: 2px solid #38bdf8;
        text-align: center;
        margin-bottom: 20px;
        color: #0f172a !important;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: #0369a1 !important;
        font-weight: 800 !important;
        font-size: 1.35em !important;
    }
    .love-card h4 {
        color: #0284c7 !important;
        font-weight: 700 !important;
        font-size: 1.15em !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1em !important;
    }
    .message-box {
        background-color: #f8fafc;
        border: 2px solid #bae6fd;
        border-radius: 12px;
        padding: 16px;
        margin-top: 10px;
        margin-bottom: 10px;
        text-align: left;
        color: #1e293b !important;
        font-size: 1.02em;
        font-weight: 600;
        line-height: 1.5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 10px !important;
    }
    .img-frame {
        background: #ffffff;
        padding: 10px;
        border-radius: 14px;
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.25);
        border: 3px solid #0ea5e9;
        margin-bottom: 12px;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        border: 2px solid #38bdf8 !important;
    }
    div.stButton > button {
        background: #0284c7;
        color: #ffffff !important;
        border-radius: 12px;
        font-weight: 700;
        font-size: 15px;
        padding: 12px 20px;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 14px rgba(2, 132, 199, 0.3);
        width: 100%;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background: #0369a1;
        opacity: 0.95;
        border-color: #e0f2fe;
    }
    @keyframes floatDown {
        0% { transform: translateY(-10vh) scale(1) rotate(0deg); opacity: 0; }
        15% { opacity: 0.95; }
        85% { opacity: 0.95; }
        100% { transform: translateY(105vh) scale(1.15) rotate(360deg); opacity: 0; }
    }
    .floating-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        overflow: hidden; pointer-events: none; z-index: 1;
    }
    .floating-item {
        position: absolute; top: -60px;
        font-size: 26px; font-weight: 800;
        color: #0284c7;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.9);
        animation: floatDown 10s infinite linear;
    }
    </style>
    <div class="floating-bg">
        <div class="floating-item" style="left: 4%; animation-duration: 9s; animation-delay: 0s;">H</div>
        <div class="floating-item" style="left: 9%; animation-duration: 11s; animation-delay: 2s;">A</div>
        <div class="floating-item" style="left: 14%; animation-duration: 8s; animation-delay: 1s;">P</div>
        <div class="floating-item" style="left: 19%; animation-duration: 12s; animation-delay: 3s;">P</div>
        <div class="floating-item" style="left: 24%; animation-duration: 9.5s; animation-delay: 0.5s;">Y</div>
        <div class="floating-item" style="left: 31%; animation-duration: 10s; animation-delay: 2s;">🎂</div>
        <div class="floating-item" style="left: 38%; animation-duration: 11.5s; animation-delay: 1.5s;">B</div>
        <div class="floating-item" style="left: 43%; animation-duration: 8.5s; animation-delay: 3.5s;">I</div>
        <div class="floating-item" style="left: 48%; animation-duration: 10s; animation-delay: 0.8s;">R</div>
        <div class="floating-item" style="left: 53%; animation-duration: 9s; animation-delay: 2.2s;">T</div>
        <div class="floating-item" style="left: 58%; animation-duration: 10.5s; animation-delay: 1.2s;">H</div>
        <div class="floating-item" style="left: 63%; animation-duration: 8.5s; animation-delay: 0.2s;">D</div>
        <div class="floating-item" style="left: 68%; animation-duration: 11s; animation-delay: 2.8s;">A</div>
        <div class="floating-item" style="left: 73%; animation-duration: 9.2s; animation-delay: 1.8s;">Y</div>
        <div class="floating-item" style="left: 80%; animation-duration: 10.5s; animation-delay: 0.5s;">💙</div>
        <div class="floating-item" style="left: 86%; animation-duration: 8s; animation-delay: 2.5s;">I</div>
        <div class="floating-item" style="left: 91%; animation-duration: 11.5s; animation-delay: 1.1s;">R</div>
        <div class="floating-item" style="left: 95%; animation-duration: 9s; animation-delay: 3.2s;">M</div>
        <div class="floating-item" style="left: 98%; animation-duration: 10.2s; animation-delay: 0.7s;">A</div>
    </div>
"""

st.markdown(css_template, unsafe_allow_html=True)

# 🎈 Efek Balon Sambutan Utama
if 'welcomed_irma' not in st.session_state:
    st.balloons()
    st.session_state['welcomed_irma'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Happy Birthday Irma Kristiani Ginting! 🎂💙</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A very special day for a very special person! ✨</p>", unsafe_allow_html=True)

# --- 1. SOUNDTRACK ULANG TAHUN (DIPINDAH KE PALING ATAS DI BAWAH JUDUL) ---
url_lagu_irma = "https://www.youtube.com/watch?v=4oxarzdbEuw" 

st.markdown("<div class='love-card'><h3>🎵 Soundtrack Ulang Tahun</h3><p>Lagu spesial penuh berkat untuk menemani harimu:</p>", unsafe_allow_html=True)
st.markdown("**♪ Happy Birthday Tuhan Berkati — Maranatha Singer**")
st.video(url_lagu_irma)

st.markdown(f"""
    <a href="{url_lagu_irma}" target="_blank">
        <button style="margin-top: 8px; width: 100%; background: #ef4444; color: white; padding: 10px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 14px;">
            ▶️ Buka YouTube Langsung (Jika Video Tidak Berputar)
        </button>
    </a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 2. UCAPAN & SURAT SPESIAL ULANG TAHUN ---
st.markdown("<div class='love-card'><h3>💌 Pesan Spesial Hari Ini</h3>", unsafe_allow_html=True)
st.markdown("<h4>Selamat Ulang Tahun, Irma! 🥳</h4>", unsafe_allow_html=True)
st.markdown("""
    <div class='message-box'>
    Halo Irma Kristiani Ginting! 🌟<br><br>
    Selamat bertambah usia ya! Semoga di umur yang baru ini, segala hal baik, kebahagiaan, kesehatan, dan kelancaran selalu menyertai setiap langkahmu. Terima kasih sudah menjadi pribadi yang hebat. Semoga hari-harimu ke depan dipenuhi senyuman dan hal-hal indah yang pantas kamu dapatkan! 🎂✨
    </div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 3. FOTO SPESIAL IRMA ---
st.markdown("<div class='love-card'><h3>📸 Spesial Untukmu Hari Ini</h3>", unsafe_allow_html=True)

if os.path.exists("foto_irma.jpeg"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.95em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
elif os.path.exists("foto_irma.jpg"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.95em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
elif os.path.exists("foto_irma.png"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.95em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
else:
    st.info("💡 Letakkan foto dengan nama 'foto_irma.jpeg' di GitHub agar fotonya tampil di sini ya!")

st.markdown("</div>", unsafe_allow_html=True)

# --- 4. KOTAK KADO KEJUTAN (SURPRISE INTERAKTIF) ---
st.markdown("<div class='love-card'><h3>🎁 Kotak Kado Kejutan Rahasia</h3><p>Ssst... Ada pesan kejutan rahasia khusus buat kamu di dalam kado ini. Coba klik tombolnya:</p>", unsafe_allow_html=True)

if 'open_gift' not in st.session_state:
    st.session_state['open_gift'] = False

if not st.session_state['open_gift']:
    if st.button("🎁 Buka Kado Kejutan Sekarang"):
        with st.spinner("Mempersiapkan kejutan spesial..."):
            time.sleep(1.2)
        st.session_state['open_gift'] = True
        st.rerun()
else:
    st.balloons()
    st.markdown("""
        <div style="background: linear-gradient(135deg, #0284c7 100%, #0369a1 0%); padding: 20px; border-radius: 14px; color: #ffffff; text-align: center; box-shadow: 0 6px 20px rgba(2,132,199,0.3);">
            <h3 style="margin-bottom: 8px; color: #fde047 !important;">🎉 SURPRISE! YOU'RE AMAZING! 🎉</h3>
            <p style="font-size: 1.05em; font-weight: 600; color: #f8fafc !important; line-height: 1.6;">
                "Semoga di tahun ini semua impian terbesarmu tercapai, dilancarkan segala urusannya, dan selalu dikelilingi orang-orang tulus. Have the happiest birthday ever, Irma Kristiani Ginting!" 🤍✨
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- 5. KOTAK UCAPAN / BALASAN DARI IRMA ---
st.markdown("<div class='love-card'><h3>✍️ Kirim Balasan / Pesan</h3><p>Ketik kesan atau pesan balasanmu di sini (pesannya akan langsung masuk ke sistem Zefanya):</p>", unsafe_allow_html=True)
pesan_irma = st.text_area("Tulis pesan atau ucapan terima kasih di sini...")
if st.button("Kirim Pesan"):
    if pesan_irma.strip():
        save_response("Pesan Ulang Tahun Irma", pesan_irma)
        st.success("Yeay! Pesan dan ucapanmu berhasil tersimpan! 💙✨")
        st.balloons()
    else:
        st.warning("Tulis dulu pesannya ya, Irma.")
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. KONFIRMASI WHATSAPP ---
st.markdown("<div class='love-card'><h3>✅ Konfirmasi ke Zefanya</h3><p>Udah buka kejutannya? Kirim kabar ke WhatsApp Zefanya yuk:</p>", unsafe_allow_html=True)
nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, makasih banyak ya buat kejutan website ulang tahun bertema biru putih ini! 🎉✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width: 100%; background-color: #22c55e; color: white; padding: 12px 18px; border: none; border-radius: 12px; font-weight: 700; font-size: 15px; cursor: pointer;">
            📲 Kirim Ucapan Terima Kasih via WhatsApp
        </button>
    </a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA
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
            st.markdown("🗑️ **Hapus Pesan:**")
            id_to_delete = st.number_input("Masukkan Nomor ID:", min_value=1, step=1)
            if st.button("❌ Hapus Pesan Ini"):
                if id_to_delete in df_data['id'].values:
                    delete_response(id_to_delete)
                    st.success(f"ID {id_to_delete} berhasil dihapus!")
                    st.rerun()
                else:
                    st.error("ID tidak ditemukan.")
        else:
            st.info("Belum ada pesan tersimpan dari Irma.")
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #0369a1; font-size: 0.85em; font-weight: bold;'>Created with pure sincerity for Irma Kristiani Ginting's Birthday 🎂💙</p>", unsafe_allow_html=True)
