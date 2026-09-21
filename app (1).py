import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os
import random

# --- INISIALISASI DATABASE SQLITE ---
def init_db():
    conn = sqlite3.connect('jawaban_avrillia.db', check_same_thread=False)
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
    conn = sqlite3.connect('jawaban_avrillia.db', check_same_thread=False)
    c = conn.cursor()
    waktu_str = datetime.datetime.now().strftime("%d %B %Y - %H:%M:%S")
    c.execute('INSERT INTO responses (topik, jawaban, waktu) VALUES (?, ?, ?)', (topik, jawaban, waktu_str))
    conn.commit()
    conn.close()

def delete_response(resp_id):
    conn = sqlite3.connect('jawaban_avrillia.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('DELETE FROM responses WHERE id = ?', (resp_id,))
    conn.commit()
    conn.close()

def get_responses():
    conn = sqlite3.connect('jawaban_avrillia.db', check_same_thread=False)
    try:
        df_resp = pd.read_sql_query('SELECT * FROM responses ORDER BY id DESC', conn)
    except:
        df_resp = pd.DataFrame(columns=['id', 'topik', 'jawaban', 'waktu'])
    conn.close()
    return df_resp

# Konfigurasi Halaman
st.set_page_config(
    page_title="Surat Zefanya for Avrillia🤍", 
    page_icon="Avrillia💌", 
    layout="centered"
)

# --- SISTEM WAKTU & TEMA WARNA MINGGUAN SPESIFIK ---
today = datetime.date.today()
current_hour = datetime.datetime.now().hour
hari_ini_inggris = today.strftime("%A")

# Pemetaan Tema Warna Mingguan Spesifik
themes = {
    "Monday": {"bg": "#FFD166", "font": "#073B4C", "accent": "#FFFFFF", "nama_tema": "Summer Citrus"},
    "Tuesday": {"bg": "#06D6A0", "font": "#1D3557", "accent": "#F1FAEE", "nama_tema": "Minty Fresh"},
    "Wednesday": {"bg": "#FFFFFF", "font": "#118AB2", "accent": "#EF476F", "nama_tema": "Electric Neon"},
    "Thursday": {"bg": "#4EA8DE", "font": "#560BAD", "accent": "#F4E285", "nama_tema": "Ocean Breeze"},
    "Friday": {"bg": "#FFB703", "font": "#241400", "accent": "#FEFAE0", "nama_tema": "Peach Blossom"},
    "Saturday": {"bg": "#FFADAD", "font": "#4A0E4E", "accent": "#CAFFBF", "nama_tema": "Pastel Pop"},
    "Sunday": {"bg": "#B5E2FA", "font": "#3A0CA3", "accent": "#F72585", "nama_tema": "Lavender Dream"}
}

indo_to_eng = {
    "Senin": "Monday",
    "Selasa": "Tuesday",
    "Rabu": "Wednesday",
    "Kamis": "Thursday",
    "Jumat": "Friday",
    "Sabtu": "Saturday",
    "Minggu": "Sunday"
}

eng_to_indo = {v: k for k, v in indo_to_eng.items()}
default_indo = eng_to_indo.get(hari_ini_inggris, "Senin")

# --- FITUR PEMILIH HARI (UNTUK TESTING & EKSPLORASI PENUH) ---
st.markdown("<div style='background: rgba(255,255,255,0.85); padding: 12px; border-radius: 12px; margin-bottom: 20px; text-align: center;'>", unsafe_allow_html=True)
selected_hari_indo = st.selectbox("📅 Pilih Hari yang Ingin Ditampilkan:", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"], index=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"].index(default_indo))
st.markdown("</div>", unsafe_allow_html=True)

selected_hari_eng = indo_to_eng[selected_hari_indo]
current_theme = themes.get(selected_hari_eng, themes["Monday"])
current_bg = current_theme["bg"]
current_font = current_theme["font"]

