import streamlit as st
import pandas as pd
import datetime
from supabase import create_client, Client

# --- SAYFA AYARLARI VE BAŞLIK ---
st.set_page_config(page_title="RTP Performans Paneli", page_icon="⚽", layout="wide")

# --- SUPABASE BAĞLANTISI ---
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
except Exception as e:
    st.error("Veritabanı bağlantı ayarları eksik. Lütfen Streamlit Secrets bölümünü kontrol edin.")

st.title("🏥 Tesis Performans, Planlama & RTP Yönetim Sistemi")
st.markdown("İzokinetik, NordBord, ForceFrame ve Haftalık/Günlük Periyotlama Entegre Sistemi")

# --- GEÇİCİ HAFIZA (Planlamalar için) ---
if 'haftalik_planlar' not in st.session_state:
    st.session_state.haftalik_planlar = []
if 'gunluk_planlar' not in st.session_state:
    st.session_state.gunluk_planlar = []

# --- YAN MENÜ (NAVİGASYON) ---
st.sidebar.header("📋 Menü")
menu = st.sidebar.radio("İşlem Seçin:", [
    "1️⃣ Ana Panel (Dashboard)", 
    "2️⃣ Haftalık Antrenman Planlama 🗓️",
    "3️⃣ Günlük İdman/Drill Planlama 📝",
    "4️⃣ Günlük Yük ve Ağrı Girişi (Gerçekleşen)", 
    "5️⃣ Bi-Weekly (2 Haftalık) Test", 
    "6️⃣ Aylık İzokinetik Test"
])

oyuncular = ["Ahmet Yılmaz", "Mehmet Demir", "Can Ercan", "Ademcan Salep"]
secilen_oyuncu = st.sidebar.selectbox("Oyuncu Seç:", oyuncular)
tarih = st.sidebar.date_input("Tarih", datetime.date.today())

# --- TRAFİK LAMBASI ALGORİTMASI ---
def durum_hesapla(vas, asimetri, hq_oran):
    if vas >= 3 or asimetri >= 15:
        return "🟥 ALARM", "ACİL DURUM: Sahaya çıkışı durdurun. Yükü %50 azaltın ve kliniğe geri dönün.", "error"
    elif (1 <= vas <= 2) or (10 <= asimetri < 15):
        return "🟨 KONTROLLÜ", "DİKKAT: Mevcut RTP aşamasında kalın. HSR ve Yön Değiştirme hacmini sabitleyin.", "warning"
    elif vas == 0 and asimetri < 10 and hq_oran >= 0.60:
        return "🟩 TAM UYGUN", "ONAY: Oyuncu bir sonraki aşamaya geçebilir. HSR ve Sprint hacmi %15-20 artırılabilir.", "success"
    else:
        return "⬜ BİLGİ BEKLENİYOR", "Durum stabil, test verileri normal sınırlar içinde.", "info"

# --- MODÜLLER / SAYFALAR ---

# 1. ANA PANEL (DASHBOARD)
if menu == "1️⃣ Ana Panel (Dashboard)":
    st.header(f"📊 {secilen_oyuncu} - Genel Durum ve Takip")
    
    # Supabase'den Son Verileri Çekme
    try:
        response = supabase.table("ÇIRPICI").select("*").eq("oyuncu_adi", secilen_oyuncu).execute()
        veriler = response.data
        
        if veriler:
            df = pd.DataFrame(veriler)
            # En son girilen veriyi alalım
            son_veri = df.iloc[-1]
            guncel_vas = son_veri.get('vas_skoru', 0)
            guncel_asimetri = son_veri.get('asimetri_yuzdesi', 0.0)
            guncel_hq = son_veri.get('hq_orani', 0.60)
            
            st.markdown("### 🚦 Algoritma Kararı (Son Teste Göre)")
            durum_baslik, durum_mesaji, alert_type = durum_hesapla(guncel_vas, guncel_asimetri, guncel_hq)
            
            if alert_type == "error": st.error(f"**{durum_baslik}** \n\n {durum_mesaji}")
            elif alert_type == "warning": st.warning(f"**{durum_baslik}** \n\n {durum_mesaji}")
            elif alert_type == "success": st.success(f"**{durum_baslik}** \n\n {durum_mesaji}")
            else: st.info(f"**{durum_baslik}** \n\n {durum_mesaji}")
            
            st.markdown("---")
            st.markdown("### 🗄️ Oyuncunun Tüm Test Geçmişi")
            df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%d-%m-%Y %H:%M')
            st.dataframe(df[["created_at", "test_turu", "vas_skoru", "asimetri_yuzdesi", "hq_orani"]], use_container_width=True)
            
        else:
            st.info("Bu oyuncuya ait henüz Supabase veritabanında test sonucu bulunmuyor.")
    except Exception as e:
        st.error(f"Veri çekme hatası: {e}")

# 2. HAFTALIK ANTRENMAN PLANLAMA
elif menu == "2️⃣ Haftalık Antrenman Planlama 🗓️":
    st.header("🗓️ Haftalık Mikroçevrim (Periyotlama) Tasarımı")
    with st.form("haftalik_plan_form"):
        hafta_no = st.text_input("Hafta Tanımı (Örn: Hafta 2 - RTP Faz 2)")
        genel_odak = st.selectbox("Haftalık Ana Odak", ["Kuvvet & Hipertrofi", "Nöromüsküler Güç / Hız", "Saha Taktik", "RTP - Klinik Aşama"])
        pzt = st.text_input("Pazartesi", "Gym: Eksantrik Odak + Saha: Doğrusal Koşular")
        sal = st.text_input("Salı", "Saha: Geniş Alan Oyunları (Hedef Yüksek Mesafe)")
        hedef_haftalik_hsr = st.number_input("Hedef Toplam Haftalık HSR (Metre)", 0, 10000, 1500)
        
        submit = st.form_submit_button("Haftalık Planı Kaydet (Panele Gönder)")
        if submit:
            st.session_state.haftalik_planlar.append({"Hafta": hafta_no, "Odak": genel_odak, "Hedef HSR": hedef_haftalik_hsr})
            st.success("Haftalık plan oturuma kaydedildi!")

