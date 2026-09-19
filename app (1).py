import streamlit as st
import datetime
import sqlite3
import pandas as pd

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

# Custom CSS: Nuansa Biru Estetik, Tombol Kontras, & Animasi Kupu-Kupu / Balon Terbang
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
    
    /* --- STYLING TOMBOL SIMPAN (Jelas, kontras, warna biru terang) --- */
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

    /* --- ANIMASI KUPU-KUPU & BALON TERBANG DI BACKGROUND --- */
    @keyframes floatUp {
        0% {
            transform: translateY(105vh) scale(0.7) rotate(0deg);
            opacity: 0;
        }
        20% {
            opacity: 0.8;
        }
        80% {
            opacity: 0.8;
        }
        100% {
            transform: translateY(-10vh) scale(1.2) rotate(360deg);
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
        bottom: -50px;
        font-size: 26px;
        animation: floatUp 12s infinite linear;
    }
    </style>

    <!-- Elemen Animasi Kupu-Kupu & Balon -->
    <div class="floating-bg">
        <div class="floating-item" style="left: 10%; animation-duration: 11s; animation-delay: 0s;">🦋</div>
        <div class="floating-item" style="left: 25%; animation-duration: 14s; animation-delay: 3s;">🎈</div>
        <div class="floating-item" style="left: 45%; animation-duration: 10s; animation-delay: 1s;">🦋</div>
        <div class="floating-item" style="left: 65%; animation-duration: 13s; animation-delay: 4s;">🎈</div>
        <div class="floating-item" style="left: 85%; animation-duration: 12s; animation-delay: 2s;">🦋</div>
    </div>
""", unsafe_allow_html=True)

# 🎈 Efek Sambutan Meriah (Balon & Kupu-kupu muncul saat pertama kali masuk web)
if 'welcomed' not in st.session_state:
    st.balloons()
    st.session_state['welcomed'] = True

# Header Utama
st.markdown("<h1 class='romantic-title'>Avrillia🤍</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Surat Harian & Kasih Sayang — Update per {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# 🎵 1. Pemutar Musik YouTube (Hindia - Cincin)
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
    "2026-09-19": "Hari ini harus banyak senyum ya, soalnya senyum kamu bikin canduuuuu !",
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

# ⛰️ Kata-kata Semangat Kerja di Berastagi
st.markdown("<div class='love-card'><h3>⛰️ Semangat Kerja di Berastagi!</h3><p>Pesan khusus untuk penyemangat aktivitasmu di sana:</p>", unsafe_allow_html=True)
st.info("✨ *'Semangat ya kerjanya di Berastagi! Walaupun udaranya dingin atau mungkin ada kecapekan dalam pekerjaan atau ada yang gosipin kamu, ingat kalau kerja kerasmu hari ini adalah langkah hebat buat masa depan dan jangan hiraukan apa kata orang ya. Jangan lupa pakai jaket hangat, jaga kesehatan, dan jangan pernah skip makan ya! Aku selalu mendoakan dan mendukungmu dari sini.'* 🤍")
st.markdown("</div>", unsafe_allow_html=True)

# ⏳ Waktu Kita (Input Langsung di Web & Simpan ke Database)
st.markdown("<div class='love-card'><h3>⏳ Waktu Kita</h3><p>Kapan waktu yang paling terbaik kita (sampai kamu senang banget)? Ketik di bawah ya:</p>", unsafe_allow_html=True)

jawaban_waktu = st.text_input("Tulis momen terbaik kita di sini:", key="input_waktu_kita")
if st.button("💾 Simpan Jawaban Waktu Kita"):
    if jawaban_waktu.strip():
        save_response("Waktu Kita (Terbaik)", jawaban_waktu)
        st.success("Yeay! Jawabanmu sudah tersimpan rapi untuk Zefanya 🤍")
        st.balloons()
    else:
        st.warning("Tulis dulu ya pesannya...")
st.markdown("</div>", unsafe_allow_html=True)

# 🧠 Kuis Kecil (Input Langsung di Web & Simpan ke Database)
st.markdown("<div class='love-card'><h3>🧠 Kuis Kecil Buat Avrillia</h3><p>Jawab pertanyaan di bawah ini ya:</p>", unsafe_allow_html=True)

quiz_1 = st.text_input("1. Kapan tanggal ulang tahunku?", key="q_ultah")
quiz_2 = st.text_input("2. Apa makanan kesukaanku?", key="q_makanan")
quiz_3 = st.text_input("3. Apa kelebihanku di mata kamu?", key="q_kelebihan")

if st.button("💾 Simpan Jawaban Kuis"):
    if quiz_1.strip() or quiz_2.strip() or quiz_3.strip():
        teks_gabungan = f"Ultah: {quiz_1} | Makanan: {quiz_2} | Kelebihan: {quiz_3}"
        save_response("Kuis Kecil", teks_gabungan)
        st.success("Terima kasih sayang, jawaban kuisnya sudah tersimpan! 🤍")
        st.balloons()
    else:
        st.warning("Isi dulu minimal salah satu pertanyaannya ya...")
st.markdown("</div>", unsafe_allow_html=True)

# Tombol Lapor ke WhatsApp Kamu secara umum
st.markdown("<div class='love-card'><h3>✅ Konfirmasi Mampir</h3><p>Udah selesai baca semuanya? Klik tombol di bawah buat kirim kabar biasa ke WhatsApp akur ya:</p>", unsafe_allow_html=True)

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

# ==========================================
# 🔒 PANEL KHUSUS ZEFANYA (MELIHAT & MENGHAPUS JAWABAN)
# ==========================================
st.markdown("<br><hr>", unsafe_allow_html=True)
with st.expander("🔒 Panel Khusus Zefanya (Klik di sini untuk melihat jawaban Avrillia)"):
    st.markdown("Masukkan PIN rahasia untuk melihat data jawaban yang masuk:")
    pin_input = st.text_input("PIN Rahasia:", type="password")
    
    # PIN rahasia kamu (bisa diubah sesuai keinginan)
    PIN_RAHASIA = "2021" 
    
    if pin_input == PIN_RAHASIA:
        st.success("PIN benar! Berikut adalah daftar jawaban dari Avrillia:")
        df_data = get_responses()
        if not df_data.empty:
            st.dataframe(df_data, use_container_width=True)
            
            st.markdown("---")
            st.markdown("🗑️ **Hapus Jawaban:**")
            id_to_delete = st.number_input("Masukkan Nomor ID (Kolom ID) dari jawaban yang ingin dihapus:", min_value=1, step=1)
            if st.button("❌ Hapus Jawaban Ini"):
                if id_to_delete in df_data['id'].values:
                    delete_response(id_to_delete)
                    st.success(f"Jawaban dengan ID {id_to_delete} berhasil dihapus! Silakan refresh halaman.")
                    st.rerun()
                else:
                    st.error("Nomor ID tidak ditemukan di database.")
        else:
            st.info("Belum ada jawaban yang dikirim.")
    elif pin_input:
        st.error("PIN salah! Coba ingat-ingat lagi ya.")

# Footer manis
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333; font-size: 0.85em; font-weight: 500;'>Web ini online 24/7 buat kamu yang bisa selalu update, semoga happy 🤍</p>", unsafe_allow_html=True)
