import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os

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

# Custom CSS: Nuansa Biru Estetik, Tombol Kontras, Bingkai Foto, & Animasi Balon/Kupu-Kupu Besar
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

    /* --- ANIMASI BALON & KUPU-KUPU BESAR (DARI ATAS KE BAWAH) --- */
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
        font-size: 42px;
        animation: floatDown 10s infinite linear;
    }
    </style>

    <!-- Elemen Animasi Balon & Kupu-Kupu Besar dari Atas ke Bawah -->
    <div class="floating-bg">
        <div class="floating-item" style="left: 10%; animation-duration: 9s; animation-delay: 0s;">🦋</div>
        <div class="floating-item" style="left: 28%; animation-duration: 12s; animation-delay: 2s;">🎈</div>
        <div class="floating-item" style="left: 48%; animation-duration: 10s; animation-delay: 1s;">🦋</div>
        <div class="floating-item" style="left: 68%; animation-duration: 11s; animation-delay: 3s;">🎈</div>
        <div class="floating-item" style="left: 88%; animation-duration: 8s; animation-delay: 1.5s;">🦋</div>
    </div>
""", unsafe_allow_html=True)

# 🎈 Efek Sambutan Meriah (Balon muncul saat pertama kali masuk web)
if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state['welcomed'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Surat Harian & Kasih Sayang — Update per {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# 🎵 1. Pemutar Musik YouTube (Hindia - Everything You Are)
st.markdown("<div class='love-card'><h3>🎵 Lagu Kita (Hindia - Everything You Are)</h3><p>Putar lagu ini langsung di sini biar suasananya makin tenang:</p>", unsafe_allow_html=True)
st.markdown("""
    <iframe width="100%" height="210" src="https://www.youtube.com/embed/lB8ASupNtlw" 
        title="Hindia - Everything You Are (Official Lyric Video)" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen style="border-radius: 12px;">
    </iframe>
