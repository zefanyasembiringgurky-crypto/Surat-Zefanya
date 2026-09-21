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

# Pemetaan Tema Warna Mingguan Spesifik Anda
themes = {
    "Monday": {"bg": "#FFD166", "font": "#073B4C", "accent": "#FFFFFF", "nama_tema": "Summer Citrus"},
    "Tuesday": {"bg": "#06D6A0", "font": "#1D3557", "accent": "#F1FAEE", "nama_tema": "Minty Fresh"},
    "Wednesday": {"bg": "#FFFFFF", "font": "#118AB2", "accent": "#EF476F", "nama_tema": "Electric Neon"},
    "Thursday": {"bg": "#4EA8DE", "font": "#560BAD", "accent": "#F4E285", "nama_tema": "Ocean Breeze"},
    "Friday": {"bg": "#FFB703", "font": "#241400", "accent": "#FEFAE0", "nama_tema": "Peach Blossom"},
    "Saturday": {"bg": "#FFADAD", "font": "#4A0E4E", "accent": "#CAFFBF", "nama_tema": "Pastel Pop"},
    "Sunday": {"bg": "#B5E2FA", "font": "#3A0CA3", "accent": "#F72585", "nama_tema": "Lavender Dream"}
}

current_theme = themes.get(hari_ini_inggris, themes["Monday"])
current_bg = current_theme["bg"]
current_font = current_theme["font"]

# Cek Night-Mode Otomatis (Jika di atas jam 18:00)
if current_hour >= 18:
    current_bg = "#0f2027"
    current_font = "#FFFFFF"

# Custom CSS & Styling (Teks hitam pekat & jelas dibaca)
css_style = """
    <style>
    .stApp {
        background: """ + current_bg + """;
        color: """ + current_font + """;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: """ + current_font + """;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 2.8em;
        padding-top: 10px;
        text-shadow: 0 2px 8px rgba(255,255,255,0.6);
    }
    .subtitle {
        text-align: center;
        color: """ + current_font + """;
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
        border: 3px solid """ + current_font + """;
        text-align: center;
        margin-bottom: 24px;
        color: #111111 !important;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: """ + current_font + """ !important;
        font-weight: 900 !important;
    }
    .love-card h4 {
        color: """ + current_font + """ !important;
        font-weight: 800 !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #111111 !important;
        font-weight: 700 !important;
        font-size: 1.1em;
    }
    
    /* --- KOTAK PESAN HARIAN DENGAN TEKS HITAM PEKAT --- */
    .message-box {
        background-color: #ffffff;
        border: 2px solid """ + current_font + """;
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

    /* --- INPUT & TEXT AREA --- */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid """ + current_font + """ !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111111 !important;
        font-weight: 700 !important;
        border: 2px solid """ + current_font + """ !important;
    }

    /* --- BINGKAI FOTO --- */
    .img-frame {
        background: #ffffff;
        padding: 10px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.2);
        border: 4px solid """ + current_font + """;
    }

    /* --- TOMBOL --- */
    div.stButton > button {
        background: """ + current_font + """;
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

    /* --- ANIMASI HURUF, BUNGA PINK, BALON & KUPU-KUPU --- */
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
        color: """ + current_font + """;
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.95);
        animation: floatDown 10s infinite linear;
    }
    </style>

    <!-- Animasi Latar Belakang -->
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

st.markdown(css_style, unsafe_allow_html=True)

# Easter Egg Title Script
st.markdown("""
    <script>
    let docTitle = document.title;
    window.addEventListener("blur", () => {
        document.title = "🥺 Ih kok ditinggal sih? Kangen ya? Balik sini dong!";
    });
    window.addEventListener("focus", () => {
        document.title = docTitle;
    });
    </script>
