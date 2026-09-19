import streamlit as st
import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="Surat Zefanya for Avrillia🤍", 
    page_icon="Avrillia💌", 
    layout="centered"
)

# Custom CSS: nuansa biru estetik & lembut dengan teks hitam jelas
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 50%, #90caf9 100%);
        color: #1a1a1a;
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
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Surat Harian & Kasih Sayang — Update per {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# 🎵 1. Pemutar Musik YouTube (Hindia - Cincin) - Diperbaiki
st.markdown("<div class='love-card'><h3>🎵 Lagu Kita (Hindia - Cincin)</h3><p>Putar lagu ini langsung di sini biar suasananya makin tenang:</p>", unsafe_allow_html=True)
st.markdown("""
    <iframe width="100%" height="210" src="https://www.youtube.com/embed/S0Kez6MERGE" 
        title="Hindia - Cincin (Official Lyric Video)" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen style="border-radius: 12px;">
    </iframe>
""", unsafe_allow_html=True)
st.markdown("<small style='color: #555;'>*Nikmati alunan musiknya sambil membaca surat hari ini.*</small></div>", unsafe_allow_html=True)

# 📅 Arsip Surat Harian
arsip_surat_harian = {
    "2026-09-19": "Hari ini harus banyak senyum ya, jalani hari dengan hati yang ringan!",
    "2026-09-18": "Kangen sushi lagi gak? Semoga weekend ini ada waktu buat makan bareng ya.",
    "2026-09-17": "Semoga istirahatmu cukup dan harinya menyenangkan.",
}

today_str = datetime.date.today().strftime("%Y-%m-%d")
default_pesan_hari_ini = arsip_surat_harian.get(today_str, "Halo kesayangan! Tetap semangat menjalani hari ini ya, aku selalu dukung dari sini 🤍")

# Kotak Surat Harian Otomatis
st.markdown("<div class='love-card'><h3>📬 Surat Hari Ini</h3>", unsafe_allow_html=True)
st.info(f"✨ **Pesan untuk hari ini ({datetime.date.today().strftime('%d %b')}):**\n\n> {default_pesan_hari_ini}")

with st.expander("📖 Lihat Arsip Pesan Hari-Hari Sebelumnya"):
    for tgl, psn in arsip_surat_harian.items():
        st.write(f"- **{tgl}**: {psn}")
st.markdown("</div>", unsafe_allow_html=True)

# ⛰️ 4. Kata-kata Semangat Kerja di Berastagi
st.markdown("<div class='love-card'><h3>⛰️ Semangat Kerja di Berastagi!</h3><p>Pesan khusus untuk penyemangat aktivitasmu di sana:</p>", unsafe_allow_html=True)
st.info("✨ *'Semangat ya kerjanya di Berastagi! Walaupun udaranya dingin dan kadang bikin mager, ingat kalau kerja kerasmu hari ini adalah langkah hebat buat masa depan. Jangan lupa pakai jaket hangat, jaga kesehatan, dan jangan pernah skip makan ya! Aku selalu mendoakan dan mendukungmu dari sini.'* 🤍")
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

# 3. Kuis Google Form (Ganti link GForm kamu di bawah ini)
st.markdown("<div class='love-card'><h3>🧠 Kuis Kecil Buat Avrillia</h3><p>Yuk isi kuis singkat seputar kita lewat Google Form di bawah ini ya! 👇</p>", unsafe_allow_html=True)

# ⚠️ Ganti link 'https://forms.gle/isigformkamudisini' dengan link Google Form asli buatanmu
link_gform = "https://forms.gle/isigformkamudisini"

st.markdown(f"""
    <a href="{link_gform}" target="_blank">
        <button style="width: 100%; background-color: #0d47a1; color: white; padding: 14px 20px; border: none; border-radius: 10px; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 10px;">
            📝 Buka & Isi Google Form Kuis Kita
        </button>
    </a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Tombol Lapor ke WhatsApp Kamu secara umum
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca semuanya? Klik tombol di bawah buat kirim kabar biasa ke WhatsApp aku ya:</p>", unsafe_allow_html=True)

nomor_wa = "6281216464994" 
pesan_wa = "Halo Zefanya, aku udah mampir dan baca web suratnya nih! 🤍✨"
link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

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
st.markdown("<p style='text-align: center; color: #333; font-size: 0.85em; font-weight: 500;'>Web ini online 24/7 buat kamu yang bisa selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