# Cek Night-Mode Otomatis (Jika di atas jam 18:00 atau khusus Minggu malam)
if (current_hour >= 18 and selected_hari_eng == hari_ini_inggris) or (selected_hari_indo == "Minggu" and current_hour >= 18):
    current_bg = "#0f2027"
    current_font = "#FFFFFF"

# Custom CSS & Styling
css_template = """
    <style>
    .stApp {
        background: __BG__;
        color: __FONT__;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: __FONT__;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 2.8em;
        padding-top: 10px;
        text-shadow: 0 2px 8px rgba(255,255,255,0.6);
    }
    .subtitle {
        text-align: center;
        color: __FONT__;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: 800;
        font-size: 1.15em;
    }
    .love-card {
        background: #ffffff !important;
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.2);
        border: 3px solid __FONT__;
        text-align: center;
        margin-bottom: 24px;
        color: #111111 !important;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: __FONT__ !important;
        font-weight: 900 !important;
    }
    .love-card h4 {
        color: __FONT__ !important;
        font-weight: 800 !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #111111 !important;
        font-weight: 700 !important;
        font-size: 1.1em;
    }
    .message-box {
        background-color: #ffffff;
        border: 2px solid __FONT__;
        border-radius: 12px;
        padding: 18px;
        margin-top: 12px;
        margin-bottom: 12px;
        text-align: left;
        color: #111111 !important;
        font-size: 1.1em;
        font-weight: 700;
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid __FONT__ !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid __FONT__ !important;
    }
    .img-frame {
        background: #ffffff;
        padding: 10px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.2);
        border: 4px solid __FONT__;
    }
    div.stButton > button {
        background: __FONT__;
        color: #ffffff !important;
        border-radius: 14px;
        font-weight: 800;
        font-size: 17px;
        padding: 14px 26px;
        border: 2px solid #ffffff;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
        width: 100%;
        cursor: pointer;
    }
    div.stButton > button:hover {
        opacity: 0.9;
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
        font-size: 34px; font-weight: bold;
        color: __FONT__;
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.95);
        animation: floatDown 10s infinite linear;
    }
    </style>
    <div class="floating-bg">
        <div class="floating-item" style="left: 4%; animation-duration: 9s; animation-delay: 0s;">A</div>
        <div class="floating-item" style="left: 12%; animation-duration: 11s; animation-delay: 2s;">🌸</div>
        <div class="floating-item" style="left: 20%; animation-duration: 8s; animation-delay: 1s;">V</div>
        <div class="floating-item" style="left: 30%; animation-duration: 12s; animation-delay: 3s;">🦋</div>
        <div class="floating-item" style="left: 40%; animation-duration: 9.5s; animation-delay: 0.5s;">R</div>
        <div class="floating-item" style="left: 50%; animation-duration: 10.5s; animation-delay: 2.5s;">🌸</div>
        <div class="floating-item" style="left: 60%; animation-duration: 11.5s; animation-delay: 1.5s;">I</div>
        <div class="floating-item" style="left: 70%; animation-duration: 8.5s; animation-delay: 3.5s;">🎈</div>
        <div class="floating-item" style="left: 80%; animation-duration: 10s; animation-delay: 0.8s;">L</div>
        <div class="floating-item" style="left: 88%; animation-duration: 9s; animation-delay: 2.2s;">I</div>
        <div class="floating-item" style="left: 95%; animation-duration: 10s; animation-delay: 1.2s;">A</div>
    </div>
"""

css_style = css_template.replace("__BG__", current_bg).replace("__FONT__", current_font)
st.markdown(css_style, unsafe_allow_html=True)

