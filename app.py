import streamlit as st
import pandas as pd
from supabase import create_client, Client

st.set_page_config(page_title="Florya RTP Sistemi", page_icon="⚽", layout="wide")

# --- 1. SUPABASE BAĞLANTISI ---
# Streamlit Secrets'a girdiğin anahtarları çekiyoruz
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

st.title("🏥 Florya As Spor Kulübü - RTP Veri Sistemi")

# --- 2. MENÜ YAPISI ---
menu = st.sidebar.radio("Menü", ["📝 Veri Girişi (Yeni Test)", "📊 Oyuncu Durum Paneli"])

# --- 3. VERİ GİRİŞ SAYFASI (VERİTABANINA YAZMA) ---
if menu == "📝 Veri Girişi (Yeni Test)":
    st.header("Yeni Test Sonucu Ekle")
    st.markdown("Buradan girilen veriler anında Supabase veritabanına kaydedilir.")
    
    with st.form("test_formu"):
        oyuncu_adi = st.text_input("Oyuncu Adı Soyadı")
        test_turu = st.selectbox("Test Türü", ["ForceDecks (CMJ/Frenleme)", "NordBord (Hamstring)", "ForceFrame (Kasık)", "İzokinetik (Aylık)"])
        vas_skoru = st.slider("VAS Ağrı Skoru (0-10)", 0, 10, 0)
        asimetri_yuzdesi = st.number_input("Asimetri Yüzdesi (%)", 0.0, 50.0, 0.0, format="%.1f")
        hq_orani = st.number_input("İzokinetik H:Q Oranı (Sadece İzokinetik ise girin)", 0.0, 2.0, 0.0, format="%.2f")
        
        kaydet = st.form_submit_button("Veritabanına Kaydet")
        
        if kaydet:
            # Supabase'e gönderilecek veri paketi (Kolon isimleri tablodakilerle birebir aynı!)
            yeni_veri = {
                "oyuncu_adi": oyuncu_adi,
                "test_turu": test_turu,
                "vas_skoru": vas_skoru,
                "asimetri_yuzdesi": asimetri_yuzdesi,
                "hq_orani": hq_orani
            }
            
            # Veriyi ÇIRPICI tablosuna yazıyoruz
            try:
                supabase.table("ÇIRPICI").insert(yeni_veri).execute()
                st.success("✅ Veri başarıyla buluta kaydedildi!")
            except Exception as e:
                st.error(f"Kayıt sırasında bir hata oluştu: {e}")

# --- 4. DASHBOARD SAYFASI (VERİTABANINDAN OKUMA) ---
elif menu == "📊 Oyuncu Durum Paneli":
    st.header("Güncel Test Sonuçları Veritabanı")
    
    try:
        # ÇIRPICI tablosundaki tüm verileri çekiyoruz
        response = supabase.table("ÇIRPICI").select("*").execute()
        veriler = response.data
        
        if veriler:
            df = pd.DataFrame(veriler)
            # Tarih formatını düzeltme
            df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%d-%m-%Y %H:%M')
            
            # Tabloyu ekrana basma (İstediğimiz sırayla)
            st.dataframe(df[["created_at", "oyuncu_adi", "test_turu", "vas_skoru", "asimetri_yuzdesi", "hq_orani"]], use_container_width=True)
            
            # Basit bir uyarı mekanizması
            st.markdown("### 🚨 Kritik Eşik Uyarıları")
            for index, row in df.iterrows():
                if row['asimetri_yuzdesi'] > 10.0:
                    st.warning(f"⚠️ **{row['oyuncu_adi']}** - {row['test_turu']} testinde asimetri çok yüksek (%{row['asimetri_yuzdesi']}).")
                if row['vas_skoru'] >= 3:
                    st.error(f"🛑 **{row['oyuncu_adi']}** - Ağrı skoru çok yüksek (VAS: {row['vas_skoru']}). Antrenman yükü düşürülmeli.")
        else:
            st.info("Sisteme henüz hiç test verisi girilmemiş.")
            
    except Exception as e:
        st.error(f"Veriler çekilirken bir hata oluştu: {e}")
