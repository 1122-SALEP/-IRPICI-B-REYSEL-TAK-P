import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json

# Sayfa yapılandırması
st.set_page_config(
    page_title="Spor Yaralanması Rehab Takip Sistemi",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Türkçe başlık
st.title("🏥 Spor Yaralanması Rehabilitasyon Takip Sistemi")
st.markdown("Profesyonel Futbolcuların Yaralanma Sonrası Geri Dönüş (Return to Play) Protokolü")

# Sidebar - Navigasyon
st.sidebar.header("📋 Menü")
page = st.sidebar.radio(
    "Sayfa Seç:",
    ["Ana Panel", "Oyuncu Profili", "İzokinetik Test", "Haftalık Plan", "Günlük Antrenman", "İstatistikler"]
)

# Demo verisi - Oyuncuları sakla
if "players" not in st.session_state:
    st.session_state.players = {
        "p001": {
            "id": "p001",
            "name": "Ercan Kaya",
            "age": 28,
            "position": "Orta Saha",
            "injuryType": "Ön Çapraz Bağ (ACL)",
            "surgeryDate": "2024-06-15",
            "phase": 1,
            "vasPain": 7.5,
            "yBalanceAsymmetry": 8.2,
            "nordbordForceDrop": 15.5,
            "adductionsAbductionsRatio": 0.72,
            "quadricepsPeakTorque": 250,
            "hamstringPeakTorque": 160,
            "quadricepsPeakTorque180": 170,
            "hamstringPeakTorque180": 120,
            "quadricepsPeakTorque300": 110,
            "hamstringPeakTorque300": 88,
            "hqRatio": 0.64,
            "hqRatio60": 0.64,
            "hqRatio180": 0.71,
            "hqRatio300": 0.80
        }
    }

# ============= ANA PANEL =============
if page == "Ana Panel":
    st.header("📊 Genel Durum Paneli")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("👥 Takip Edilen Oyuncular", len(st.session_state.players))
    with col2:
        st.metric("🏥 Aktif Yaralanmalar", 1)
    with col3:
        st.metric("✅ İyileşen Oyuncular", len(st.session_state.players) - 1 if len(st.session_state.players) > 1 else 0)
    
    st.divider()
    
    st.subheader("📈 Oyuncu Durumu Özeti")
    
    for player_id, player in st.session_state.players.items():
        with st.container(border=True):
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.write(f"**{player['name']}**")
                st.caption(f"Pos: {player['position']}")
            
            with col2:
                st.write(f"**Aşama:** {player['phase']}")
                st.caption(f"Yaralanma: {player['injuryType']}")
            
            with col3:
                st.write(f"**Ağrı (VAS):** {player['vasPain']}/10")
                if player['vasPain'] > 5:
                    st.caption("🔴 Yüksek ağrı")
                else:
                    st.caption("🟢 Kontrol altında")
            
            with col4:
                st.write(f"**H:Q Ratio:** {player['hqRatio']:.2f}")
                if player['hqRatio'] >= 0.60:
                    st.caption("✅ Uygun")
                else:
                    st.caption("⚠️ Düşük")
            
            with col5:
                if st.button("📋 Detay", key=f"detail_{player_id}"):
                    st.session_state.selected_player = player_id

# ============= OYUNCU PROFİLİ =============
elif page == "Oyuncu Profili":
    st.header("👤 Oyuncu Profili")
    
    if st.session_state.players:
        player_name = st.selectbox(
            "Oyuncu Seç:",
            list(st.session_state.players.values()),
            format_func=lambda x: x["name"]
        )
        
        player = player_name
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Temel Bilgiler")
            st.write(f"**Adı:** {player['name']}")
            st.write(f"**Yaşı:** {player['age']}")
            st.write(f"**Pozisyon:** {player['position']}")
            st.write(f"**Yaralanma Türü:** {player['injuryType']}")
            st.write(f"**Ameliyat Tarihi:** {player['surgeryDate']}")
            st.write(f"**Rehabilitasyon Aşaması:** {player['phase']}/6")
        
        with col2:
            st.subheader("📊 Haftalık Metrikler")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("VAS Ağrı Skoru", f"{player['vasPain']:.1f}/10")
                st.metric("Y-Balance Asimetrisi", f"{player['yBalanceAsymmetry']:.1f}%")
            
            with col_b:
                st.metric("Nordborg Kuvvet Düşüşü", f"{player['nordbordForceDrop']:.1f}%")
                st.metric("Addüksiyon/Abdüksiyon Oranı", f"{player['adductionsAbductionsRatio']:.2f}")
        
        st.divider()
        
        st.subheader("💪 İzokinetik Test Sonuçları")
        
        tab1, tab2, tab3 = st.tabs(["60°/s (Kuvvet)", "180°/s (Güç)", "300°/s (Dayanıklılık)"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Quadriceps Peak Torque", f"{player['quadricepsPeakTorque']} Nm")
            with col2:
                st.metric("Hamstring Peak Torque", f"{player['hamstringPeakTorque']} Nm")
            with col3:
                hq = player['hqRatio60'] if 'hqRatio60' in player else player['hamstringPeakTorque'] / player['quadricepsPeakTorque']
                st.metric("H:Q Ratio", f"{hq:.2f}", delta="✅ Uygun" if hq >= 0.60 else "⚠️ Düşük")
        
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Quadriceps Peak Torque", f"{player['quadricepsPeakTorque180']} Nm")
            with col2:
                st.metric("Hamstring Peak Torque", f"{player['hamstringPeakTorque180']} Nm")
            with col3:
                hq = player['hqRatio180'] if 'hqRatio180' in player else player['hamstringPeakTorque180'] / player['quadricepsPeakTorque180']
                st.metric("H:Q Ratio", f"{hq:.2f}", delta="✅ Uygun" if hq >= 0.70 else "⚠️ Düşük")
        
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Quadriceps Peak Torque", f"{player['quadricepsPeakTorque300']} Nm")
            with col2:
                st.metric("Hamstring Peak Torque", f"{player['hamstringPeakTorque300']} Nm")
            with col3:
                hq = player['hqRatio300'] if 'hqRatio300' in player else player['hamstringPeakTorque300'] / player['quadricepsPeakTorque300']
                st.metric("H:Q Ratio", f"{hq:.2f}", delta="✅ Uygun" if hq >= 0.80 else "⚠️ Düşük")

# ============= İZOKİNETİK TEST =============
elif page == "İzokinetik Test":
    st.header("🔬 Aylık İzokinetik Dinamometre Testi")
    
    if st.session_state.players:
        player_name = st.selectbox(
            "Oyuncu Seç:",
            list(st.session_state.players.values()),
            format_func=lambda x: x["name"],
            key="iso_player"
        )
        
        player = player_name
        
        st.info(f"📊 {player['name']} için H:Q Oran Analizi (60°/s, 180°/s, 300°/s)")
        
        tab1, tab2, tab3 = st.tabs(["60°/s (Strength)", "180°/s (Power)", "300°/s (Endurance)"])
        
        with tab1:
            st.subheader("Düşük Açısal Hız — Maksimal Kuvvet")
            col1, col2 = st.columns(2)
            
            with col1:
                q_torque = st.slider("Quadriceps Peak Torque (Nm)", 0, 500, player['quadricepsPeakTorque'], key="q60")
            with col2:
                h_torque = st.slider("Hamstring Peak Torque (Nm)", 0, 500, player['hamstringPeakTorque'], key="h60")
            
            hq = h_torque / q_torque if q_torque > 0 else 0
            
            col_result1, col_result2 = st.columns(2)
            with col_result1:
                st.metric("H:Q Ratio @ 60°/s", f"{hq:.2f}")
            with col_result2:
                if hq >= 0.60:
                    st.success("✅ Referans eşiğinin üzerinde")
                else:
                    st.warning("⚠️ Referans eşiğinin altında")
        
        with tab2:
            st.subheader("Orta Açısal Hız — Patlayıcı Güç")
            col1, col2 = st.columns(2)
            
            with col1:
                q_torque = st.slider("Quadriceps Peak Torque (Nm)", 0, 400, player['quadricepsPeakTorque180'], key="q180")
            with col2:
                h_torque = st.slider("Hamstring Peak Torque (Nm)", 0, 400, player['hamstringPeakTorque180'], key="h180")
            
            hq = h_torque / q_torque if q_torque > 0 else 0
            
            col_result1, col_result2 = st.columns(2)
            with col_result1:
                st.metric("H:Q Ratio @ 180°/s", f"{hq:.2f}")
            with col_result2:
                if hq >= 0.70:
                    st.success("✅ Referans eşiğinin üzerinde")
                else:
                    st.warning("⚠️ Referans eşiğinin altında")
        
        with tab3:
            st.subheader("Yüksek Açısal Hız — Dayanıklılık")
            col1, col2 = st.columns(2)
            
            with col1:
                q_torque = st.slider("Quadriceps Peak Torque (Nm)", 0, 300, player['quadricepsPeakTorque300'], key="q300")
            with col2:
                h_torque = st.slider("Hamstring Peak Torque (Nm)", 0, 300, player['hamstringPeakTorque300'], key="h300")
            
            hq = h_torque / q_torque if q_torque > 0 else 0
            
            col_result1, col_result2 = st.columns(2)
            with col_result1:
                st.metric("H:Q Ratio @ 300°/s", f"{hq:.2f}")
            with col_result2:
                if hq >= 0.80:
                    st.success("✅ Referans eşiğinin üzerinde")
                else:
                    st.warning("⚠️ Referans eşiğinin altında")

# ============= HAFTALIK PLAN =============
elif page == "Haftalık Plan":
    st.header("📅 Haftalık Rehabilitasyon Planı")
    
    st.info("""
    **Aşama 1 - İlk 2 Hafta (Post-Op):** Ağrı kontrolü, şişlik azaltma, ROM artışı
    
    **Aşama 2 - Haftalar 3-4:** Kas güçlendirme başlangıcı, proprioseptif eğitim
    
    **Aşama 3 - Haftalar 5-8:** Dinamik denge, single-leg egzersizler
    
    **Aşama 4 - Haftalar 9-12:** Pliometrik eğitim, sprint hızı
    
    **Aşama 5 - Haftalar 13-16:** Pozisyon spesifik teknikler
    
    **Aşama 6 - Haftalar 17+:** Saha geçiş, full training
    """)

# ============= GÜNLÜK ANTRENMAN =============
elif page == "Günlük Antrenman":
    st.header("🏋️ Günlük Antrenman Planı")
    
    st.subheader("Örnek Günlük Seansı")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**1-) Isınma & Mobilizasyon (RAMP)**")
        st.write("- Light Cardio: 5 min (treadmill/bike)")
        st.write("- Dynamic Stretching: 5-7 min")
        st.write("- Movement Preparation: 5-10 min")
    
    with col2:
        st.write("**2-) Core-Aktivasyon**")
        st.write("- Planks: 3x20-30 sec")
        st.write("- Bird Dogs: 3x10 each side")
        st.write("- Clamshells: 3x15 each side")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**3-) Pliometri ve SAQ**")
        st.write("- Double Leg Hops: 3x10")
        st.write("- Single Leg Hops: 3x8 each")
        st.write("- Lateral Bounds: 3x8 each")
    
    with col2:
        st.write("**4-) Direnç**")
        st.write("- Leg Press: 3x12 @ RPE 7/10")
        st.write("- Leg Curl: 3x12 @ RPE 7/10")
        st.write("- Adductor: 3x15")
        st.write("- Abductor: 3x15")
    
    st.divider()
    
    st.write("**5-) Metabolik**")
    st.write("- Cool-down + Static Stretching: 10 min")
    st.write("- Ice: 15 min (if needed)")

# ============= İSTATİSTİKLER =============
elif page == "İstatistikler":
    st.header("📈 İstatistik ve Grafik Analiz")
    
    st.info("Uzun vadeli ilerlemeyi takip etmek için aylık sonuçların karşılaştırması yapılabilir.")
    
    # Demo veri
    import matplotlib.pyplot as plt
    import numpy as np
    
    weeks = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    vas_pain = np.array([7.5, 7.2, 6.8, 6.2, 5.5, 4.8, 3.5, 2.2])
    hq_ratio = np.array([0.55, 0.57, 0.59, 0.61, 0.63, 0.65, 0.68, 0.72])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax1.plot(weeks, vas_pain, marker='o', color='red', linewidth=2, markersize=8)
    ax1.set_xlabel("Hafta")
    ax1.set_ylabel("VAS Ağrı Skoru")
    ax1.set_title("Ağrı Düzeyinin Haftalık Değişimi")
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 10)
    
    ax2.plot(weeks, hq_ratio, marker='s', color='green', linewidth=2, markersize=8)
    ax2.axhline(y=0.60, color='orange', linestyle='--', label='Referans (0.60)')
    ax2.set_xlabel("Hafta")
    ax2.set_ylabel("H:Q Ratio")
    ax2.set_title("H:Q Oranının Haftalık Değişimi")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    st.pyplot(fig)

st.divider()
st.caption("© 2024 Spor Yaralanması Rehab Takip Sistemi | Powered by Streamlit")
