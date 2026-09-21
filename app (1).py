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

# Custom CSS: Nuansa Biru Estetik, Tombol Kontras, Bingkai Foto, & Animasi Huruf AVRILLIA + Balon/Kupu-Kupu
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 50%, #90caf9 100%);
        color: #1a1a1a;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: #0d47a1;
        font-family: 'Georgia', serif;
        font-weight: 400;
        padding-top: 10px;
    }
    .subtitle {
        text-align: center;
        color: #1565c0;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: 500;
    }
    .love-card {
        background: rgba(255, 255, 255, 0.90);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        text-align: center;
        margin-bottom: 20px;
        color: #1a1a1a;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: #0d47a1 !important;
    }
    .love-card p {
        color: #2d2d2d !important;
    }
    div[data-testid="stMarkdownContainer"] p, 
    div[data-testid="stRadio"] label, 
    div[data-testid="stTextInput"] label,
    div[data-testid="stDateInput"] label {
        color: #1a1a1a !important;
        font-weight: 500;
    }
    
    /* --- BINGKAI FOTO ROMANTIS --- */
    .img-frame {
        background: #ffffff;
        padding: 8px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(13, 71, 161, 0.15);
        border: 3px solid rgba(13, 71, 161, 0.15);
    }

    /* --- STYLING TOMBOL SIMPAN / AKSI --- */
    div.stButton > button {
        background: linear-gradient(135deg, #1976d2 0%, #0d47a1 100%);
        color: #ffffff !important;
        border-radius: 12px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 4px 12px rgba(13, 71, 161, 0.3);
        width: 100%;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #2196f3 0%, #1565c0 100%);
        color: #ffffff !important;
    }

    /* --- ANIMASI HURUF, BALON & KUPU-KUPU (DARI ATAS KE BAWAH) --- */
    @keyframes floatDown {
        0% {
            transform: translateY(-10vh) scale(1) rotate(0deg);
            opacity: 0;
        }
        15% {
            opacity: 0.85;
        }
        85% {
            opacity: 0.85;
        }
        100% {
            transform: translateY(105vh) scale(1.2) rotate(360deg);
            opacity: 0;
        }
    }
    .floating-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        pointer-events: none;
        z-index: 1;
    }
    .floating-item {
        position: absolute;
        top: -60px;
        font-size: 38px;
        font-family: 'Georgia', serif;
        font-weight: bold;
        color: rgba(13, 71, 161, 0.65);
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.9);
        animation: floatDown 10s infinite linear;
    }
    </style>

    <!-- Elemen Animasi Huruf AVRILLIA, Balon & Kupu-Kupu dari Atas ke Bawah -->
    <div class="floating-bg">
        <div class="floating-item" style="left: 5%; animation-duration: 9s; animation-delay: 0s;">A</div>
        <div class="floating-item" style="left: 15%; animation-duration: 11s; animation-delay: 2s;">🦋</div>
        <div class="floating-item" style="left: 25%; animation-duration: 8s; animation-delay: 1s;">V</div>
        <div class="floating-item" style="left: 35%; animation-duration: 12s; animation-delay: 3s;">🎈</div>
        <div class="floating-item" style="left: 45%; animation-duration: 9.5s; animation-delay: 0.5s;">R</div>
        <div class="floating-item" style="left: 55%; animation-duration: 10.5s; animation-delay: 2.5s;">I</div>
        <div class="floating-item" style="left: 65%; animation-duration: 11.5s; animation-delay: 1.5s;">L</div>
        <div class="floating-item" style="left: 75%; animation-duration: 8.5s; animation-delay: 3.5s;">L</div>
        <div class="floating-item" style="left: 82%; animation-duration: 10s; animation-delay: 0.8s;">I</div>
        <div class="floating-item" style="left: 92%; animation-duration: 9s; animation-delay: 2.2s;">A</div>
    </div>
