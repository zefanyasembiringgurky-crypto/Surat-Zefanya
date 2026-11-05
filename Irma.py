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

# Custom CSS & Tema Birthday (Pastel Pink & Gold yang Elegan)
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        color: #2b2d42;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: #7209b7;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 2.6em;
        padding-top: 10px;
        text-shadow: 0 2px 10px rgba(255,255,255,0.8);
    }
    .subtitle {
        text-align: center;
        color: #3a0ca3;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: 800;
        font-size: 1.2em;
    }
    .love-card {
        background: #ffffff !important;
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.15);
        border: 3px solid #f72585;
        text-align: center;
        margin-bottom: 24px;
        color: #111111 !important;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: #7209b7 !important;
        font-weight: 900 !important;
    }
    .love-card h4 {
        color: #3a0ca3 !important;
        font-weight: 800 !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #2b2d42 !important;
        font-weight: 700 !important;
        font-size: 1.1em;
    }
    .message-box {
        background-color: #f8f9fa;
        border: 2px solid #f72585;
        border-radius: 12px;
        padding: 18px;
        margin-top: 12px;
        margin-bottom: 12px;
        text-align: left;
        color: #2b2d42 !important;
        font-size: 1.1em;
        font-weight: 700;
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid #7209b7 !important;
        border-radius: 10px !important;
    }
    .img-frame {
        background: #ffffff;
        padding: 12px;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(247, 37, 133, 0.2);
        border: 4px solid #f72585;
        margin-bottom: 15px;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid #7209b7 !important;
    }
    div.stButton > button {
        background: #7209b7;
        color: #ffffff !important;
        border-radius: 14px;
        font-weight: 800;
        font-size: 17px;
        padding: 14px 26px;
        border: 2px solid #ffffff;
        box-shadow: 0 6px 18px rgba(114, 9, 183, 0.3);
        width: 100%;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background: #f72585;
        opacity: 0.95;
        border-color: #ffd700;
    }
    @keyframes floatDown {
        0% { transform: translateY(-10vh) scale(1) rotate(0deg); opacity: 0; }
        15% { opacity: 0.95; }
        85% { opacity: 0.95; }
        100% { transform: translateY(105vh) scale(1.25) rotate(360deg); opacity: 0; }
    }
    .floating-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        overflow: hidden; pointer-events: none; z-index: 1;
    }
    .floating-item {
        position: absolute; top: -60px;
        font-size: 32px; font-weight: 900;
        color: #7209b7;
        text-shadow: 0 2px 5px rgba(255, 255, 255, 0.9);
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
        <div class="floating-item" style="left: 80%; animation-duration: 10.5s; animation-delay: 0.5s;">✨</div>
        <div class="floating-item" style="left: 86%; animation-duration: 8s; animation-delay: 2.5s;">I</div>
        <div class="floating-item" style="left: 91%; animation-duration: 11.5s; animation-delay: 1.1s;">R</div>
        <div class="floating-item" style="left: 95%; animation-duration: 9s; animation-delay: 3.2s;">M</div>
        <div class="floating-item" style="left: 98%; animation-duration: 10.2s; animation-delay: 0.7s;">A</div>
    </div>
"""

st.markdown(css_template, unsafe_allow_html=True)

# 🎈 Balon Sambutan Ulang Tahun
if 'welcomed_irma' not in st.session_state:
    st.balloons()
    st.session_state['welcomed_irma'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Happy Birthday Irma Kristiani Ginting! 🎂✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Spesial Hari Ini — Wishing you all the happiness in the world! 💖</p>", unsafe_allow_html=True)

# --- 1. UCAPAN & SURAT SPESIAL ULANG TAHUN ---
st.markdown("<div class='love-card'><h3>💌 Pesan Spesial Hari Ini</h3>", unsafe_allow_html=True)
st.markdown("<h4>Selamat Ulang Tahun, Irma! 🥳</h4>", unsafe_allow_html=True)
st.markdown("""
    <div class='message-box'>
    Halo Irma Kristiani Ginting! 🌟<br><br>
    Selamat bertambah usia ya! Semoga di umur yang baru ini, segala hal baik, kebahagiaan, kesehatan, dan kelancaran selalu menyertai setiap langkahmu. Semoga hari-harimu ke depan dipenuhi senyuman, tawa, dan hal-hal indah yang pantas kamu dapatkan. 
    <br><br>
    Tetap jadi pribadi yang hebat dan menginspirasi ya! Enjoy your special day to the fullest! 🎂✨🥂
    </div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 2. FOTO SPESIAL IRMA ---
st.markdown("<div class='love-card'><h3>📸 Spesial Untukmu Hari Ini</h3>", unsafe_allow_html=True)

# Cek apakah foto sudah diupload di GitHub
if os.path.exists("foto_irma.jpeg"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; color: #7209b7; font-style: italic;">"Satu foto, sejuta makna. Doa terbaik selalu menyertai setiap langkah dan senyumanmu!" ✨</p>', unsafe_allow_html=True)
elif os.path.exists("foto_irma.jpg"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; color: #7209b7; font-style: italic;">"Satu foto, sejuta makna. Doa terbaik selalu menyertai setiap langkah dan senyumanmu!" ✨</p>', unsafe_allow_html=True)
elif os.path.exists("foto_irma.png"):
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image("foto_irma.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; color: #7209b7; font-style: italic;">"Satu foto, sejuta makna. Doa terbaik selalu menyertai setiap langkah dan senyumanmu!" ✨</p>', unsafe_allow_html=True)
else:
    st.info("💡 Zefanya: File foto belum ditemukan. Jangan lupa upload foto Irma dengan nama 'foto_irma.jpeg' atau 'foto_irma.jpg' di repositori GitHub kamu ya!")

st.markdown("</div>", unsafe_allow_html=True)

# --- 3. KOTAK KADO KEJUTAN INTERAKTIF ---
st.markdown("<div class='love-card'><h3>🎁 Kotak Kado Kejutan</h3><p>Ssst... Ada kejutan kecil di dalam kado ini buat kamu. Coba klik tombol di bawah:</p>", unsafe_allow_html=True)

if 'open_gift' not in st.session_state:
    st.session_state['open_gift'] = False

if not st.session_state['open_gift']:
    if st.button("🎁 Buka Kado Spesial Ini"):
        with st.spinner("Membuka kado penuh doa dan kejutan..."):
            time.sleep(1.2)
        st.session_state['open_gift'] = True
        st.rerun()
else:
    st.balloons()
    st.markdown("""
        <div style="background: linear-gradient(135deg, #f72585 0%, #7209b7 100%); padding: 22px; border-radius: 16px; color: #ffffff; text-align: center; box-shadow: 0 8px 25px rgba(114,9,183,0.3);">
            <h2 style="margin-bottom: 10px; color: #ffd700;">🎉 SURPRISE! 🎉</h2>
            <p style="font-size: 1.2em; font-weight: 700; color: #ffffff !important; line-height: 1.6;">
                "Semoga traktirannya lancar dan semua impian besarmu tercapai tahun ini ya, Irma! Kalau butuh teman cerita atau bantuan apa pun, semesta selalu punya cara baik buat mempertemukan orang baik. Have a wonderful birthday!" 🤍✨
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- 4. SOUNDTRACK ULANG TAHUN (LINK RESMI MARANATHA SINGER) ---
url_lagu_irma = "https://www.youtube.com/watch?v=4oxarzdbEuw" 

st.markdown("<div class='love-card'><h3>🎵 Soundtrack Ulang Tahun</h3><p>Lagu pilihan penuh doa untuk menemani hari bahagiamu:</p>", unsafe_allow_html=True)
st.markdown("**♪ Happy Birthday Tuhan Berkati — Maranatha Singer**")
st.video(url_lagu_irma)

st.markdown(f"""
    <a href="{url_lagu_irma}" target="_blank">
        <button style="margin-top: 10px; width: 100%; background: #ff0000; color: white; padding: 10px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">
            ▶️ Klik di Sini Jika Video di Atas Tidak Bisa Diputar (Buka YouTube Langsung)
        </button>
    </a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 5. KOTAK UCAPAN / BALASAN DARI IRMA ---
st.markdown("<div class='love-card'><h3>✍️ Tinggalkan Balasan / Doa</h3><p>Ketik kesan atau pesan balasanmu di sini (pesannya bakal langsung masuk ke sistem Zefanya):</p>", unsafe_allow_html=True)
pesan_irma = st.text_area("Tulis pesan atau ucapan terima kasih di sini...")
if st.button("Kirim Pesan ke Zefanya"):
    if pesan_irma.strip():
        save_response("Pesan Ulang Tahun Irma", pesan_irma)
        st.success("Yeay! Pesan dan ucapanmu sudah berhasil tersimpan dengan manis! 🤍✨")
        st.balloons()
    else:
        st.warning("Tulis dulu pesannya ya, Irma.")
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. KONFIRMASI WHATSAPP ---
st.markdown("<div class='love-card'><h3>✅ Kabari Zefanya</h3><p>Udah buka kejutannya? Klik tombol di bawah buat kirim konfirmasi ke WhatsApp Zefanya:</p>", unsafe_allow_html=True)
nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, makasih banyak ya buat kejutan website ulang tahunnya dan lagunya yang indah! 🎉✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width: 100%; background-color: #25D366; color: white; padding: 14px 20px; border: none; border-radius: 12px; font-weight: 800; font-size: 17px; cursor: pointer;">
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
st.markdown("<p style='text-align: center; color: #3a0ca3; font-size: 0.9em; font-weight: bold;'>Created with pure sincerity for Irma Kristiani Ginting's Birthday 🎂✨</p>", unsafe_allow_html=True)