""", unsafe_allow_html=True)

# 🎈 Sambutan Balon Pertama Kali Masuk
if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state['welcomed'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Tema Hari Ini: {current_theme['nama_tema']} — Update per {today.strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# --- JADWAL MINGGUAN ---
start_of_week = today - datetime.timedelta(days=today.weekday())

weekly_schedule = {
    0: { 
        "nama": "Senin", "tanggal": start_of_week + datetime.timedelta(days=0),
        "tema": "💼 Edisi Senin: Pawang Kerja Anti-Mager",
        "pesan": "Selamat hari Senin, pawang kerjaku! 🦖✨ Semangat ya kerjanya hari ini! Ingat, kalau kerjaan bikin pusing, tarik napas dalam-dalam dan ingat dompetmu butuh asupan saldo sehat. Senyum dong biar monitor kantor silau sama cantiknya kamu! 🤍💪",
        "foto": "foto_senin.jpeg", "fitur_spesial": "weather_note"
    },
    1: { 
        "nama": "Selasa", "tanggal": start_of_week + datetime.timedelta(days=1),
        "tema": "🌿 Edisi Selasa: Waktunya Me-Time & Santai",
        "pesan": "Selamat hari Selasa! Waktunya menikmati hari dengan rileks dan santai. Jangan terlalu diforsir kerjanya ya jagoanku! ✨",
        "foto": "foto_selasa.jpeg", "fitur_spesial": "fake_error"
    },
    2: { 
        "nama": "Rabu", "tanggal": start_of_week + datetime.timedelta(days=2),
        "tema": "✨ Edisi Rabu: Mid-Week Hug (Setengah Perjalanan)",
        "pesan": "Udah hari Rabu nih! Nggak terasa udah setengah jalan menuju weekend. Tetap semangat ya bidadari Berastagi! Kerjaan sebanyak apapun pasti kelar kalau dikerjakan pakai senyuman manismu. 🫂🤍",
        "foto": "foto_rabu.jpeg", "fitur_spesial": "mood_tracker"
    },
    3: { 
        "nama": "Kamis", "tanggal": start_of_week + datetime.timedelta(days=3),
        "tema": "🌸 Edisi Kamis: Kamisan Manis Menuju Weekend",
        "pesan": "Selamat hari Kamis! Sikit lagi mau weekend, tahan dikit lagi ya! Tetap fokus, jaga kesehatan, dan ingat ada aku yang selalu dukung kamu dari jauh. Semangat pejuang rupiah! 🤍",
        "foto": "foto_kamis.jpeg", "fitur_spesial": "snap_challenge"
    },
    4: { 
        "nama": "Jumat", "tanggal": start_of_week + datetime.timedelta(days=4),
        "tema": "🥳 Edisi Jumat: Jumat Berkah & Bau-bau Weekend",
        "pesan": "Yeay, Jumat berkah! Hari terakhir kerja sebelum weekend. Selesaikan sisa tugasmu dengan senyuman paling cerah ya! Sebentar lagi mau santai-santai. Pokoknya hari ini harus happy! 🤍",
        "foto": "foto_jumat.jpeg", "fitur_spesial": "spam_notification"
    },
    5: { 
        "nama": "Sabtu", "tanggal": start_of_week + datetime.timedelta(days=5),
        "tema": "☕ Edisi Sabtu: Secangkir Kopi & Senyumanmu",
        "pesan": "Selamat hari Sabtu, kesayanganku! ☕ Jangan lupa sarapan yang enak ya, biar energinya full. Kalau ada yang nyebelin, senyumin aja karena cantiknya kamu nggak ada tandingan. Semangat! 🤍",
        "foto": "foto_sabtu.jpeg", "fitur_spesial": "running_button"
    },
    6: { 
        "nama": "Minggu", "tanggal": start_of_week + datetime.timedelta(days=6),
        "tema": "☕ Edisi Minggu: Sweet & Lazy Sunday",
        "pesan": "Selamat hari Minggu! Waktunya istirahat total, santai secukupnya, dan siapin mood buat menyambut minggu baru. Have a wonderful Sunday, kesayangan! 🤍☕",
        "foto": "foto_minggu.jpeg", "fitur_spesial": "secret_inbox"
    }
}

current_data = weekly_schedule.get(today.weekday(), weekly_schedule[0])

# 📬 1. SURAT HARI INI (DENGAN KOTAK HTML KONTRAS TINGGI)
st.markdown(f"<div class='love-card'><h3>📬 Surat Hari Ini ({current_data['nama']}, {current_data['tanggal'].strftime('%d %b %Y')})</h3>", unsafe_allow_html=True)
st.markdown(f"<h4>{current_data['tema']}</h4>", unsafe_allow_html=True)
st.markdown(f"<div class='message-box'>{current_data['pesan']}</div>", unsafe_allow_html=True)

if current_data["fitur_spesial"] == "fake_error":
    st.error("⚠️ **SYSTEM ALERT:** Koneksi dari Berastagi terdeteksi terlalu menawan. Sistem hampir *crash* karena kepenuhan rasa rindu!")
elif current_data["fitur_spesial"] == "mood_tracker":
    st.markdown("---")
    st.markdown("💖 **Mood Tracker Hari Ini:**")
    m_pilih = st.selectbox("Gimana suasana hatimu hari ini?", ["Pilih mood...", "Semangat 45 🔥", "Lelah tapi tetap cantik 🌸", "Butuh boba & pelukan 🧋", "Happy pol! ✨"])
    if st.button("Simpan Moodku"):
        save_response("Mood Harian Rabu", m_pilih)
        st.success("Mood gemasmu berhasil dicatat di sistem Zefanya! 🤍")
elif current_data["fitur_spesial"] == "running_button":
    st.markdown("---")
    st.markdown("🎯 **Tantangan Hari Ini:** Coba klik tombol di bawah kalau berani:")
    if st.button("❌ Jangan Klik Tombol Ini!"):
        st.balloons()
        st.success("Hahaha ketahuan kan penasaran! Mana bisa menolak pesona Zefanya? 😉🤍")

st.markdown("</div>", unsafe_allow_html=True)

# 🎵 2. JUKEBOX 7 LAGU PILIHAN (DENGAN TOMBOL CADANGAN LANGSUNG KE YOUTUBE)
st.markdown("<div class='love-card'><h3>🎵 Jukebox Musik Kita (Hindia & .Feast)</h3><p>Pilih lagu favoritmu untuk menemani hari ini:</p>", unsafe_allow_html=True)

pilihan_lagu = st.selectbox("Pilih Daftar Lagu:", [
    "1. Secukupnya — Hindia",
    "2. Mata Air — Hindia",
    "3. Peradaban — .Feast",
    "4. Bayangkan Jika Kita Tidak Menyerah — Hindia",
    "5. Rumah ke Rumah — Hindia",
    "6. Cincin — Hindia",
    "7. Evaluasi — Hindia"
])

# Pemetaan ID Video YouTube Resmi yang Stabil
if "1." in pilihan_lagu:
    yt_id = "wnAKxtEi78c"
    yt_url = "https://www.youtube.com/watch?v=wnAKxtEi78c"
elif "2." in pilihan_lagu:
    yt_id = "i0aE3fHHitY"
    yt_url = "https://www.youtube.com/watch?v=i0aE3fHHitY"
elif "3." in pilihan_lagu:
    yt_id = "8c0IzngvGEw"
    yt_url = "https://www.youtube.com/watch?v=8c0IzngvGEw"
elif "4." in pilihan_lagu:
    yt_id = "5H3p96u8_8k"
    yt_url = "https://www.youtube.com/watch?v=5H3p96u8_8k"
elif "5." in pilihan_lagu:
    yt_id = "5H3p96u8_8k"
    yt_url = "https://www.youtube.com/watch?v=5H3p96u8_8k"
elif "6." in pilihan_lagu:
    yt_id = "2q8X93a9n6o"
    yt_url = "https://www.youtube.com/watch?v=2q8X93a9n6o"
else:
    yt_id = "2q8X93a9n6o"
    yt_url = "https://www.youtube.com/watch?v=2q8X93a9n6o"

# Pemutar Video Streamlit
st.video(yt_url)

# Tombol Cadangan Langsung ke YouTube jika embed diblokir
st.markdown(f"""
    <a href="{yt_url}" target="_blank">
        <button style="margin-top: 10px; width: 100%; background: #ff0000; color: white; padding: 10px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">
            ▶️ Klik di Sini Jika Video di Atas Diblokir (Buka YouTube Langsung)
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ⛰️ 3. FOTO UTAMA HARIAN
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