""", unsafe_allow_html=True)

# 🎈 Efek Sambutan Meriah (Balon muncul saat pertama kali masuk web)
if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state['welcomed'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Surat Harian & Kasih Sayang — Update per {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# 🎵 1. Pemutar Musik YouTube (Hindia - Kita ke Sana)
st.markdown("<div class='love-card'><h3>🎵 Lagu Kita (Hindia - Kita ke Sana)</h3><p>Putar lagu ini langsung di sini biar harimu makin tenang:</p>", unsafe_allow_html=True)
st.markdown("""
    <iframe width="100%" height="210" src="https://www.youtube.com/embed/DrulgpXAGCA" 
        title="Hindia - Kita ke Sana (Official Lyric Video)" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen style="border-radius: 12px;">
    </iframe>
""", unsafe_allow_html=True)
st.markdown("<small style='color: #555;'>*Nikmati alunan musiknya sambil membaca surat hari ini.*</small></div>", unsafe_allow_html=True)

# 📅 2. Surat Hari Ini (Edisi Hari Senin - Lucu & Penyemangat Kerja)
arsip_surat_harian = {
    "2026-09-21": "Selamat hari Senin, pawang kerjaku! 🦖✨ Semangat ya kerjanya hari ini! Ingat, kalau kerjaan bikin pusing, tarik napas dalam-dalam, minum air putih, dan ingat kalau dompetmu butuh asupan saldo yang sehat. Jangan cemberut ya, senyum dong biar monitor kantornya silau sama cantiknya kamu! Kalau ada yang nyebelin hari ini, bayangin aja aku lagi ngelawak di sebelahmu. Fighting! 🤍💪",
    "2026-09-20": "Selamat hari Minggu dan selamat menikmati hari liburmu ya!",
}

today_str = datetime.date.today().strftime("%Y-%m-%d")
default_pesan_hari_ini = arsip_surat_harian.get(today_str, "Halo Avrillia! Selamat hari Senin, hadapi kerjaan hari ini dengan senyuman mautmu ya 🤍")

st.markdown("<div class='love-card'><h3>📬 Surat Hari Ini (Edisi Senin Semangat 💼)</h3>", unsafe_allow_html=True)
st.info(f"✨ **Pesan untuk hari ini ({datetime.date.today().strftime('%d %b')}):**\n\n> {default_pesan_hari_ini}")

with st.expander("📖 Lihat Arsip Pesan Hari-Hari Sebelumnya"):
    for tgl, psn in arsip_surat_harian.items():
        st.write(f"- **{tgl}**: {psn}")
st.markdown("</div>", unsafe_allow_html=True)

# 🚌 3. Pesan Super Kreatif Berastagi (Layout Dua Kolom dengan Foto: foto_dirimu.jpeg / jpg)
st.markdown("<div class='love-card'><h3>⛰️ Pesan Spesial untuk Jagoan Berastagi</h3><p>Penyemangat super buat hari ini:</p>", unsafe_allow_html=True)
st.info("✨ *'Hei orang hebat di Berastagi! Walaupun udaranya dingin dan kerjaan hari Senin ini kelihatan banyak, ingat ya kamu itu jauh lebih kuat dari deadline manapun. Jangan lupa pakai jaket kesayangan dan senyum manisnya dipasang terus. Semangat menjemput rezeki, nanti kalau udah selesai aku kasih pelukan virtual paling erat!'* 🤍")

img_path_1 = "foto_dirimu.jpeg" if os.path.exists("foto_dirimu.jpeg") else ("foto_dirimu.jpg" if os.path.exists("foto_dirimu.jpg") else None)

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
                Melihat foto ini bikin aku sadar, sejauh apapun jarak kita atau seberapa sibuknya hari Senin ini, energinya langsung terisi lagi cuma karena bayangin senyuman kamu. Kamu hebat banget hari ini, proud of you! 🤍
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto baru belum di-upload (gunakan nama `foto_dirimu.jpeg` atau `foto_dirimu.jpg` di GitHub).")
st.markdown("</div>", unsafe_allow_html=True)

# ⏳ 4. Waktu Kita (Layout Dua Kolom dengan Foto: foto_waktu_kita.jpeg / jpg)
st.markdown("<div class='love-card'><h3>⏳ Waktu Kita (Momen Spesial Baru)</h3><p>Kenangan indah yang selalu jadi alasan untuk bertahan 🤍</p>", unsafe_allow_html=True)

img_path_2 = "foto_waktu_kita.jpeg" if os.path.exists("foto_waktu_kita.jpeg") else ("foto_waktu_kita.jpg" if os.path.exists("foto_waktu_kita.jpg") else None)

if img_path_2:
    col_img2, col_txt2 = st.columns([1, 1], gap="medium")
    with col_img2:
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image(img_path_2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_txt2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 10px; text-align: left;">
                <h4 style="color: #0d47a1; margin-bottom: 8px;">Rumah Adalah Kamu... 🤗🤍</h4>
                <p style="color: #2d2d2d; font-size: 0.95em; line-height: 1.6;">
                Di antara semua tempat di dunia, bersandar dan ketawa bareng kamu di momen ini adalah definisi kenyamanan yang hakiki. Terima kasih ya sudah jadi rumah tempat aku selalu ingin pulang. 🫂✨
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto waktu kita belum di-upload (gunakan nama `foto_waktu_kita.jpeg` atau `foto_waktu_kita.jpg` di GitHub).")

st.markdown("</div>", unsafe_allow_html=True)

# 🧘‍♀️ 5. Time Capsule: Video Peregangan Kerja & Mini Game "Kotak Kejutan Cinta"
st.markdown("<div class='love-card'><h3>🧘‍♀️ Pojok Sehat & Refreshing Kerja</h3><p>Yuk luangkan waktu sebentar buat stretching biar badannya tidak kaku, tonton video di bawah ya: 👇</p>", unsafe_allow_html=True)

# Embed YouTube Short untuk peregangan kerja
st.video("https://youtube.com/shorts/DWwsx-VmCQQ")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4>🎁 Kotak Kejutan Cinta (Mini Game)</h4><p>Pencet tombol di bawah untuk ambil kartu semangat acak khusus buat kamu:</p>", unsafe_allow_html=True)

if 'random_quote' not in st.session_state:
    st.session_state['random_quote'] = "Pencet tombol di bawah dulu ya sayang! 👇"

if st.button("🎲 Ambil Kartu Semangat Acak"):
    quotes_list = [
        "✨ 'Kamu hebat banget hari ini! Jangan lupa senyum dan minum air putih ya.'",
        "🦖 'Pawang kerjaku nomor satu! Kalau capek, bayangin aku lagi bawain es krim kesukaanmu.'",
        "🤍 'Jarak boleh jauh, tapi doa dan sayangku selalu nemenin kamu di Berastagi.'",
        "💪 'Deadline aja bisa kamu taklukkan, apalagi cuma hari Senin! Semangat jagoan!'"
    ]
    st.session_state['random_quote'] = random.choice(quotes_list)
    st.balloons()

st.info(st.session_state['random_quote'])
st.markdown("</div>", unsafe_allow_html=True)

# ✨ 6. Penilaian Kebahagiaan Membaca Surat (Isi Versi Lucu & Menghibur)
st.markdown("<div class='love-card'><h3>💖 Seberapa Senang Kamu Baca Surat Ini?</h3><p>Pilih tingkat kebahagiaanmu dengan jujur (atau kena denda senyum):</p>", unsafe_allow_html=True)

pilihan_senang = st.radio("Pilih ekspresi kamu sekarang:", [
    "Senang banget kayak menang doorprize kulkas dua pintu 🧊", 
    "Bahagia pol sampe mau minta traktir sushi 🍣", 
    "Senyum-senyum sendiri dikira orang gila sama teman sekantor 🤪"
])

if st.button("💾 Simpan Perasaanku"):
    save_response("Tingkat Kebahagiaan Membaca Surat", pilihan_senang)
    st.success("Yeay! Jawaban gemasmu sudah sukses masuk ke Panel Zefanya 🤍")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Tombol Konfirmasi ke WhatsApp Kamu
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca semuanya? Klik tombol di bawah buat kirim kabar ke WhatsApp aku ya:</p>", unsafe_allow_html=True)

nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web surat edisi hari Senin nih! 🤍✨"
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
        st.success("PIN benar!")
        df_data = get_responses()
        if not df_data.empty:
            st.dataframe(df_data, use_container_width=True)
            
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
            st.info("Belum ada data.")
    elif pin_input:
        st.error("PIN salah.")

# Footer manis
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333; font-size: 0.85em; font-weight: 500;'>Web ini online 24/7 buat kamu yang bisa selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