""", unsafe_allow_html=True)
st.markdown("<small style='color: #555;'>*Nikmati alunan musiknya sambil membaca surat hari ini.*</small></div>", unsafe_allow_html=True)

# 📅 1. Surat Hari Ini (Edisi Hari Minggu / Libur)
arsip_surat_harian = {
    "2026-09-20": "Selamat hari Minggu dan selamat menikmati hari liburmu ya! Semoga hari ini benar-benar jadi waktu yang pas buat recharge energi, istirahat yang tenang, dan melakukan hal-hal yang bikin kamu happy. Jangan mikirin kerjaan dulu ya hari ini, nikmati waktu santaimu secukupnya. I'm always cheering for you! 🤍",
    "2026-09-19": "Hari ini harus banyak senyum ya, jalani hari dengan hati yang ringan!",
    "2026-09-18": "Kangen sushi lagi gak? Semoga weekend ini ada waktu buat makan bareng ya.",
}

today_str = datetime.date.today().strftime("%Y-%m-%d")
default_pesan_hari_ini = arsip_surat_harian.get(today_str, "Halo Avrillia! Selamat hari Minggu, nikmati liburmu dengan senyuman paling manis ya 🤍")

st.markdown("<div class='love-card'><h3>📬 Surat Hari Ini (Edisi Hari Minggu ☀️)</h3>", unsafe_allow_html=True)
st.info(f"✨ **Pesan untuk hari ini ({datetime.date.today().strftime('%d %b')}):**\n\n> {default_pesan_hari_ini}")

with st.expander("📖 Lihat Arsip Pesan Hari-Hari Sebelumnya"):
    for tgl, psn in arsip_surat_harian.items():
        st.write(f"- **{tgl}**: {psn}")
st.markdown("</div>", unsafe_allow_html=True)

# 🚌 3. Perjalanan Medan ke Berastagi (Layout Dua Kolom: Foto & Pesan Kecantikan/Senyuman)
st.markdown("<div class='love-card'><h3>🚌 Hati-Hati di Perjalanan ke Berastagi</h3><p>Pesan khusus untuk perjalananmu siang ini:</p>", unsafe_allow_html=True)
st.info("✨ *'Avrillia, selamat menikmati hari di Medan ya pagi ini. Nanti siang pas mau balik ke Berastagi naik bus, tolong jaga diri baik-baik ya, jangan tidur pulas di jalan, pasang jaket yang hangat karena udaranya nanti dingin, dan kabari aku kalau sudah sampai dengan selamat. Have a safe trip, my love!'* 🤍")

img_path_1 = "foto_perjalanan.jpeg" if os.path.exists("foto_perjalanan.jpeg") else ("foto_perjalanan.jpg" if os.path.exists("foto_perjalanan.jpg") else None)

if img_path_1:
    col_img1, col_txt1 = st.columns([1, 1], gap="medium")
    with col_img1:
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image(img_path_1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_txt1:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 10px; text-align: left;">
                <h4 style="color: #0d47a1; margin-bottom: 8px;">Cantik & Manisnya Kamu... ✨</h4>
                <p style="color: #2d2d2d; font-size: 0.95em; line-height: 1.6;">
                Tau gak? Setiap kali aku lihat foto kamu, aku selalu kagum sama betapa cantiknya kamu. Senyuman manis kamu itu selalu berhasil jadi penenang sekaligus pemandangan paling indah buat aku. Tetap senyum terus ya, kesayanganku! 🤍
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto perjalanan tidak ditemukan di repository GitHub.")
st.markdown("</div>", unsafe_allow_html=True)

# ⏳ 4. Waktu Kita (Layout Dua Kolom: Foto & Pesan Pelukan Hangat)
st.markdown("<div class='love-card'><h3>⏳ Waktu Kita (Galeri Kenangan)</h3><p>Waktu terbaik kita yang selalu jadi tempat berpulang paling nyaman 🤍</p>", unsafe_allow_html=True)

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
                <h4 style="color: #0d47a1; margin-bottom: 8px;">Pelukan Hangat Paling Nyaman... 🤗🤍</h4>
                <p style="color: #2d2d2d; font-size: 0.95em; line-height: 1.6;">
                Tidak ada tempat yang lebih menenangkan di dunia ini selain berada di dalam dekapan pelukan hangatmu. Setiap detik waktu yang kita lewati berdua selalu jadi memori terindah yang paling aku syukuri. Pelukan itu yang selalu bikin aku merasa utuh. 🫂✨
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ File foto waktu kita tidak ditemukan di repository GitHub.")

st.markdown("</div>", unsafe_allow_html=True)

# 🕰️ 5. Time Capsule: Ungkapan Terima Kasih (Klik untuk Membuka)
st.markdown("<div class='love-card'><h3>🕰️ Time Capsule: Pesan & Ungkapan Hati</h3><p>Ada pesan khusus yang tersimpan di sini. Klik tombol di bawah untuk membukanya: 👇</p>", unsafe_allow_html=True)

if 'show_gratitude' not in st.session_state:
    st.session_state['show_gratitude'] = False

if st.button("✨ Klik untuk Membuka Pesan Spesial"):
    st.session_state['show_gratitude'] = True
    st.balloons()

if st.session_state['show_gratitude']:
    st.markdown("""
        <div style='background: rgba(255,255,255,0.95); padding: 22px; border-radius: 15px; text-align: left; color: #1a1a1a; margin-top: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-left: 5px solid #0d47a1;'>
        <h4 style='color: #0d47a1; margin-top: 0;'>Terima Kasih Banyak, Avrillia 🤍</h4>
        <p>Sambil mendengarkan alunan musik ini, aku ingin mengucapkan terima kasih yang sebesar-besarnya dari lubuk hatiku.</p>
        <p>Kamu sudah banyak sekali membantuku dalam segala hal, terutama di masa-masa kita berjuang bersama saat masih mahasiswa—dari urusan tugas, skripsi, dukungan moral, sampai kesabaranmu menghadapi masa-masa lelah dan penuh tekanan.</p>
        <p>Aku tidak akan bisa melaluinya dengan mudah kalau bukan karena kehadiran, ketulusan, dan bantuanmu. Terima kasih sudah selalu jadi tempat berpulang yang paling tenang dan hebat mendampingiku. Aku sangat bersyukur memiliki kamu.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ✨ 6. Penilaian Kebahagiaan Membaca Surat (Tersimpan ke Panel Zefanya)
st.markdown("<div class='love-card'><h3>💖 Seberapa Senang Kamu Baca Surat Ini?</h3><p>Pilih ekspresi kebahagiaanmu hari ini ya:</p>", unsafe_allow_html=True)

pilihan_senang = st.radio("Pilih tingkat kebahagiaan:", ["happy", "happyyy", "happyyyyyyy bgttttt"])

if st.button("💾 Simpan Perasaanku"):
    save_response("Tingkat Kebahagiaan Membaca Surat", pilihan_senang)
    st.success("Yeay! Perasaan senangnya sudah tersimpan untuk Zefanya 🤍")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Tombol Lapor ke WhatsApp Kamu secara umum
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca semuanya? Klik tombol di bawah buat kirim kabar ke WhatsApp aku ya:</p>", unsafe_allow_html=True)

nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web surat hari Minggu ini! 🤍✨"
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
