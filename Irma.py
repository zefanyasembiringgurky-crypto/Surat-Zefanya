import streamlit as st
import datetime
import os
import time

# Konfigurasi Halaman
st.set_page_config(
    page_title="Happy Birthday Irma Kristiani Ginting 🎂", 
    page_icon="🎉", 
    layout="centered"
)

# --- ZONA WAKTU WIB (UTC+7) ---
wib_offset = datetime.timezone(datetime.timedelta(hours=7))
now_wib = datetime.datetime.now(wib_offset)
current_hour = now_wib.hour

# Custom CSS, Tema Biru Putih Elegan, & Animasi Bom Intro
css_template = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 50%, #f0fdf4 100%);
        color: #0f172a;
        overflow-x: hidden;
    }
    .romantic-title {
        text-align: center;
        color: #0369a1;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 1.8em;
        padding-top: 10px;
        text-shadow: 0 2px 6px rgba(255,255,255,0.9);
    }
    .subtitle {
        text-align: center;
        color: #0284c7;
        font-style: italic;
        margin-bottom: 20px;
        font-weight: 700;
        font-size: 0.95em;
    }
    .love-card {
        background: #ffffff !important;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.06);
        border: 2px solid #38bdf8;
        text-align: center;
        margin-bottom: 16px;
        color: #0f172a !important;
        position: relative;
        z-index: 2;
    }
    .love-card h3 {
        color: #0369a1 !important;
        font-weight: 800 !important;
        font-size: 1.2em !important;
    }
    .love-card h4 {
        color: #0284c7 !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
    }
    .love-card p, .love-card label, .love-card span {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 0.95em !important;
    }
    .message-box {
        background-color: #f8fafc;
        border: 2px solid #bae6fd;
        border-radius: 10px;
        padding: 14px;
        margin-top: 8px;
        margin-bottom: 8px;
        text-align: left;
        color: #1e293b !important;
        font-size: 0.95em;
        font-weight: 600;
        line-height: 1.5;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .img-frame {
        background: #ffffff;
        padding: 8px;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(56, 189, 248, 0.2);
        border: 2px solid #0ea5e9;
        margin-bottom: 10px;
    }
    div.stButton > button {
        background: #0284c7;
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 700;
        font-size: 14px;
        padding: 10px 16px;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
        width: 100%;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background: #0369a1;
        opacity: 0.95;
        border-color: #e0f2fe;
    }
    @keyframes floatDown {
        0% { transform: translateY(-10vh) scale(1) rotate(0deg); opacity: 0; }
        15% { opacity: 0.95; }
        85% { opacity: 0.95; }
        100% { transform: translateY(105vh) scale(1.1) rotate(360deg); opacity: 0; }
    }
    .floating-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        overflow: hidden; pointer-events: none; z-index: 1;
    }
    .floating-item {
        position: absolute; top: -60px;
        font-size: 22px; font-weight: 800;
        color: #0284c7;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.9);
        animation: floatDown 10s infinite linear;
    }
    @keyframes fireworkBurst {
        0% { transform: scale(0.1); opacity: 1; }
        50% { transform: scale(1.5); opacity: 0.8; filter: drop-shadow(0 0 15px #fde047); }
        100% { transform: scale(2.2); opacity: 0; }
    }
    .fireworks-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        font-size: 2.8rem;
        animation: fireworkBurst 1.5s ease-out forwards;
        margin: 10px 0;
    }
    </style>
    <div class="floating-bg">
        <div class="floating-item" style="left: 4%; animation-duration: 9s; animation-delay: 0s;">H</div>
        <div class="floating-item" style="left: 9%; animation-duration: 11s; animation-delay: 2s;">A</div>
        <div class="floating-item" style="left: 14%; animation-duration: 8s; animation-delay: 1s;">P</div>
        <div class="floating-item" style="left: 19%; animation-duration: 12s; animation-delay: 3s;">P</div>
        <div class="floating-item" style="left: 24%; animation-duration: 9.5s; animation-delay: 0.5s;">Y</div>
        <div class="floating-item" style="left: 31%; animation-duration: 10s; animation-delay: 2s;">🎂</div>
        <div class="floating-item" style="left: 38%; animation-duration: 11.5s; animation-delay: 1.5s;">B</div>
        <div class="floating-item" style="left: 43%; animation-duration: 8.5s; animation-delay: 3.5s;">I</div>
        <div class="floating-item" style="left: 48%; animation-duration: 10s; animation-delay: 0.8s;">R</div>
        <div class="floating-item" style="left: 53%; animation-duration: 9s; animation-delay: 2.2s;">T</div>
        <div class="floating-item" style="left: 58%; animation-duration: 10.5s; animation-delay: 1.2s;">H</div>
        <div class="floating-item" style="left: 63%; animation-duration: 8.5s; animation-delay: 0.2s;">D</div>
        <div class="floating-item" style="left: 68%; animation-duration: 11s; animation-delay: 2.8s;">A</div>
        <div class="floating-item" style="left: 73%; animation-duration: 9.2s; animation-delay: 1.8s;">Y</div>
        <div class="floating-item" style="left: 80%; animation-duration: 10.5s; animation-delay: 0.5s;">🎆</div>
        <div class="floating-item" style="left: 86%; animation-duration: 8s; animation-delay: 2.5s;">I</div>
        <div class="floating-item" style="left: 91%; animation-duration: 11.5s; animation-delay: 1.1s;">R</div>
        <div class="floating-item" style="left: 95%; animation-duration: 9s; animation-delay: 3.2s;">M</div>
        <div class="floating-item" style="left: 98%; animation-duration: 10.2s; animation-delay: 0.7s;">A</div>
    </div>
"""

st.markdown(css_template, unsafe_allow_html=True)

# --- SISTEM INTRO BOM / SURPRISE PEMBUKA ---
if 'intro_opened' not in st.session_state:
    st.session_state['intro_opened'] = False

if not st.session_state['intro_opened']:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: #ffffff; padding: 30px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.12); border: 3px solid #0284c7;">
            <h2 style="color: #0369a1; font-family: 'Georgia', serif; font-size: 1.5em; margin-bottom: 15px;">
                🚨 PERINGATAN SISTEM: Ada Kiriman Kejutan Spesial! 🎁
            </h2>
            <p style="color: #334155; font-size: 1.05em; font-weight: 600; margin-bottom: 20px;">
                Ssst... Terdeteksi sinyal kejutan ulang tahun buat <b>Irma Kristiani Ginting</b>. Tekan tombol di bawah untuk meledakkan kejutannya! 💥
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("💣 LEDAKKAN KEJUTAN SEKARANG"):
        intro_placeholder = st.empty()
        intro_placeholder.markdown("""
            <div style="text-align: center; padding: 40px;">
                <div class="fireworks-container">💣 💥 🎆 🎇 ✨</div>
                <h2 style="color: #0369a1; margin-top: 15px;">SELAMAT ULANG TAHUN IRMA KRISTIANI GINTING! 🎉</h2>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(2.2)
        intro_placeholder.empty()
        
        st.session_state['intro_opened'] = True
        st.rerun()

else:
    # --- HALAMAN UTAMA SETELAH INTRO BOM DIBUKA ---
    
    if 'welcomed_irma' not in st.session_state:
        st.balloons()
        st.session_state['welcomed_irma'] = True

    # Header Utama
    st.markdown("<h1 class='romantic-title'>Happy Birthday Irma Kristiani Ginting! 🎂💙</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>A very special day for a very special person! ✨</p>", unsafe_allow_html=True)

    # --- 1. SOUNDTRACK ULANG TAHUN (POSISI DI ATAS) ---
    url_lagu_irma = "https://www.youtube.com/watch?v=4oxarzdbEuw" 

    st.markdown("<div class='love-card'><h3>🎵 Soundtrack Ulang Tahun</h3><p>Lagu spesial penuh berkat untuk menemani harimu:</p>", unsafe_allow_html=True)
    st.markdown("**♪ Happy Birthday Tuhan Berkati — Maranatha Singer**")
    st.video(url_lagu_irma)



    # --- 2. UCAPAN & SURAT SPESIAL UNTUK GURU ---
    st.markdown("<div class='love-card'><h3>💌 Pesan Spesial Hari Ini</h3>", unsafe_allow_html=True)
    st.markdown("<h4>Selamat Ulang Tahun, Irma! 🥳</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div class='message-box'>
        Halo, Irma Kristiani Ginting! Selamat ulang tahun ya! 🎂💙<br><br>
        Di hari spesial ini, aku cuma mau ngucapin doa terbaik buat kamu. Semoga panjang umur, sehat selalu, dan apa pun impian serta urusanmu tahun ini dilancarkan sama Tuhan.<br><br>
        Hebat banget ya, di usiamu yang sekarang kamu sudah menjalani peran yang luar biasa sebagai seorang guru. Terima kasih sudah sabar dan berdedikasi mengajar serta menginspirasi banyak orang. Bukan cuma hebat dalam mendidik, kamu juga selalu tampil anggun, cantik, rapi, dan membawa energi positif ke mana pun kamu pergi.<br><br>
        Tetap jadi diri sendiri yang luar biasa, ya. Semoga hari-harimu ke depan makin banyak senyumnya dan dijauhkan dari hal-hal yang bikin capek. Have a wonderful birthday! like you
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- 3. FOTO SPESIAL IRMA ---
    st.markdown("<div class='love-card'><h3>📸 Spesial Untukmu Hari Ini</h3>", unsafe_allow_html=True)

    if os.path.exists("foto_irma.jpeg"):
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image("foto_irma.jpeg", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.9em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
    elif os.path.exists("foto_irma.jpg"):
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image("foto_irma.jpg", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.9em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
    elif os.path.exists("foto_irma.png"):
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image("foto_irma.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<p style="font-weight: 600; color: #0369a1; font-style: italic; font-size: 0.9em;">"Senyuman terbaik untuk hari yang luar biasa. Stay wonderful, Irma!" 💙</p>', unsafe_allow_html=True)
    else:
        st.info("💡 Letakkan foto dengan nama 'foto_irma.jpeg' di GitHub agar fotonya tampil di sini ya!")

    st.markdown("</div>", unsafe_allow_html=True)

    # --- 4. KOTAK KADO DENGAN VIDEO UCAPAN YOUTUBE ---
    st.markdown("<div class='love-card'><h3>🎁 Kotak Kado Kejutan Rahasia</h3><p>Ssst... Ada video ucapan spesial khusus buat kamu di dalam kado ini. Coba klik tombolnya:</p>", unsafe_allow_html=True)

    if 'open_gift' not in st.session_state:
        st.session_state['open_gift'] = False

    if not st.session_state['open_gift']:
        if st.button("🎆 Nyalakan Pesta Kembang Api & Buka Kejutan"):
            firework_placeholder = st.empty()
            firework_placeholder.markdown("""
                <div style="text-align: center; padding: 15px;">
                    <div class="fireworks-container">🎆 🎇 ✨ 🌟 💥</div>
                    <p style="color: #0369a1; font-weight: bold; margin-top: 5px;">Mempersiapkan video kejutan untuk Irma...</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1.8)
            firework_placeholder.empty()
            
            st.session_state['open_gift'] = True
            st.rerun()
    else:
        st.balloons()
        st.markdown("""
            <div style="text-align: center; padding: 10px;">
                <div class="fireworks-container">🎇 🎆 💖 🌟 🎆 🎇</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Link Video Ucapan Selamat Ulang Tahun dari YouTube
        url_video_ucapan_kado = "https://www.youtube.com/watch?v=DwpDkQRDfvI"
        
        st.markdown("""
            <div style="background: linear-gradient(135deg, #0284c7 100%, #0369a1 0%); padding: 16px; border-radius: 12px; color: #ffffff; text-align: center; box-shadow: 0 4px 16px rgba(2,132,199,0.3); margin-bottom: 12px;">
                <h3 style="margin-bottom: 6px; color: #fde047 !important; font-size: 1.1em !important;">🎉 SPESIAL VIDEO UCAPAN ULANG TAHUN 🎉</h3>
                <p style="font-size: 0.9em; font-weight: 600; color: #f8fafc !important; margin-bottom: 10px;">
                    Tonton video ucapan spesial ini sampai habis ya, Irma! ✨
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.video(url_video_ucapan_kado)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- 5. KONFIRMASI WHATSAPP ---
    st.markdown("<div class='love-card'><h3>✅ Konfirmasi ke Zefanya</h3><p>Udah buka kejutannya? Kirim kabar ke WhatsApp Zefanya yuk:</p>", unsafe_allow_html=True)
    nomor_wa = "6281216464994" 
    pesan_wa = "Halo Zefanya, makasih banyak ya buat video kejutan ulang tahunnya! Keren banget! 🎉✨"
    link_wa = f"https://wa.me/{nomor_wa}?text={pesan_wa.replace(' ', '%20')}"

    st.markdown(f"""
        <a href="{link_wa}" target="_blank">
            <button style="width: 100%; background-color: #22c55e; color: white; padding: 10px 16px; border: none; border-radius: 10px; font-weight: 700; font-size: 14px; cursor: pointer;">
                📲 Kirim Ucapan Terima Kasih via WhatsApp
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
            st.info("Sistem video kado YouTube berjalan sempurna!")
        elif pin_input:
            st.error("PIN salah.")

    # Footer
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #0369a1; font-size: 0.8em; font-weight: bold;'>Created with pure sincerity for Irma Kristiani Ginting's Birthday 🎂💙</p>", unsafe_allow_html=True)
