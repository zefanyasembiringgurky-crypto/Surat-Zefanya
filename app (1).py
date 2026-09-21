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

# --- SISTEM WAKTU & 3 WARNA CERAH GRADASI HARIAN ---
today = datetime.date.today()
current_hour = datetime.datetime.now().hour
hari_ini_inggris = today.strftime("%A")

# Pemetaan gradasi 3 warna cerah per hari agar kontras dan mencolok
bg_colors = {
    "Monday": "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 50%, #fbc2eb 100%)",     # Sky Blue - Pink Soft
    "Tuesday": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #ff9a9e 100%)",    # Peach - Warm Coral
    "Wednesday": "linear-gradient(135deg, #d4fc79 0%, #96e6a1 50%, #8fd3f4 100%)",  # Fresh Mint - Soft Blue
    "Thursday": "linear-gradient(135deg, #fbc531 0%, #e84118 50%, #f5cd79 100%)",   # Gold - Vibrant Sunset
    "Friday": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #a1c4fd 100%)",     # Pink Pastel - Sky
    "Saturday": "linear-gradient(135deg, #f6d365 0%, #fda085 50%, #fbc531 100%)",   # Sunny Orange - Yellow
    "Sunday": "linear-gradient(135deg, #84fab0 0%, #8fd3f4 50%, #a1c4fd 100%)"      # Mint - Cyan Blue
}
current_bg = bg_colors.get(hari_ini_inggris, "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 50%, #fbc2eb 100%)")

# Cek Night-Mode Otomatis (Jika di atas jam 18:00)
if current_hour >= 18:
    current_bg = "linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)"

# Custom CSS & Styling (Teks hitam pekat, card putih tebal, tombol jelas)
css_style = """
    <style>
    .stApp {
        background: """ + current_bg + """;
        color: #111111;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: #0b3c5d;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 2.8em;
        padding-top: 10px;
        text-shadow: 0 2px 8px rgba(255,255,255,0.9);
    }
    .subtitle {
        text-align: center;
        color: #1d2731;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: 700;
        font-size: 1.1em;
    }
    .love-card {
        background: rgba(255, 255, 255, 0.98);
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(6px);
        border: 3px solid rgba(11, 60, 93, 0.3);
        text-align: center;
        margin-bottom: 24px;
        color: #111111;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: #0b3c5d !important;
        font-weight: 800 !important;
    }
    .love-card h4 {
        color: #1d2731 !important;
        font-weight: 700 !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #111111 !important;
        font-weight: 700 !important;
        font-size: 1.05em;
    }
    
    /* --- BINGKAI FOTO ROMANTIS --- */
    .img-frame {
        background: #ffffff;
        padding: 10px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.2);
        border: 4px solid #0b3c5d;
    }

    /* --- TOMBOL KONTRAS TINGGI & JELAS --- */
    div.stButton > button {
        background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%);
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
        background: linear-gradient(135deg, #328cc1 0%, #1d2731 100%);
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
        color: rgba(11, 60, 93, 0.85);
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.95);
        animation: floatDown 10s infinite linear;
    }
    </style>

    <!-- Elemen Animasi Latar Belakang -->
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
st.markdown(f"<p class='subtitle'>Surat Harian & Kasih Sayang — Update per {today.strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

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

# 📬 1. SURAT HARI INI
st.markdown(f"<div class='love-card'><h3>📬 Surat Hari Ini ({current_data['nama']}, {current_data['tanggal'].strftime('%d %b %Y')})</h3>", unsafe_allow_html=True)
st.markdown(f"<h4>{current_data['tema']}</h4>", unsafe_allow_html=True)
st.info(f"> {current_data['pesan']}")

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

# 🎵 2. JUKEBOX SEMUA LAGU HINDIA & .F.E.A.S.T (BERLAKU DI SEMUA HARI, TEPAT SETELAH SURAT)
st.markdown("<div class='love-card'><h3>🎵 Jukebox Musik Kita (Hindia & .F.E.A.S.T)</h3><p>Pilih lagu favoritmu untuk menemani hari ini:</p>", unsafe_allow_html=True)

pilihan_lagu = st.selectbox("Pilih Daftar Lagu:", [
    "Secukupnya — Lagu kebangsaan bangkit dari penat & lelah bekerja",
    "Rumah ke Rumah — Perjalanan hidup & pendewasaan yang adiktif",
    "Evaluasi — Dorongan mental bertahan di hari yang berat",
    "Mata Air — Merayakan diri sendiri & mencintai diri apa adanya",
    "Basmi (feat. .F.E.A.S.T) — Lagu rock alternatif penuh energi berapi-api",
    "Peradaban (feat. .F.E.A.S.T) — Anthem perjuangan sosial yang membakar semangat",
    "Segala Bunga — Nuansa segar & asyik untuk tetap produktif",
    "Apapun yang Terjadi — Penguat diri menghadapi ketidakpastian masa depan"
])

# Embed YouTube URL yang aktif dan dijamin jalan
if "Secukupnya" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/J762g_t6-q4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Rumah ke Rumah" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/5H3p96u8_8k" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Evaluasi" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/2q8X93a9n6o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Mata Air" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/6k48i4tN4hM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Basmi" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/0x91p5u5a8g" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Peradaban" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/7X8652lK35o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Segala Bunga" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/DrulgpXAGCA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
else: # Apapun yang Terjadi
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/DrulgpXAGCA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)

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
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 10px; text-align: left;">
                <h4 style="color: #0b3c5d; margin-bottom: 8px;">Bidadari Berastagi Paling Bersinar... ✨</h4>
                <p style="color: #111111; font-size: 1.05em; line-height: 1.6; font-weight: 700;">
                Sejauh apapun jarak kita atau sibuknya hari ini, energiku langsung terisi lagi cuma karena bayangin senyuman kamu. Proud of you! 🤍
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto harian belum di-upload di GitHub (sediakan `foto_senin.jpeg`, dll atau `foto_dirimu.jpeg`).")
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
st.markdown("<p style='text-align: center; color: #111; font-size: 0.9em; font-weight: bold;'>Web ini online 24/7 buat kamu yang selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