# ✨ 5. PENILAIAN KEBAHAGIAAN (BAHASA MEDAN)
st.markdown("<div class='love-card'><h3>💖 Seberapa Senang Kamu Baca Surat Ini?</h3>", unsafe_allow_html=True)
pilihan_senang = st.radio("Pilih ekspresi kamu sekarang:", [
    "Bahagia kalilah rasa a, serasa menang tender ganti rugi jalan tol! 🛞😂", 
    "Senyum-senyum sendiri aku nengoknya, kayak orang gila di Medan Mall! 🤪", 
    "Kalak karona (manis) kali suratnya, jadi rindu mau kuajak nge-teh manis berdua! ☕✨"
])

if st.button("💾 Simpan Perasaanku"):
    save_response("Tingkat Kebahagiaan", pilihan_senang)
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

# 🕰️ 7. KAPSUL WAKTU MINGGU INI (TIME-LOCK CALENDAR — POSISI PALING BAWAH SEBELUM PANEL)
st.markdown("<div class='love-card'><h3>🕰️ Kapsul Waktu Minggu Ini (Time-Lock Calendar)</h3><p>Hari yang sudah lewat bisa dibuka kembali. Hari depan otomatis terkunci rapi! 👇</p>", unsafe_allow_html=True)

for idx, data in weekly_schedule.items():
    tgl_surat = data["tanggal"]
    nama_hari = data["nama"]
    
    if tgl_surat <= today:
        with st.expander(f"📖 {nama_hari} ({tgl_surat.strftime('%d %b %Y')}) — 🔓 Terbuka"):
            st.markdown(f"**{data['tema']}**")
            st.write(data['pesan'])
            if os.path.exists(data["foto"]):
                st.image(data["foto"], width=250)
    else:
        with st.expander(f"🔒 {nama_hari} ({tgl_surat.strftime('%d %b %Y')}) — 🔒 Terkunci"):
            st.warning(f"Sabar ya sayang! Surat untuk hari **{nama_hari}** ini masih terkunci dan baru bisa dibuka tanggal **{tgl_surat.strftime('%d %B %Y')}**! 🤫🤍")

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
            
            # Grafik Riwayat Mood / Respons
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
