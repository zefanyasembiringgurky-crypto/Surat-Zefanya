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

# --- SISTEM WAKTU & WARNA BACKGROUND HARIAN ---
today = datetime.date.today()
current_hour = datetime.datetime.now().hour
hari_ini_inggris = today.strftime("%A")

# Pemetaan warna background cerah harian
bg_colors = {
    "Monday": "linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",     # Sky Blue
    "Tuesday": "linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",    # Sunny Peach
    "Wednesday": "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",  # Fresh Mint
    "Thursday": "linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",   # Soft Lavender
    "Friday": "linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",     # Sunset Coral
    "Saturday": "linear-gradient(135deg, #fffde7 0%, #fff9c4 100%)",   # Golden Sun
    "Sunday": "linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%)"      # Pastel Cyan
}
current_bg = bg_colors.get(hari_ini_inggris, "linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)")

# Cek Night-Mode Otomatis (Jika di atas jam 18:00)
if current_hour >= 18:
    current_bg = "linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)"

# Custom CSS & Styling (Menggunakan format() untuk mengelakkan ralat f-string brace)
css_template = """
    <style>
    .stApp {{
        background: {bg_val};
        color: #1a1a1a;
        overflow-x: hidden;
    }}
    .romantic-title {{
        text-align: center;
        color: #0d47a1;
        font-family: 'Georgia', serif;
        font-weight: bold;
        padding-top: 10px;
        text-shadow: 0 2px 4px rgba(255,255,255,0.8);
    }}
    .subtitle {{
        text-align: center;
        color: #1565c0;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: bold;
    }}
    .love-card {{
        background: rgba(255, 255, 255, 0.95);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
        backdrop-filter: blur(4px);
        border: 2px solid rgba(13, 71, 161, 0.2);
        text-align: center;
        margin-bottom: 20px;
        color: #1a1a1a;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {{
        color: #0d47a1 !important;
        font-weight: bold;
    }}
    .love-card p, .love-card label {{
        color: #1a1a1a !important;
        font-weight: 600;
    }}
    
    /* --- BINGKAI FOTO ROMANTIS --- */
    .img-frame {{
        background: #ffffff;
        padding: 8px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(13, 71, 161, 0.2);
        border: 3px solid #0d47a1;
    }}

    /* --- TOMBOL KONTRAS TINGGI & MUDAH DIKLIK --- */
    div.stButton > button {{
        background: linear-gradient(135deg, #0d47a1 0%, #1565c0 100%);
        color: #ffffff !important;
        border-radius: 12px;
        font-weight: bold;
        font-size: 16px;
        padding: 12px 24px;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 15px rgba(13, 71, 161, 0.4);
        width: 100%;
        cursor: pointer;
    }}
    div.stButton > button:hover {{
        background: linear-gradient(135deg, #1565c0 0%, #1976d2 100%);
        border-color: #ffd54f;
    }}

    /* --- ANIMASI HURUF, BUNGA PINK, BALON & KUPU-KUPU --- */
    @keyframes floatDown {{
        0% {{ transform: translateY(-10vh) scale(1) rotate(0deg); opacity: 0; }}
        15% {{ opacity: 0.9; }}
        85% {{ opacity: 0.9; }}
        100% {{ transform: translateY(105vh) scale(1.2) rotate(360deg); opacity: 0; }}
    }}
    .floating-bg {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        overflow: hidden; pointer-events: none; z-index: 1;
    }}
    .floating-item {{
        position: absolute; top: -60px;
        font-size: 32px; font-weight: bold;
        color: rgba(13, 71, 161, 0.7);
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.9);
        animation: floatDown 10s infinite linear;
    }}
    </style>

    <!-- Elemen Animasi Latar Belakang (A-V-R-I-L-L-I-A, Bunga Pink, Balon, Kupu-kupu) -->
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

st.markdown(css_template.format(bg_val=current_bg), unsafe_allow_html=True)

# Easter Egg Title Script (Tab browser berubah saat ditinggal)
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

# --- JADWAL MINGGUAN & TIME-LOCK CALENDAR ---
start_of_week = today - datetime.timedelta(days=today.weekday())

weekly_schedule = {
    0: { # SENIN
        "nama": "Senin", "tanggal": start_of_week + datetime.timedelta(days=0),
        "tema": "💼 Edisi Senin: Pawang Kerja Anti-Mager",
        "pesan": "Selamat hari Senin, pawang kerjaku! 🦖✨ Semangat ya kerjanya hari ini! Ingat, kalau kerjaan bikin pusing, tarik napas dalam-dalam dan ingat dompetmu butuh asupan saldo sehat. Senyum dong biar monitor kantor silau sama cantiknya kamu! 🤍💪",
        "foto": "foto_senin.jpeg", "fitur_spesial": "weather_note"
    },
    1: { # SELASA (Bertukar dari Sabtu + Fitur Plot Twist The Fake System Error)
        "nama": "Selasa", "tanggal": start_of_week + datetime.timedelta(days=1),
        "tema": "🌿 Edisi Selasa: Waktunya Me-Time & Santai",
        "pesan": "Selamat hari Selasa! Waktunya menikmati hari dengan rileks dan santai. Jangan terlalu diforsir kerjanya ya jagoanku! ✨",
        "foto": "foto_selasa.jpeg", "fitur_spesial": "fake_error"
    },
    2: { # RABU (Mood Tracker Pindah ke sini)
        "nama": "Rabu", "tanggal": start_of_week + datetime.timedelta(days=2),
        "tema": "✨ Edisi Rabu: Mid-Week Hug (Setengah Perjalanan)",
        "pesan": "Udah hari Rabu nih! Nggak terasa udah setengah jalan menuju weekend. Tetap semangat ya bidadari Berastagi! Kerjaan sebanyak apapun pasti kelar kalau dikerjakan pakai senyuman manismu. 🫂🤍",
        "foto": "foto_rabu.jpeg", "fitur_spesial": "mood_tracker"
    },
    3: { # KAMIS
        "nama": "Kamis", "tanggal": start_of_week + datetime.timedelta(days=3),
        "tema": "🌸 Edisi Kamis: Kamisan Manis Menuju Weekend",
        "pesan": "Selamat hari Kamis! Sikit lagi mau weekend, tahan dikit lagi ya! Tetap fokus, jaga kesehatan, dan ingat ada aku yang selalu dukung kamu dari jauh. Semangat pejuang rupiah! 🤍",
        "foto": "foto_kamis.jpeg", "fitur_spesial": "snap_challenge"
    },
    4: { # JUMAT
        "nama": "Jumat", "tanggal": start_of_week + datetime.timedelta(days=4),
        "tema": "🥳 Edisi Jumat: Jumat Berkah & Bau-bau Weekend",
        "pesan": "Yeay, Jumat berkah! Hari terakhir kerja sebelum weekend. Selesaikan sisa tugasmu dengan senyuman paling cerah ya! Sebentar lagi mau santai-santai. Pokoknya hari ini harus happy! 🤍",
        "foto": "foto_jumat.jpeg", "fitur_spesial": "spam_notification"
    },
    5: { # SABTU (Bertukar dari Selasa + Tombol Lari)
        "nama": "Sabtu", "tanggal": start_of_week + datetime.timedelta(days=5),
        "tema": "☕ Edisi Sabtu: Secangkir Kopi & Senyumanmu",
        "pesan": "Selamat hari Sabtu, kesayanganku! ☕ Jangan lupa sarapan yang enak ya, biar energinya full. Kalau ada yang nyebelin, senyumin aja karena cantiknya kamu nggak ada tandingan. Semangat! 🤍",
        "foto": "foto_sabtu.jpeg", "fitur_spesial": "running_button"
    },
    6: { # MINGGU
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

# Eksekusi Fitur Spesial Berdasarkan Hari
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

# ⛰️ 2. FOTO UTAMA HARIAN
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
                <h4 style="color: #0d47a1; margin-bottom: 8px;">Bidadari Berastagi Paling Bersinar... ✨</h4>
                <p style="color: #2d2d2d; font-size: 0.95em; line-height: 1.6;">
                Sejauh apapun jarak kita atau sibuknya hari ini, energiku langsung terisi lagi cuma karena bayangin senyuman kamu. Proud of you! 🤍
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto harian belum di-upload di GitHub (sediakan `foto_senin.jpeg`, dll atau `foto_dirimu.jpeg`).")
st.markdown("</div>", unsafe_allow_html=True)

# 🎵 3. JUKEBOX LAGU HINDIA & .F.E.A.S.T
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

if "Secukupnya" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/J762g_t6-q4" frameborder="0" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Rumah ke Rumah" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/5H3p96u8_8k" frameborder="0" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
elif "Evaluasi" in pilihan_lagu:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/2q8X93a9n6o" frameborder="0" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)
else:
    st.markdown("""<iframe width="100%" height="180" src="https://www.youtube.com/embed/DrulgpXAGCA" frameborder="0" allowfullscreen style="border-radius: 12px;"></iframe>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 🕰️ 4. KAPSUL WAKTU MINGGU INI (TIME-LOCK CALENDAR)
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