# 3. GÜNLÜK İDMAN/DRILL PLANLAMA
elif menu == "3️⃣ Günlük İdman/Drill Planlama 📝":
    st.header("📝 Günlük Detaylı Antrenman ve Drill Programlama")
    with st.form("gunluk_plan_form"):
        idman_tipi = st.selectbox("Antrenman Türü", ["Saha İdmanı", "Gym / Kuvvet Seansı", "Kombine", "Rehab"])
        isinma = st.text_area("Isınma (RAMP)", "10 dk Dinamik Esneme + Bant Çalışmaları")
        ana_bolum = st.text_area("Ana Bölüm", "3x5 Trapbar Deadlift (%80 1RM)")
        
        c1, c2 = st.columns(2)
        with c1: hedef_mesafe = st.number_input("Target Toplam Mesafe (m)", 0, 15000, 4500)
        with c2: hedef_hsr = st.number_input("Target HSR Mesafe (>19.8 km/s) (m)", 0, 2000, 300)
        
        submit = st.form_submit_button("Günlük Planı Yayınla")
        if submit:
            st.session_state.gunluk_planlar.append({"Tarih": str(tarih), "Tür": idman_tipi, "Hedef Mesafe": hedef_mesafe})
            st.success("Günlük plan başarıyla oluşturuldu!")

# 4. GÜNLÜK YÜK VE AĞRI GİRİŞİ (GERÇEKLEŞEN)
elif menu == "4️⃣ Günlük Yük ve Ağrı Girişi (Gerçekleşen)":
    st.header("🏃‍♂️ Gerçekleşen Antrenman Yükü ve Sporcu Yanıtı")
    with st.form("gunluk_form"):
        st.markdown("**Bu veriler Supabase ÇIRPICI tablosuna kaydedilir:**")
        vas_agri = st.slider("Antrenman Sonrası Ağrı (VAS 0-10)", 0, 10, 0)
        gerceklesen_mesafe = st.number_input("Gerçekleşen Toplam Mesafe (Metre)", 0, 15000, 4200)
        s_rpe = st.slider("Seans RPE (Zorluk 1-10)", 1, 10, 5)
        
        submit = st.form_submit_button("Gerçekleşen Veriyi Veritabanına Yaz")
        if submit:
            yeni_veri = {
                "oyuncu_adi": secilen_oyuncu,
                "test_turu": "Günlük İdman Yükü",
                "vas_skoru": vas_agri,
                "asimetri_yuzdesi": 0.0,
                "hq_orani": 0.0
            }
            supabase.table("ÇIRPICI").insert(yeni_veri).execute()
            st.success("Günlük dış yük ve iç yük başarıyla Supabase'e işlendi.")

# 5. Bİ-WEEKLY TEST GİRİŞİ
elif menu == "5️⃣ Bi-Weekly (2 Haftalık) Test":
    st.header("⚖️ 2 Haftalık Nöromüsküler Batarya")
    with st.form("biweekly_form"):
        st.subheader("ForceFrame & NordBord")
        test_cihazi = st.selectbox("Cihaz Seçimi", ["ForceFrame (Kasık)", "NordBord (Hamstring)"])
        asimetri_degeri = st.number_input("Kuvvet Asimetrisi (%)", 0.0, 50.0, value=7.0, format="%.1f")
        vas_skoru = st.slider("Test Sırası VAS Skoru", 0, 10, 0)
        
        submit = st.form_submit_button("Test Sonuçlarını Veritabanına Kaydet")
        if submit:
            yeni_veri = {
                "oyuncu_adi": secilen_oyuncu,
                "test_turu": test_cihazi,
                "vas_skoru": vas_skoru,
                "asimetri_yuzdesi": asimetri_degeri,
                "hq_orani": 0.0
            }
            supabase.table("ÇIRPICI").insert(yeni_veri).execute()
            st.success(f"{test_cihazi} verileri başarıyla Supabase'e güncellendi.")

# 6. AYLIK İZOKİNETİK TEST GİRİŞİ
elif menu == "6️⃣ Aylık İzokinetik Test":
    st.header("🔬 Aylık İzokinetik Dinamometre Testi (Aşama Geçişi)")
    with st.form("izokinetik_form"):
        q_torque = st.number_input("Quadriceps Peak Torque (Nm)", 0, 500, 250)
        h_torque = st.number_input("Hamstring Peak Torque (Nm)", 0, 500, 160)
        
        hq_ratio = h_torque / q_torque if q_torque > 0 else 0.0
        st.info(f"Hesaplanan Konvansiyonel H:Q Oranı: **{hq_ratio:.2f}** (İdeal: >0.60)")
        
        submit = st.form_submit_button("İzokinetik Onayını Veritabanına Kaydet")
        if submit:
            yeni_veri = {
                "oyuncu_adi": secilen_oyuncu,
                "test_turu": "İzokinetik (60°/s)",
                "vas_skoru": 0,
                "asimetri_yuzdesi": 0.0,
                "hq_orani": float(hq_ratio)
            }
            supabase.table("ÇIRPICI").insert(yeni_veri).execute()
            st.success("İzokinetik test veritabanına BAŞARIYLA işlendi!")
