import streamlit as st
import datetime
import random

# Konfigurasi Halaman
st.set_page_config(
    page_title="Untuk Kamu yang Dirindukan 🤍", 
    page_icon="Avrillia💌", 
    layout="centered"
)

# Custom CSS: nuansa aesthetic/romantis dengan teks hitam jelas
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffd1dc 50%, #ffc0cb 100%);
        color: #1a1a1a;
    }
    .romantic-title {
        text-align: center;
        color: #8b1e41;
        font-family: 'Georgia', serif;
        font-weight: 400;
        padding-top: 10px;
    }
    .subtitle {
        text-align: center;
        color: #3b2a26;
        font-style: italic;
        margin-bottom: 30px;
        font-weight: 500;
    }
    .love-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
        margin-bottom: 20px;
        color: #1a1a1a;
    }
    .love-card h3 {
        color: #2b1b17 !important;
    }
    .love-card p {
        color: #2d2d2d !important;
    }
    /* Mengubah warna teks widget streamlit agar gelap/hitam */
    div[data-testid="stMarkdownContainer"] p, 
    div[data-testid="stRadio"] label, 
    div[data-testid="stTextInput"] label,
    div[data-testid="stDateInput"] label {
        color: #1a1a1a !important;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown("<h1 class='romantic-title'>For My Favorite Person 🤍</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Kasih sayang yang tidak punya tombol 'off'</p>", unsafe_allow_html=True)

# 1. Hari / Waktu Bersama (Bisa diketik atau pilih kalender)
st.markdown("<div class='love-card'><h3>⏳ Menghitung Waktu Berharga</h3>", unsafe_allow_html=True)

tipe_input = st.radio("Pilih cara input hari spesial:", ["Pilih Tanggal Kalender", "Ketik Tanggal/Cerita Sendiri"])

if tipe_input == "Pilih Tanggal Kalender":
    start_date = st.date_input("Kapan hari spesial/mulai dekat kita?", datetime.date(2021, 1, 16))
    today = datetime.date.today()
    days_count = (today - start_date).days
    st.metric(label="Hari penuh cerita terukir:", value=f"{days_count:,} Hari")
else:
    custom_text = st.text_input("Ketik tanggal / catatan hari spesial kalian:", value="11 Juni 2023 - Awal mula cerita")
    st.info(f"✨ Catatan tersimpan: **{custom_text}**")

st.markdown("</div>", unsafe_allow_html=True)

# 2. Tombol Saat Kangen
st.markdown("<div class='love-card'><h3>💌 Lagi Kangen Ya?</h3><p>Klik tombol di bawah kalau pas lagi kangen tapi gengsi/jarak membatasi:</p>", unsafe_allow_html=True)

pesan_kangen = [
    "Hei... jangan lupa makan, jangan terlalu kecapekan. Aku di sini.",
    "Rindu ini ibarat ombak, kadang tenang kadang kencang, tapi tujuannya tetap ke pantai yang sama: kamu.",
    "Walaupun gak ngabarin 24 jam, pikiranku sempat mampir ke senyummu hari ini kok.",
    "Kasih sayang ini tidak akan putus cuma karena sibuk atau jarak. Tetap bernafas dengan tenang ya."
]

if st.button("Pencet Kalau suka:)", use_container_width=True):
    st.balloons()
    st.success(random.choice(pesan_kangen))
st.markdown("</div>", unsafe_allow_html=True)

# 3. Alasan Kenapa Sayang
st.markdown("<div class='love-card'><h3>✨ Alasan Kenapa Aku Bisa Kagum & Sayang</h3>", unsafe_allow_html=True)
alasan_list = [
    "aku rindu makan sushi, selama gak ada kamu gak pernah lagi makan sushi.",
    "Cara kamu ketawa dan senyum lepas pas dengar hal konyol.",
    "Ketulusan kamu waktu cerita hal-hal kecil yang bikin antusias.",
    "Cara bertahan kamu di hari-hari yang berat tanpa banyak mengeluh ke publik.",
    "Keberadaan kamu yang bikin tempat biasa jadi terasa 'rumah'."
]

if st.button("Buka Satu Alasan Hari Ini 🎲", use_container_width=True):
    st.info(random.choice(alasan_list))
st.markdown("</div>", unsafe_allow_html=True)

# Footer manis
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4a4a4a; font-size: 0.85em; font-weight: 500;'>Web ini online 24/7 buat kamu buka kapan saja rindu datang 🤍</p>", unsafe_allow_html=True)
