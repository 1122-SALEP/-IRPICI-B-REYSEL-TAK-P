import React, { useState, useEffect } from "react";
import { Player } from "../types";
import { Activity, Save, ThumbsUp, ThumbsDown, ShieldAlert, BadgeCheck, Zap, Gauge, Flame } from "lucide-react";

interface IsokineticTestViewProps {
  selectedPlayer: Player;
  onUpdatePlayerMetrics: (playerId: string, metrics: Partial<Player>) => void;
}

export default function IsokineticTestView({
  selectedPlayer,
  onUpdatePlayerMetrics,
}: IsokineticTestViewProps) {
  const [qTorque60, setQTorque60] = useState(selectedPlayer.quadricepsPeakTorque || 250);
  const [hTorque60, setHTorque60] = useState(selectedPlayer.hamstringPeakTorque || 160);

  const [qTorque180, setQTorque180] = useState(selectedPlayer.quadricepsPeakTorque180 || 170);
  const [hTorque180, setHTorque180] = useState(selectedPlayer.hamstringPeakTorque180 || 120);

  const [qTorque300, setQTorque300] = useState(selectedPlayer.quadricepsPeakTorque300 || 110);
  const [hTorque300, setHTorque300] = useState(selectedPlayer.hamstringPeakTorque300 || 88);

  const [successMsg, setSuccessMsg] = useState("");

  useEffect(() => {
    setQTorque60(selectedPlayer.quadricepsPeakTorque || 250);
    setHTorque60(selectedPlayer.hamstringPeakTorque || 160);
    setQTorque180(selectedPlayer.quadricepsPeakTorque180 || 170);
    setHTorque180(selectedPlayer.hamstringPeakTorque180 || 120);
    setQTorque300(selectedPlayer.quadricepsPeakTorque300 || 110);
    setHTorque300(selectedPlayer.hamstringPeakTorque300 || 88);
  }, [selectedPlayer]);

  const hqRatio60 = qTorque60 > 0 ? hTorque60 / qTorque60 : 0;
  const hqRatio180 = qTorque180 > 0 ? hTorque180 / qTorque180 : 0;
  const hqRatio300 = qTorque300 > 0 ? hTorque300 / qTorque300 : 0;

  const isApproved60 = hqRatio60 >= 0.60;
  const isApproved180 = hqRatio180 >= 0.70;
  const isApproved300 = hqRatio300 >= 0.80;

  const isApproved = isApproved60 && isApproved180 && isApproved300;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    onUpdatePlayerMetrics(selectedPlayer.id, {
      hqRatio: parseFloat(hqRatio60.toFixed(2)), // core hqRatio uses the 60°/s standard
      quadricepsPeakTorque: qTorque60,
      hamstringPeakTorque: hTorque60,
      quadricepsPeakTorque180: qTorque180,
      hamstringPeakTorque180: hTorque180,
      quadricepsPeakTorque300: qTorque300,
      hamstringPeakTorque300: hTorque300,
      hqRatio60: parseFloat(hqRatio60.toFixed(2)),
      hqRatio180: parseFloat(hqRatio180.toFixed(2)),
      hqRatio300: parseFloat(hqRatio300.toFixed(2)),
    });

    if (isApproved) {
      setSuccessMsg("TÜM HIZLARDA İZOKİNETİK TEST BAŞARILI! Aşama geçiş vizesi verildi ve ana panele kaydedildi.");
    } else {
      setSuccessMsg("Sonuçlar Kaydedildi. UYARI: Bazı açısal hızlardaki H:Q oranları kritik referans eşiğinin altında kaldığı için tam vize verilmedi.");
    }
    setTimeout(() => setSuccessMsg(""), 6000);
  };

  return (
    <div className="space-y-6" id="isokinetic-test-view-root">
      {/* Header */}
      <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
        <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
          <Activity className="text-violet-600 h-6 w-6" />
          🔬 Aylık Çoklu Açısal Hız İzokinetik Dinamometre Testi (H:Q Oran Analizi)
        </h2>
        <p className="text-xs text-slate-500 mt-1">
          {selectedPlayer.name} için diz ekstansör/fleksör (Quadriceps / Hamstring) kas kuvvet dengesinin <strong>farklı açısal hızlardaki (60°/s, 180°/s, 300°/s)</strong> tepe tork (Peak Torque) ve H/Q oran analizi.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Form panel */}
        <div className="lg:col-span-2 bg-white p-6 rounded-2xl border border-slate-100 shadow-sm space-y-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            {successMsg && (
              <div className={`p-4 rounded-xl text-xs font-semibold animate-fade-in flex items-start gap-2.5 border ${
                isApproved 
                  ? "bg-emerald-50 border-emerald-200 text-emerald-800" 
                  : "bg-amber-50 border-amber-200 text-amber-800"
              }`}>
                {isApproved ? (
                  <BadgeCheck className="text-emerald-500 h-5 w-5 shrink-0" />
                ) : (
                  <ShieldAlert className="text-amber-500 h-5 w-5 shrink-0" />
                )}
                <span>{successMsg}</span>
              </div>
            )}

            {/* 60°/s - Strength */}
            <div className="border border-slate-100 rounded-2xl p-5 bg-slate-50/40 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                <h3 className="text-xs font-bold text-indigo-700 uppercase flex items-center gap-1.5">
                  <Gauge size={14} />
                  1) Düşük Açısal Hız (60°/s) — Maksimal Kuvvet / Strength
                </h3>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  isApproved60 ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"
                }`}>
                  H/Q: {hqRatio60.toFixed(2)} (Ref ≥ 0.60)
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Quadriceps Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="500"
                      value={qTorque60}
                      onChange={(e) => setQTorque60(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="50"
                      max="450"
                      step="5"
                      value={qTorque60}
                      onChange={(e) => setQTorque60(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-indigo-600 cursor-pointer"
                    />
                  </div>
                </div>

                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Hamstring Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="500"
                      value={hTorque60}
                      onChange={(e) => setHTorque60(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="50"
                      max="450"
                      step="5"
                      value={hTorque60}
                      onChange={(e) => setHTorque60(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-indigo-600 cursor-pointer"
                    />
                  </div>
                </div>
              </div>
            </div>

            {/* 180°/s - Power */}
            <div className="border border-slate-100 rounded-2xl p-5 bg-slate-50/40 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                <h3 className="text-xs font-bold text-amber-700 uppercase flex items-center gap-1.5">
                  <Zap size={14} />
                  2) Orta Açısal Hız (180°/s) — Patlayıcı Güç / Power
                </h3>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  isApproved180 ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"
                }`}>
                  H/Q: {hqRatio180.toFixed(2)} (Ref ≥ 0.70)
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Quadriceps Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="400"
                      value={qTorque180}
                      onChange={(e) => setQTorque180(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="30"
                      max="350"
                      step="5"
                      value={qTorque180}
                      onChange={(e) => setQTorque180(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-amber-500 cursor-pointer"
                    />
                  </div>
                </div>

                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Hamstring Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="400"
                      value={hTorque180}
                      onChange={(e) => setHTorque180(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="30"
                      max="350"
                      step="5"
                      value={hTorque180}
                      onChange={(e) => setHTorque180(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-amber-500 cursor-pointer"
                    />
                  </div>
                </div>
              </div>
            </div>

            {/* 300°/s - Endurance */}
            <div className="border border-slate-100 rounded-2xl p-5 bg-slate-50/40 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                <h3 className="text-xs font-bold text-rose-700 uppercase flex items-center gap-1.5">
                  <Flame size={14} />
                  3) Yüksek Açısal Hız (300°/s) — Hız ve Dayanıklılık / Endurance
                </h3>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  isApproved300 ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"
                }`}>
                  H/Q: {hqRatio300.toFixed(2)} (Ref ≥ 0.80)
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Quadriceps Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="300"
                      value={qTorque300}
                      onChange={(e) => setQTorque300(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="20"
                      max="250"
                      step="5"
                      value={qTorque300}
                      onChange={(e) => setQTorque300(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-rose-500 cursor-pointer"
                    />
                  </div>
                </div>

                <div className="bg-white p-3.5 rounded-xl border border-slate-100 space-y-2">
                  <label className="text-[11px] font-bold text-slate-600 uppercase block">Hamstring Peak Torque (Nm)</label>
                  <div className="flex items-center gap-3">
                    <input
                      type="number"
                      min="0"
                      max="300"
                      value={hTorque300}
                      onChange={(e) => setHTorque300(parseInt(e.target.value) || 0)}
                      className="w-16 text-xs bg-slate-50 border border-slate-200 rounded-lg p-1.5 font-extrabold text-center"
                    />
                    <input
                      type="range"
                      min="20"
                      max="250"
                      step="5"
                      value={hTorque300}
                      onChange={(e) => setHTorque300(parseInt(e.target.value) || 0)}
                      className="flex-1 accent-rose-500 cursor-pointer"
                    />
                  </div>
                </div>
              </div>
            </div>

            {/* Calculations Indicator */}
            <div className="bg-slate-50 p-5 rounded-2xl border border-slate-100 flex flex-col md:flex-row items-center justify-between gap-4">
              <div className="grid grid-cols-3 gap-6 w-full md:w-auto">
                <div className="text-center md:text-left">
                  <span className="text-[10px] text-slate-400 font-bold uppercase block">H/Q Ratio @ 60°/s</span>
                  <span className={`text-xl font-black font-mono ${isApproved60 ? "text-emerald-600" : "text-rose-600"}`}>
                    {hqRatio60.toFixed(2)}
                  </span>
                  <span className="text-[9px] text-slate-400 block">Maks. Kuvvet</span>
                </div>
                <div className="text-center md:text-left border-l border-slate-200 pl-4">
                  <span className="text-[10px] text-slate-400 font-bold uppercase block">H/Q Ratio @ 180°/s</span>
                  <span className={`text-xl font-black font-mono ${isApproved180 ? "text-emerald-600" : "text-rose-600"}`}>
                    {hqRatio180.toFixed(2)}
                  </span>
                  <span className="text-[9px] text-slate-400 block">Patlayıcı Güç</span>
                </div>
                <div className="text-center md:text-left border-l border-slate-200 pl-4">
                  <span className="text-[10px] text-slate-400 font-bold uppercase block">H/Q Ratio @ 300°/s</span>
                  <span className={`text-xl font-black font-mono ${isApproved300 ? "text-emerald-600" : "text-rose-600"}`}>
                    {hqRatio300.toFixed(2)}
                  </span>
                  <span className="text-[9px] text-slate-400 block">Direnç & Hız</span>
                </div>
              </div>

              {qTorque60 > 0 ? (
                isApproved ? (
                  <div className="bg-emerald-500/10 text-emerald-700 border border-emerald-500/20 rounded-xl p-3 flex items-center gap-2 shrink-0">
                    <ThumbsUp size={20} className="shrink-0" />
                    <div>
                      <span className="text-xs font-bold block">TÜMÜ UYGUN (VİZE)</span>
                      <span className="text-[10px] text-emerald-600 font-medium">Biyomekanik geçiş kriterleri tamamlandı.</span>
                    </div>
                  </div>
                ) : (
                  <div className="bg-amber-500/10 text-amber-700 border border-amber-500/20 rounded-xl p-3 flex items-center gap-2 shrink-0">
                    <ThumbsDown size={20} className="shrink-0" />
                    <div>
                      <span className="text-xs font-bold block">ENGEL VAR</span>
                      <span className="text-[10px] text-amber-600 font-medium">Zayıf H:Q oranı olan açıları güçlendirin.</span>
                    </div>
                  </div>
                )
              ) : (
                <div className="text-xs text-slate-400 italic">Veri girişi bekleniyor...</div>
              )}
            </div>

            <button
              type="submit"
              className="w-full bg-violet-600 hover:bg-violet-700 text-white font-bold py-3.5 px-4 rounded-xl shadow-xs transition flex items-center justify-center gap-2 text-sm cursor-pointer"
            >
              <Save size={18} />
              Tüm Açısal Hız Test Onaylarını Kaydet
            </button>
          </form>
        </div>

        {/* Clinical reference box */}
        <div className="bg-slate-50 p-5 rounded-2xl border border-slate-100 space-y-4">
          <h4 className="font-bold text-slate-800 text-xs uppercase tracking-wider">İzokinetik H:Q Klinik Standartları</h4>
          <div className="text-xs text-slate-600 space-y-4 leading-relaxed">
            <p>
              İzokinetik kas kuvveti testi, profesyonel sporcuların Return To Play (Saha Geçiş) protokollerinin "altın standart" vizesidir. Sadece Peak Torque (60°/s) değil, <strong>farklı açısal hızlardaki tork oranları</strong> da değerlendirilmelidir.
            </p>

            <div className="p-3 bg-white border border-slate-200/60 rounded-xl space-y-1">
              <span className="font-bold text-slate-800 text-[11px] block">🏎️ Açısal Hız Farklarının Önemi:</span>
              <p className="text-[11px] text-slate-500">
                Açısal hız arttıkça (60 → 180 → 300°/s) hem Quadriceps hem de Hamstring tepe torkları düşer. Ancak Quadriceps torku daha hızlı azaldığından, <strong>sağlıklı bir dizde H:Q oranı açısal hız arttıkça yükselmelidir</strong>.
              </p>
            </div>

            <div className="p-3 bg-white border border-slate-200/60 rounded-xl space-y-2">
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-indigo-500" />
                <span className="font-bold text-slate-800">60°/s Koşulu ≥ 0.60</span>
              </div>
              <p className="text-[11px] text-slate-500">
                Maksimal tork (kuvvet) dengesidir. Bu oranın 0.60 altında olması Hamstring gücünün yetersiz olduğunu gösterir.
              </p>
            </div>

            <div className="p-3 bg-white border border-slate-200/60 rounded-xl space-y-2">
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-amber-500" />
                <span className="font-bold text-slate-800">180°/s Koşulu ≥ 0.70</span>
              </div>
              <p className="text-[11px] text-slate-500">
                Patlayıcı güç hızı dengesidir. Koşu mekaniğinde hamstringin ani frenleme yükü için kritiktir.
              </p>
            </div>

            <div className="p-3 bg-white border border-slate-200/60 rounded-xl space-y-2">
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-rose-500" />
                <span className="font-bold text-slate-800">300°/s Koşulu ≥ 0.80</span>
              </div>
              <p className="text-[11px] text-slate-500">
                Yüksek hızlı kas dayanıklılığı dengesidir. Maksimal sprint hızlarındaki koruma potansiyeli bu oranla ölçülür.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
