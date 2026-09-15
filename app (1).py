import streamlit as st
import datetime
import random

# Konfigurasi Halaman
st.set_page_config(
    page_title="Surat Zefanya for Avrillia🤍", 
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
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Surat Harian Zefanya — Update per {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# 📅 ARsip Surat Harian (Tiap hari tinggal tambah di sini!)
arsip_surat_harian = {
    "2026-09-15": "Hari ini harus banyak senyum ya, jangan skip makan walau sibuk kerja!",
   

today_str = datetime.date.today().strftime("%Y-%m-%d")
default_pesan_hari_ini = arsip_surat_harian.get(today_str, "Halo Avrillia! Tetap semangat menjalani hari ini ya, aku selalu dukung dari sini 🤍")

# 1. Kotak Surat Harian Otomatis
st.markdown("<div class='love-card'><h3>📬 Surat Hari Ini</h3>", unsafe_allow_html=True)
st.info(f"✨ **Pesan untuk hari ini ({datetime.date.today().strftime('%d %b')}):**\n\n> {default_pesan_hari_ini}")

with st.expander("📖 Lihat Arsip Pesan Hari-Hari Sebelumnya"):
    for tgl, psn in arsip_surat_harian.items():
        st.write(f"- **{tgl}**: {psn}")
st.markdown("</div>", unsafe_allow_html=True)

# 2. Waktu Kita
st.markdown("<div class='love-card'><h3>⏳ Waktu Kita</h3>", unsafe_allow_html=True)
tipe_input = st.radio("Pilih cara input hari spesial:", ["Pilih Tanggal Kalender", "Ketik Tanggal/Cerita Sendiri"])

if tipe_input == "Pilih Tanggal Kalender":
    start_date = st.date_input("Kapan hari spesial/mulai dekat kita?", datetime.date(2021, 1, 16))
    today = datetime.date.today()
    days_count = (today - start_date).days
    st.metric(label="Hari penuh cerita terukir:", value=f"{days_count:,} Hari")
    st.balloons()
else:
    custom_text = st.text_input("Ketik tanggal / catatan hari spesial kalian:", value="11 Juni 2023 - Awal mula cerita")
    if custom_text:
        st.balloons()
    st.info(f"✨ Catatan tersimpan: **{custom_text}**")
st.markdown("</div>", unsafe_allow_html=True)

# 3. Tombol Saat Kangen
st.markdown("<div class='love-card'><h3>💌 Lagi Kerja ya? Semangat ya, ingat pesan aku ini</h3><p>Klik tombol di bawah kalau pas lagi kangen tapi gengsi/jarak membatasi:</p>", unsafe_allow_html=True)

pesan_kangen = [
    "Hei... jangan lupa makan, jangan terlalu kecapekan, jaga kesehatan. Aku di sini.",
    "Jangan buat aku cemburu please, aku gak kuat tapi mau gimana lagi:(.",
    "Walaupun gak ngabarin, tapi kamu selalu masuk dalam mimpiku.",
    "Kasih sayang ini tidak akan putus cuma karena sibuk, jarak atauapapun itu. Tetap selalu bahagia ya."
]

if st.button("Pencet kalau kangen wkwkwk:)", use_container_width=True):
    st.balloons()
    st.success(random.choice(pesan_kangen))
st.markdown("</div>", unsafe_allow_html=True)

# 4. Alasan Kenapa Sayang
st.markdown("<div class='love-card'><h3>✨ Alasan Kenapa Aku Bisa Kagum & Sayang</h3>", unsafe_allow_html=True)
alasan_list = [
    "aku rindu makan sushi, selama gak ada kamu gak pernah lagi makan sushi.",
    "Cara kamu ketawa dan senyum lepas pas dengar hal konyol.",
    "Ketulusan kamu waktu cerita hal-hal kecil yang bikin antusias.",
    "Karna kamu cantik bangetttttt, masakan kamu juga enakkk.",
    "Cara bertahan kamu di hari-hari yang berat tanpa banyak mengeluh ke publik.",
    "Keberadaan kamu yang bikin tempat biasa jadi terasa 'rumah'."
]

if st.button("Buka Satu Alasan Hari Ini 🎲", use_container_width=True):
    st.markdown("<div style='font-size: 28px; text-align: center; margin: 10px 0;'>💖 💗 💓 💞 💘 💖 💗 💓</div>", unsafe_allow_html=True)
    st.info(random.choice(alasan_list))
st.markdown("</div>", unsafe_allow_html=True)

# 5. Tombol Lapor ke WhatsApp Kamu
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca? Klik tombol di bawah buat kirim kabar ke WhatsApp aku ya:</p>", unsafe_allow_html=True)

# ⚠️ Ganti nomor '628xxxxxxxxxx' di bawah dengan nomor WhatsApp kamu (pakai format 62 di depan, jangan pakai angka 0)
nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web suratnya nih! 🤍✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace('6281216464994', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width: 100%; background-color: #25D366; color: white; padding: 12px 20px; border: none; border-radius: 10px; font-weight: bold; font-size: 16px; cursor: pointer;">
            📲 Klik di Sini Kalau Udah Dibaca (Lapor WA)
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer manis
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4a4a4a; font-size: 0.85em; font-weight: 500;'>Web ini online 24/7 buat kamu yang bisa selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)