# 📥 5. KOTAK CURHAT (SECRET INBOX)
st.markdown("<div class='love-card'><h3>📥 Kotak Curhat Rahasia</h3><p>Ada uneg-uneg atau capek hari ini? Ketik di sini, pesannya langsung masuk ke Panel Zefanya:</p>", unsafe_allow_html=True)
curhat_input = st.text_area("Tulis ceritamu di sini...")
if st.button("Kirim ke Zefanya"):
    if curhat_input.strip():
        save_response("Kotak Curhat Rahasia", curhat_input)
        st.success("Curhatanmu sudah sampai di hati (dan panel) Zefanya! 🤍")
    else:
        st.warning("Tulis dulu pesannya ya.")
st.markdown("</div>", unsafe_allow_html=True)

# ✨ 6. PENILAIAN KEBAHAGIAAN (BAHASA MEDAN)
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

# 📲 7. LAPOR WHATSAPP
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca? Klik tombol di bawah buat kirim kabar ke WhatsApp aku ya:</p>", unsafe_allow_html=True)
nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web surat harian nih! 🤍✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width: 100%; background-color: #25D366; color: white; padding: 12px 20px; border: none; border-radius: 10px; font-weight: bold; font-size: 16px; cursor: pointer;">
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
st.markdown("<p style='text-align: center; color: #fff; font-size: 0.85em; font-weight: bold;'>Web ini online 24/7 buat kamu yang selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