# 🎈 Sambutan Balon Pertama Kali Masuk
if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state['welcomed'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Tema Hari Ini: {current_theme['nama_tema']} ({selected_hari_indo})</p>", unsafe_allow_html=True)

# --- DATA JADWAL HARI & KEJUTAN PILIHAN ---
weekly_schedule = {
    "Senin": { 
        "tema": "💼 Edisi Senin: Pawang Kerja Anti-Mager",
        "pesan": "Selamat hari Senin, Avrillia! 🦖✨ Semangat ya kerjanya hari ini! Ingat, kalau kerjaan bikin pusing, tarik napas dalam-dalam dan ingat dompetmu butuh asupan saldo sehat. Senyum dong biar monitor kantor silau sama cantiknya kamu! 🤍💪",
        "foto": "foto_senin.jpeg", "fitur_spesial": "weather_note",
        "lagu_judul": "Secukupnya — Hindia", "lagu_url": "https://www.youtube.com/watch?v=wnAKxtEi78c"
    },
    "Selasa": { 
        "tema": "🌿 Edisi Selasa: Waktunya Me-Time & Santai",
        "pesan": "Selamat hari Selasa! Waktunya menikmati hari dengan rileks dan santai. Jangan terlalu diforsir kerjanya ya Avrillia! ✨",
        "foto": "foto_selasa.jpeg", "fitur_spesial": "fake_error",
        "lagu_judul": "Mata Air — Hindia", "lagu_url": "https://www.youtube.com/watch?v=i0aE3fHHitY"
    },
    "Rabu": { 
        "tema": "✨ Edisi Rabu: Mid-Week Hug (Setengah Perjalanan)",
        "pesan": "Udah hari Rabu nih! Nggak terasa udah setengah jalan menuju weekend. Tetap semangat ya bidadari Berastagi! Kerjaan sebanyak apapun pasti kelar kalau dikerjakan pakai senyuman manismu. 🫂🤍",
        "foto": "foto_rabu.jpeg", "fitur_spesial": "mood_tracker",
        "lagu_judul": "Peradaban — .Feast", "lagu_url": "https://www.youtube.com/watch?v=8c0IzngvGEw"
    },
    "Kamis": { 
        "tema": "🌸 Edisi Kamis: Kamisan Manis Menuju Weekend",
        "pesan": "Selamat hari Kamis! Sikit lagi mau weekend, tahan dikit lagi ya! Tetap fokus, jaga kesehatan, dan ingat ada aku yang selalu dukung kamu dari jauh. Semangat pejuang rupiah! 🤍",
        "foto": "foto_kamis.jpeg", "fitur_spesial": "snap_challenge",
        "lagu_judul": "Bayangkan Jika Kita Tidak Menyerah — Hindia", "lagu_url": "https://www.youtube.com/watch?v=rSTO0VrV38Y"
    },
    "Jumat": { 
        "tema": "🥳 Edisi Jumat: Jumat Berkah & Bau-bau Weekend",
        "pesan": "Yeay, Jumat berkah! Hari terakhir kerja sebelum weekend. Selesaikan sisa tugasmu dengan senyuman paling cerah ya! Sebentar lagi mau santai-santai. Pokoknya hari ini harus happy! 🤍",
        "foto": "foto_jumat.jpeg", "fitur_spesial": "spam_notification",
        "lagu_judul": "Rumah ke Rumah — Hindia", "lagu_url": "https://www.youtube.com/watch?v=pjhOjHDX0A8"
    },
    "Sabtu": { 
        "tema": "☕ Edisi Sabtu: Secangkir Kopi & Senyumanmu",
        "pesan": "Selamat hari Sabtu, Avrillia! ☕ Jangan lupa sarapan yang enak ya, biar energinya full. Hati-hati dalam perjalanan dari Berastagi ke Medan ya sayang, semoga lancar dan selamat sampai tujuan! 🚗✨",
        "foto": "foto_sabtu.jpeg", "fitur_spesial": "running_button",
        "lagu_judul": "Peradaban — .Feast", "lagu_url": "https://www.youtube.com/watch?v=qf1W5iIRTe8"
    },
    "Minggu": { 
        "tema": "☕ Edisi Minggu: Sweet & Lazy Sunday",
        "pesan": "Selamat hari Minggu! Waktunya istirahat total, santai secukupnya. Hati-hati dalam perjalanan kembali dari Medan ke Berastagi, selamat berlibur dan nikmati waktunya ya, kesayangan! 🌴🤍",
        "foto": "foto_minggu.jpeg", "fitur_spesial": "secret_inbox",
        "lagu_judul": "Evaluasi — Hindia", "lagu_url": "https://www.youtube.com/watch?v=cWrSjCZ5AeE"
    }
}

current_data = weekly_schedule[selected_hari_indo]

# 📬 1. SURAT HARI INI
st.markdown(f"<div class='love-card'><h3>📬 Surat Hari Ini ({selected_hari_indo})</h3>", unsafe_allow_html=True)
st.markdown(f"<h4>{current_data['tema']}</h4>", unsafe_allow_html=True)
st.markdown(f"<div class='message-box'>{current_data['pesan']}</div>", unsafe_allow_html=True)

# FITUR SPESIFIK BERDASARKAN HARI (SELASA DENGAN DETEKSI BOM ZEFANYA)
if current_data["fitur_spesial"] == "fake_error":
    if 'bomb_triggered' not in st.session_state:
        st.session_state['bomb_triggered'] = False

    if not st.session_state['bomb_triggered']:
        st.markdown("""
            <div style="background: #fff3cd; padding: 16px; border-radius: 12px; border-left: 6px solid #ffc107; text-align: center; margin-bottom: 15px;">
                <p style="color: #856404; font-weight: bold; margin-bottom: 12px; font-size: 1.1em;">
                    ⚠️ PERINGATAN SISTEM: Terdeteksi Bom Rindu berkedip di sistem! Jangan panik...
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("💣 DETEKSI BOM ZEFANYA"):
            st.session_state['bomb_triggered'] = True
            st.rerun()
    else:
        st.balloons()
        st.markdown("""
            <div style="background: #ffe6e6; padding: 18px; border-radius: 14px; border: 2px solid #ff4d4d; text-align: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(255,77,77,0.2);">
                <h3 style="color: #d90429; margin-bottom: 8px;">💥 BOOOM! Hayo kaget yaaa! 😜</h3>
                <p style="color: #111111; font-weight: 700; font-size: 1.1em; line-height: 1.5;">
                    Hahaha, tenang aja! Itu bukan bom beneran kok, tapi <b>Bom Kangen</b> dari Zefanya yang siap meledakkan senyuman di wajah cantikmu hari ini! 💣🤍✨
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Desain Piagam Sertifikat Resmi Klasik
        st.markdown("""
            <div style="background: #ffffff; border: 5px double #1D3557; padding: 25px; border-radius: 15px; text-align: center; position: relative; box-shadow: 0 8px 25px rgba(0,0,0,0.15); margin-top: 15px; margin-bottom: 15px;">
                <div style="position: absolute; top: 15px; right: 20px; background: #e63946; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold; transform: rotate(8deg);">
                    Approved by Zefanya 🏆
                </div>
                <h3 style="color: #1D3557; font-family: 'Georgia', serif; margin-bottom: 5px; font-size: 1.4em;">📜 SERTIFIKAT RESMI PAWANG 📜</h3>
                <p style="color: #6c757d; font-size: 0.9em; font-style: italic; margin-bottom: 15px;">Diberikan dengan penuh rasa rindu dan bangga</p>
                <hr style="border: 1px solid #dee2e6; width: 80%; margin: 0 auto 15px auto;">
                <p style="color: #111111; font-size: 1.1em; font-weight: 700; line-height: 1.5;">
                    Sertifikat kehormatan ini diberikan kepada:<br>
                    <span style="color: #e63946; font-size: 1.3em; font-family: 'Georgia', serif;">Avrillia 🤍</span><br>
                    Sebagai <b>Pawang Kerja Anti-Mager Paling Hebat se-Sumatera Utara!</b>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏆 Klaim Gelar Pawang Sekarang"):
            st.balloons()
            st.markdown("""
                <div style="background-color: #2b9348; padding: 14px; border-radius: 12px; color: #ffffff !important; font-weight: bold; text-align: center; margin-top: 12px; font-size: 1.1em; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                    Yeay! Gelar Pawang Resmi Diklaim! Kamu memang yang terbaik! ✨
                </div>
            """, unsafe_allow_html=True)

elif current_data["fitur_spesial"] == "mood_tracker":
    st.markdown("---")
    st.markdown("💖 **Mood Tracker Hari Ini:**")
    m_pilih = st.selectbox("Gimana suasana hatimu hari ini?", ["Pilih mood...", "Semangat 45 🔥", "Lelah tapi tetap cantik 🌸", "Butuh boba & pelukan 🧋", "Happy pol! ✨"])
    if st.button("Simpan Moodku"):
        save_response("Mood Harian Rabu", m_pilih)
        st.success("Mood gemasmu berhasil dicatat di sistem Zefanya! 🤍")
elif current_data["fitur_spesial"] == "snap_challenge":
    st.markdown("---")
    st.info("🌤️ **Asisten Cuaca Berastagi:** Suhu dingin paling pas ditemenin senyuman manis kamu hari ini. Jangan lupa pakai jaket ya!")
elif current_data["fitur_spesial"] == "spam_notification":
    st.warning("🚨 **BREAKING NEWS RINDU:** Terdeteksi tingkat kangen tingkat tinggi di udara. Harap segera tersenyum agar sistem kembali stabil!")
elif current_data["fitur_spesial"] == "running_button":
    st.markdown("---")
    st.markdown("🎯 **Tantangan Hari Sabtu:** Coba klik tombol di bawah kalau berani:")
    if st.button("❌ Jangan Klik Tombol Ini!"):
        st.balloons()
        st.success("Hahaha ketahuan kan penasaran! Mana bisa menolak pesona Zefanya? 😉🤍 Hati-hati di jalan ya menuju Medan!")

st.markdown("</div>", unsafe_allow_html=True)

# 🎵 2. LAGU SPESIAL HARI INI
st.markdown(f"<div class='love-card'><h3>🎵 Soundtrack Hari Ini</h3><p>Lagu pilihan spesial buat menemani hari {selected_hari_indo}:</p>", unsafe_allow_html=True)
st.markdown(f"**♪ {current_data['lagu_judul']}**")

st.video(current_data['lagu_url'])

st.markdown(f"""
    <a href="{current_data['lagu_url']}" target="_blank">
        <button style="margin-top: 10px; width: 100%; background: #ff0000; color: white; padding: 10px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">
            ▶️ Klik di Sini Jika Video di Atas Diblokir (Buka YouTube Langsung)
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ⛰️ 3. FOTO UTAMA HARIAN (KHUSUS HARI SENIN)
if selected_hari_indo == "Senin":
    st.markdown("<div class='love-card'><h3>⛰️ Pesan & Foto Spesial Berastagi</h3>", unsafe_allow_html=True)
    target_foto = current_data["foto"]
    if os.path.exists(target_foto):
        img_path_1 = target_foto
    elif os.path.exists("foto_dirimu.jpeg"):
        img_path_1 = "foto_dirimu.jpeg"
    elif os.path.exists("foto_dirimu.jpg"):
        img_path_1 = "foto_dirimu.jpg"
    else:
        img_path_1 = None

    if img_path_1:
        col_img1, col_txt1 = st.columns([1, 1], gap="medium")
        with col_img1:
            st.markdown('<div class="img-frame">', unsafe_allow_html=True)
            st.image(img_path_1, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col_txt1:
            st.markdown(f"""
                <div style="display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 10px; text-align: left;">
                    <h4 style="color: {current_font}; margin-bottom: 8px;">Bidadari Berastagi Paling Bersinar... ✨</h4>
                    <p style="color: #111111; font-size: 1.05em; line-height: 1.6; font-weight: 700;">
                    Sejauh apapun jarak kita atau sibuknya hari ini, energiku langsung terisi lagi cuma karena bayangin senyuman kamu. Proud of you! 🤍
                    </p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ File foto harian belum di-upload di GitHub.")
    st.markdown("</div>", unsafe_allow_html=True)

# 📥 4. KOTAK CURHAT (SECRET INBOX)
st.markdown("<div class='love-card'><h3>📥 Kotak Curhat Rahasia</h3><p>Ada uneg-uneg atau capek hari ini? Ketik di sini, pesannya langsung masuk ke Panel Zefanya:</p>", unsafe_allow_html=True)
curhat_input = st.text_area("Tulis ceritamu di sini...")
if st.button("Kirim ke Zefanya"):
    if curhat_input.strip():
        save_response("Kotak Curhat Rahasia", curhat_input)
        st.success("Curhatanmu sudah sampai di hati (dan panel) Zefanya! 🤍")
    else:
        st.warning("Tulis dulu pesannya ya.")
st.markdown("</div>", unsafe_allow_html=True)

# ✨ 5. PENILAIAN KEBAHAGIAAN (2 PILIHAN UNIK ACAK PER HARI)
expression_options_by_day = {
    "Senin": ["sikik aaaa", "happy"],
    "Selasa": ["happyyy", "happyy bgttttttttt"],
    "Rabu": ["makasih banyakkkk", "hapyy bgttt lohhh aku, terharu"],
    "Kamis": ["AAAAAAAAAAAAA", "Jadi tambah semangat kerja dehhhhh"],
    "Jumat": ["penghilang rasa ngantukkuuuu", "semangat yaa buat temanyaaaaa, aku selalu menungguu"],
    "Sabtu": ["asikkkkkkkkkkk", "asik"],
    "Minggu": ["setress si tapi ada ini ga setres lagii", "happyyy"]
}

current_expressions = expression_options_by_day.get(selected_hari_indo, ["happy", "asik"])

st.markdown(f"<div class='love-card'><h3>💖 Ekspresi {selected_hari_indo}</h3>", unsafe_allow_html=True)
pilihan_senang = st.radio("Pilih ekspresi kamu sekarang:", current_expressions)

if st.button("💾 Simpan Perasaanku"):
    save_response(f"Ekspresi {selected_hari_indo}", pilihan_senang)
    st.success("Mantap kali! Jawabannya udah sukses masuk ke Panel Zefanya 🤍")
    st.balloons()
st.markdown("</div>", unsafe_allow_html=True)

# 📲 6. LAPOR WHATSAPP
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca? Klik tombol di bawah buat kirim kabar ke WhatsApp aku ya:</p>", unsafe_allow_html=True)
nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web surat harian nih! 🤍✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width: 100%; background-color: #25D366; color: white; padding: 14px 20px; border: none; border-radius: 12px; font-weight: 800; font-size: 17px; cursor: pointer;">
            📲 Klik di Sini Kalau Udah Dibaca (Lapor WA)
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
            st.markdown("📊 **Grafik Riwayat Aktivitas/Mood Avrillia:**")
            mood_counts = df_data['topik'].value_counts()
            st.bar_chart(mood_counts)
            
            st.markdown("---")
            st.markdown("🗑️ **Hapus Jawaban:**")
            id_to_delete = st.number_input("Masukkan Nomor ID:", min_value=1, step=1)
            if st.button("❌ Hapus Jawaban Ini"):
                if id_to_delete in df_data['id'].values:
                    delete_response(id_to_delete)
                    st.success(f"ID {id_to_delete} berhasil dihapus!")
                    st.rerun()
                else:
                    st.error("ID tidak ditemukan.")
        else:
            st.info("Belum ada data respons tersimpan.")
    elif pin_input:
        st.error("PIN salah.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: {current_font}; font-size: 0.9em; font-weight: bold;'>Web ini online 24/7 buat kamu yang selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
