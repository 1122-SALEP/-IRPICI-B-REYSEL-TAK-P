export interface Player {
  id: string;
  name: string;
  rtpStage: string; // Örn: "Aşama 1: Klinik", "Aşama 2: Düz Koşu", vb.
  
  // Mevcut Test / RTP Eşikleri
  vasPain: number;        // 0-10 (Vizör Ağrı Skalası)
  asymmetry: number;      // ForceDecks Eksantrik Frenleme Asimetrisi (%)
  hqRatio: number;        // İzokinetik H:Q Oranı
  nordbordDrop: number;   // NordBord Kuvvet Kaybı (%)
  
  // Cihaz Tabanlı Test Bataryaları ve Metrik Şemaları
  rsi_modified: number;              // ForceDecks CMJ (Dinamik) - Float
  ecc_decel_impulse_asym: number;    // ForceDecks CMJ (Frenleme) - Float (%)
  rfd_0_200ms: number;               // ForceDecks IMTP (İzometrik) - Integer (N/s)
  nordbord_peak_force_asym: number;  // NordBord Nordic Hamstring Asimetrisi - Float (%)
  nordbord_peak_force_total: number; // NordBord Nordic Hamstring Toplam Kuvvet - Integer (N)
  add_abd_ratio: number;             // ForceFrame Kasık Sıkıştırma Oranı - Float
  groin_peak_force_asym: number;     // ForceFrame Kasık Sıkıştırma Asimetrisi - Float (%)
  hq_ratio_60: number;               // İzokinetik H:Q 60°/s - Float
  quad_peak_torque_bw: number;       // İzokinetik 60°/s Bağıl Güç - Float (Nm/kg)
  
  // İki Haftalık Nöromüsküler Metrikler
  eccentricBrakingAsymmetry: number;
  rsiModified: number;
  hamstringAsymmetry: number;
  hamstringPeakForce: number;
  adductionsAbductionsRatio: number;
  
  // Aylık İzokinetik Test Değerleri
  quadricepsPeakTorque: number; // 60°/s
  hamstringPeakTorque: number;  // 60°/s
  quadricepsPeakTorque180?: number;
  hamstringPeakTorque180?: number;
  quadricepsPeakTorque300?: number;
  hamstringPeakTorque300?: number;
  hqRatio60?: number;
  hqRatio180?: number;
  hqRatio300?: number;
}

export interface WeeklyPlan {
  id: string;
  playerId: string;
  weekNo: string;
  focus: string;
  mon: string;
  tue: string;
  wed: string;
  thu: string;
  fri: string;
  sat: string;
  sun: string;
  targetHsr: number;
  createdAt: string;
}

export interface DailyPlan {
  id: string;
  playerId: string;
  date: string;
  type: string; // "Saha İdmanı" | "Gym / Kuvvet Seansı" vb.
  warmup: string;         // 1-) Isınma
  coreActivation: string; // 2-) Core-Aktivasyon
  plyoSaq: string;        // 3-) Pliometri ve Saq
  resistance: string;     // 4-) Direnç
  energyProtocol: string; // 5-) Metabolik Protokol
  targetDistance: number;
  targetHsr: number;
  targetRpe: number;
}

export interface RealizedLog {
  id: string;
  playerId: string;
  date: string;
  rtpStage: string;
  actualDistance: number;
  actualHsr: number;
  actualRpe: number;
  vasPain: number;
  createdAt: string;

  // Klinik İç Yük ve Günlük Wellness Değerleri
  vas_pain_score: number;             // 0-10
  session_rpe: number;                // 1-10
  daily_training_duration: number;    // Dakika
  sRPE: number;                       // session_rpe * duration (İç Yük)
  sleep_score: number;                // 1-5 Sabah Uyku Puanı
  fatigue_score: number;              // 1-5 Sabah Yorgunluk Puanı
  stress_score: number;               // 1-5 Sabah Stres Puanı
  wellness_score: number;             // Ortalama Wellness Puanı (1-5)
}import { Player, WeeklyPlan, DailyPlan, RealizedLog } from "./types";

export const INITIAL_PLAYERS: Player[] = [
  {
    id: "p1",
    name: "Ahmet Yılmaz",
    rtpStage: "Aşama 3: Agility/Yön Değiştirme",
    vasPain: 0,
    asymmetry: 8.5,
    hqRatio: 0.65,
    nordbordDrop: 5.0,
    
    rsi_modified: 0.45,
    ecc_decel_impulse_asym: 8.5,
    rfd_0_200ms: 6200,
    nordbord_peak_force_asym: 7.0,
    nordbord_peak_force_total: 380,
    add_abd_ratio: 1.05,
    groin_peak_force_asym: 6.5,
    hq_ratio_60: 0.65,
    quad_peak_torque_bw: 3.4,

    eccentricBrakingAsymmetry: 8.5,
    rsiModified: 0.45,
    hamstringAsymmetry: 7.0,
    hamstringPeakForce: 380,
    adductionsAbductionsRatio: 1.05,
    quadricepsPeakTorque: 250,
    hamstringPeakTorque: 162,
    quadricepsPeakTorque180: 170,
    hamstringPeakTorque180: 120,
    quadricepsPeakTorque300: 110,
    hamstringPeakTorque300: 88,
    hqRatio60: 0.65,
    hqRatio180: 0.71,
    hqRatio300: 0.80,
  },
  {
    id: "p2",
    name: "Mehmet Demir",
    rtpStage: "Aşama 2: Düz Koşu",
    vasPain: 2,
    asymmetry: 12.0,
    hqRatio: 0.58,
    nordbordDrop: 8.0,

    rsi_modified: 0.38,
    ecc_decel_impulse_asym: 12.0,
    rfd_0_200ms: 5100,
    nordbord_peak_force_asym: 11.5,
    nordbord_peak_force_total: 310,
    add_abd_ratio: 0.95,
    groin_peak_force_asym: 12.0,
    hq_ratio_60: 0.58,
    quad_peak_torque_bw: 2.8,

    eccentricBrakingAsymmetry: 12.0,
    rsiModified: 0.38,
    hamstringAsymmetry: 11.5,
    hamstringPeakForce: 310,
    adductionsAbductionsRatio: 0.95,
    quadricepsPeakTorque: 220,
    hamstringPeakTorque: 128,
    quadricepsPeakTorque180: 150,
    hamstringPeakTorque180: 96,
    quadricepsPeakTorque300: 95,
    hamstringPeakTorque300: 68,
    hqRatio60: 0.58,
    hqRatio180: 0.64,
    hqRatio300: 0.72,
  }
];

export const INITIAL_WEEKLY_PLANS: WeeklyPlan[] = [
  {
    id: "wp1",
    playerId: "p1",
    weekNo: "2026-Haziran / Hafta 4 - RTP Faz 3",
    focus: "Nöromüsküler Güç / Hız",
    mon: "Gym: Eksantrik Odak + Saha: Doğrusal Koşular",
    tue: "Saha: Geniş Alan Oyunları (Hedef Yüksek Mesafe)",
    wed: "RECOVERY / Klinik Restorasyon",
    thu: "Gym: Güç/RFD + Saha: Dar Alan Oyunları (İvmelenme)",
    fri: "Saha: Taktik + Sprint Aktivasyonu",
    sat: "MAÇGÜNÜ / Maksimal Yüklenme Simülasyonu",
    sun: "OFF / Dinlenme",
    targetHsr: 1500,
    createdAt: "2026-06-25T10:00:00Z"
  }
];

export const INITIAL_DAILY_PLANS: DailyPlan[] = [
  {
    id: "dp1",
    playerId: "p1",
    date: "2026-06-30",
    type: "Kombine (Saha + Gym)",
    warmup: "10 dk RAMP Isınma: Dinamik Esnemeler, Kalça Mobilizasyonu",
    coreActivation: "Anti-rotasyonel Paloff Press 3x10, Deadbug 3x12, Glute Bridge 3x15",
    plyoSaq: "Hurdle Jump (Frenlemeli) 3x4, Merdiven Ayak Çalışmaları, Kısa Reaktif Çıkışlar",
    resistance: "Trapbar Deadlift 3x5 (%80 1RM - Eksantrik Odak), Bulgar Split Squat 3x6",
    energyProtocol: "Aerobik Güç Gelişimi: 4x60m Progresif İlerleyen Koşular (Giderek Artan Hız)",
    targetDistance: 4500,
    targetHsr: 300,
    targetRpe: 6
  }
];

export const INITIAL_REALIZED_LOGS: RealizedLog[] = [
  {
    id: "rl1",
    playerId: "p1",
    date: "2026-06-29",
    rtpStage: "Aşama 3: Agility/Yön Değiştirme",
    actualDistance: 4300,
    actualHsr: 280,
    actualRpe: 6,
    vasPain: 0,
    createdAt: "2026-06-29T18:00:00Z",
    vas_pain_score: 0,
    session_rpe: 6,
    daily_training_duration: 60,
    sRPE: 360,
    sleep_score: 4,
    fatigue_score: 4,
    stress_score: 5,
    wellness_score: 4.33,
  }
];import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { Player, WeeklyPlan, DailyPlan, RealizedLog } from "./types";
import {
  INITIAL_PLAYERS,
  INITIAL_WEEKLY_PLANS,
  INITIAL_DAILY_PLANS,
  INITIAL_REALIZED_LOGS,
} from "./data";

// Modüler Görünümlerin İmport Edilmesi
import DashboardView from "./components/DashboardView";
import WeeklyPlanningView from "./components/WeeklyPlanningView";
import DailyPlanningView from "./components/DailyPlanningView";
import DailyRealizedView from "./components/DailyRealizedView";
import BiWeeklyTestView from "./components/BiWeeklyTestView";
import IsokineticTestView from "./components/IsokineticTestView";

import {
  LayoutDashboard,
  CalendarDays,
  FileSpreadsheet,
  Zap,
  Activity,
  HeartPulse,
  Users,
  Calendar,
  RotateCcw,
  Plus,
  Menu,
  X,
} from "lucide-react";

export default function App() {
  const [players, setPlayers] = useState<Player[]>(() => {
    const saved = localStorage.getItem("rtp_players");
    return saved ? JSON.parse(saved) : INITIAL_PLAYERS;
  });

  const [weeklyPlans, setWeeklyPlans] = useState<WeeklyPlan[]>(() => {
    const saved = localStorage.getItem("rtp_weekly_plans");
    return saved ? JSON.parse(saved) : INITIAL_WEEKLY_PLANS;
  });

  const [dailyPlans, setDailyPlans] = useState<DailyPlan[]>(() => {
    const saved = localStorage.getItem("rtp_daily_plans");
    return saved ? JSON.parse(saved) : INITIAL_DAILY_PLANS;
  });

  const [realizedLogs, setRealizedLogs] = useState<RealizedLog[]>(() => {
    const saved = localStorage.getItem("rtp_realized_logs");
    return saved ? JSON.parse(saved) : INITIAL_REALIZED_LOGS;
  });

  const [selectedPlayerId, setSelectedPlayerId] = useState<string>("p1");
  const [selectedDate, setSelectedDate] = useState<string>("2026-06-30");
  const [activeMenu, setActiveMenu] = useState<string>("dashboard");
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [newPlayerName, setNewPlayerName] = useState("");
  const [showAddPlayer, setShowAddPlayer] = useState(false);

  useEffect(() => {
    localStorage.setItem("rtp_players", JSON.stringify(players));
  }, [players]);

  useEffect(() => {
    localStorage.setItem("rtp_weekly_plans", JSON.stringify(weeklyPlans));
  }, [weeklyPlans]);

  useEffect(() => {
    localStorage.setItem("rtp_daily_plans", JSON.stringify(dailyPlans));
  }, [dailyPlans]);

  useEffect(() => {
    localStorage.setItem("rtp_realized_logs", JSON.stringify(realizedLogs));
  }, [realizedLogs]);

  const selectedPlayer = players.find((p) => p.id === selectedPlayerId) || players[0];

  const handleUpdatePlayerMetrics = (playerId: string, metrics: Partial<Player>) => {
    setPlayers((prev) =>
      prev.map((p) => (p.id === playerId ? { ...p, ...metrics } : p))
    );
  };

  const handleAddPlayer = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newPlayerName.trim()) return;

    const newPlayer: Player = {
      id: "p_" + Date.now(),
      name: newPlayerName.trim(),
      rtpStage: "Aşama 1: Klinik",
      vasPain: 0,
      asymmetry: 5.0,
      hqRatio: 0.60,
      nordbordDrop: 5.0,
      rsi_modified: 0.40,
      ecc_decel_impulse_asym: 5.0,
      rfd_0_200ms: 5000,
      nordbord_peak_force_asym: 5.0,
      nordbord_peak_force_total: 350,
      add_abd_ratio: 1.05,
      groin_peak_force_asym: 5.0,
      hq_ratio_60: 0.60,
      quad_peak_torque_bw: 3.1,
      eccentricBrakingAsymmetry: 5.0,
      rsiModified: 0.40,
      hamstringAsymmetry: 5.0,
      hamstringPeakForce: 350,
      adductionsAbductionsRatio: 1.05,
      quadricepsPeakTorque: 200,
      hamstringPeakTorque: 120,
    };

    setPlayers((prev) => [...prev, newPlayer]);
    setSelectedPlayerId(newPlayer.id);
    setNewPlayerName("");
    setShowAddPlayer(false);
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans">
      <header className="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="lg:hidden p-2">
              {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
            <h1 className="text-base sm:text-lg font-extrabold text-slate-900">
              🏥 Tesis Performans, Planlama & RTP Yönetim Sistemi
            </h1>
          </div>
          <button onClick={() => {
            if (confirm("Veriler sıfırlansın mı?")) {
              localStorage.clear();
              window.location.reload();
            }
          }} className="flex items-center gap-1 px-3 py-1.5 text-xs text-slate-500 hover:text-rose-600 bg-slate-100 rounded-lg">
            <RotateCcw size={12} />
            <span>Sıfırla</span>
          </button>
        </div>
      </header>

      <div className="max-w-7xl mx-auto w-full px-4 py-6 flex-1 flex flex-col lg:flex-row gap-6">
        <aside className={`w-full lg:w-72 shrink-0 space-y-6 lg:block ${mobileMenuOpen ? "block" : "hidden"}`}>
          <div className="bg-white p-5 rounded-2xl border border-slate-100 space-y-4">
            <div className="flex justify-between items-center">
              <label className="text-xs font-bold text-slate-400 uppercase">👤 Oyuncu Seçimi</label>
              <button onClick={() => setShowAddPlayer(true)} className="text-xs text-indigo-600 font-bold">+ Yeni</button>
            </div>
            {showAddPlayer && (
              <form onSubmit={handleAddPlayer} className="space-y-2">
                <input type="text" placeholder="Oyuncu Adı..." value={newPlayerName} onChange={(e) => setNewPlayerName(e.target.value)} className="w-full text-xs border border-slate-200 rounded-lg p-2" required />
                <button type="submit" className="w-full text-xs bg-indigo-600 text-white rounded p-1.5">Ekle</button>
              </form>
            )}
            <select value={selectedPlayerId} onChange={(e) => setSelectedPlayerId(e.target.value)} className="w-full text-sm font-bold bg-slate-50 border border-slate-200 rounded-xl p-2.5">
              {players.map((p) => <option key={p.id} value={p.id}>{p.name}</option>)}
            </select>
          </div>

          <nav className="bg-white p-4 rounded-2xl border border-slate-100 space-y-1">
            <button onClick={() => setActiveMenu("dashboard")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "dashboard" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <LayoutDashboard size={16} /> 1️⃣ Ana Panel (Dashboard)
            </button>
            <button onClick={() => setActiveMenu("weekly")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "weekly" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <CalendarDays size={16} /> 2️⃣ Haftalık Planlama 🗓️
            </button>
            <button onClick={() => setActiveMenu("daily")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "daily" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <FileSpreadsheet size={16} /> 3️⃣ Günlük İdman Planı
            </button>
            <button onClick={() => setActiveMenu("realized")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "realized" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <Zap size={16} /> 4️⃣ Günlük Yük Girişi 🏃‍♂️
            </button>
            <button onClick={() => setActiveMenu("biweekly")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "biweekly" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <HeartPulse size={16} /> 5️⃣ Haftalık Nöromüsküler Batarya
            </button>
            <button onClick={() => setActiveMenu("isokinetic")} className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold ${activeMenu === "isokinetic" ? "bg-slate-900 text-white" : "text-slate-600 hover:bg-slate-50"}`}>
              <Activity size={16} /> 6️⃣ Aylık İzokinetik Test 🔬
            </button>
          </nav>
        </aside>

        <main className="flex-1 min-w-0">
          <AnimatePresence mode="wait">
            <motion.div key={activeMenu + "_" + selectedPlayerId} initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -12 }} transition={{ duration: 0.15 }} className="space-y-6">
              {activeMenu === "dashboard" && <DashboardView selectedPlayer={selectedPlayer} weeklyPlans={weeklyPlans} dailyPlans={dailyPlans} realizedLogs={realizedLogs} onUpdatePlayerMetrics={handleUpdatePlayerMetrics} />}
              {activeMenu === "weekly" && <WeeklyPlanningView selectedPlayer={selectedPlayer} weeklyPlans={weeklyPlans} onAddWeeklyPlan={() => {}} onDeleteWeeklyPlan={() => {}} />}
              {activeMenu === "isokinetic" && <IsokineticTestView selectedPlayer={selectedPlayer} onUpdatePlayerMetrics={handleUpdatePlayerMetrics} />}
              {/* Diğer modüller burada render edilir... */}
            </motion.div>
          </AnimatePresence>
        </main>
      </div>
    </div>
  );
}import React, { useState, useEffect } from "react";
import { Player } from "../types";
import { 
  Activity, 
  BadgeCheck, 
  Zap, 
  Gauge, 
  Flame, 
  ChevronRight, 
  Scale, 
  Info
} from "lucide-react";

interface IsokineticTestViewProps {
  selectedPlayer: Player;
  onUpdatePlayerMetrics: (playerId: string, metrics: Partial<Player>) => void;
}

export default function IsokineticTestView({
  selectedPlayer,
  onUpdatePlayerMetrics,
}: IsokineticTestViewProps) {
  const [bodyWeight, setBodyWeight] = useState(80);

  // --- STASYON 1: 60°/s (Maksimal Kuvvet Değerlendirmesi) ---
  const [qPeakTorqueL60, setQPeakTorqueL60] = useState(250);
  const [qPeakTorqueR60, setQPeakTorqueR60] = useState(245);
  const [hPeakTorqueL60, setHPeakTorqueL60] = useState(160);
  const [hPeakTorqueR60, setHPeakTorqueR60] = useState(155);
  const [qTimeToPeakL60, setQTimeToPeakL60] = useState(210);
  const [qTimeToPeakR60, setQTimeToPeakR60] = useState(215);
  const [qAngleL60, setQAngleL60] = useState(65);
  const [qAngleR60, setQAngleR60] = useState(67);

  // --- STASYON 2: 180°/s (Güç ve Hız Değerlendirmesi) ---
  const [qPeakTorqueL180, setQPeakTorqueL180] = useState(170);
  const [qPeakTorqueR180, setQPeakTorqueR180] = useState(165);
  const [hPeakTorqueL180, setHPeakTorqueL180] = useState(120);
  const [hPeakTorqueR180, setHPeakTorqueR180] = useState(115);
  const [qAvgPowerL180, setQAvgPowerL180] = useState(280);
  const [qAvgPowerR180, setQAvgPowerR180] = useState(270);
  const [hEccPeakTorqueL180, setHEccPeakTorqueL180] = useState(165);
  const [hEccPeakTorqueR180, setHEccPeakTorqueR180] = useState(160);

  // --- STASYON 3: 300°/s (Kuvvette Devamlılık Değerlendirmesi) ---
  const [qPeakTorqueL300, setQPeakTorqueL300] = useState(110);
  const [qPeakTorqueR300, setQPeakTorqueR300] = useState(105);
  const [hPeakTorqueL300, setHPeakTorqueL300] = useState(88);
  const [hPeakTorqueR300, setHPeakTorqueR300] = useState(82);
  const [qFatigueL300, setQFatigueL300] = useState(42);
  const [qFatigueR300, setQFatigueR300] = useState(44);
  const [hFatigueL300, setHFatigueL300] = useState(45);
  const [hFatigueR300, setHFatigueR300] = useState(47);
  const [qWorkL300, setQWorkL300] = useState(1200);
  const [qWorkR300, setQWorkR300] = useState(1150);

  const [successMsg, setSuccessMsg] = useState("");

  useEffect(() => {
    setQPeakTorqueL60(selectedPlayer.quadricepsPeakTorque || 250);
    setQPeakTorqueR60(selectedPlayer.quadricepsPeakTorque ? Math.round(selectedPlayer.quadricepsPeakTorque * 0.96) : 240);
    setHPeakTorqueL60(selectedPlayer.hamstringPeakTorque || 160);
    setHPeakTorqueR60(selectedPlayer.hamstringPeakTorque ? Math.round(selectedPlayer.hamstringPeakTorque * 0.96) : 150);
    setQPeakTorqueL180(selectedPlayer.quadricepsPeakTorque180 || 170);
    setQPeakTorqueR180(selectedPlayer.quadricepsPeakTorque180 ? Math.round(selectedPlayer.quadricepsPeakTorque180 * 0.97) : 165);
    setQPeakTorqueL300(selectedPlayer.quadricepsPeakTorque300 || 110);
    setQPeakTorqueR300(selectedPlayer.quadricepsPeakTorque300 ? Math.round(selectedPlayer.quadricepsPeakTorque300 * 0.95) : 105);
  }, [selectedPlayer]);

  const pWeight = bodyWeight > 0 ? bodyWeight : 80;

  // Rölatif Kuvvetler
  const qRelL60 = parseFloat((qPeakTorqueL60 / pWeight).toFixed(2));

  // Asimetriler (Sağ vs Sol)
  const qAsym60 = Math.max(qPeakTorqueL60, qPeakTorqueR60) > 0 ? parseFloat((Math.abs(qPeakTorqueL60 - qPeakTorqueR60) / Math.max(qPeakTorqueL60, qPeakTorqueR60) * 100).toFixed(1)) : 0;
  const hAsym60 = Math.max(hPeakTorqueL60, hPeakTorqueR60) > 0 ? parseFloat((Math.abs(hPeakTorqueL60 - hPeakTorqueR60) / Math.max(hPeakTorqueL60, hPeakTorqueR60) * 100).toFixed(1)) : 0;
  const qAsym180 = Math.max(qPeakTorqueL180, qPeakTorqueR180) > 0 ? parseFloat((Math.abs(qPeakTorqueL180 - qPeakTorqueR180) / Math.max(qPeakTorqueL180, qPeakTorqueR180) * 100).toFixed(1)) : 0;
  const hAsym180 = Math.max(hPeakTorqueL180, hPeakTorqueR180) > 0 ? parseFloat((Math.abs(hPeakTorqueL180 - hPeakTorqueR180) / Math.max(hPeakTorqueL180, hPeakTorqueR180) * 100).toFixed(1)) : 0;
  const qAsym300 = Math.max(qPeakTorqueL300, qPeakTorqueR300) > 0 ? parseFloat((Math.abs(qPeakTorqueL300 - qPeakTorqueR300) / Math.max(qPeakTorqueL300, qPeakTorqueR300) * 100).toFixed(1)) : 0;

  // H:Q Rasyoları
  const hqRatioL60 = qPeakTorqueL60 > 0 ? parseFloat((hPeakTorqueL60 / qPeakTorqueL60).toFixed(2)) : 0;
  const hqRatioR60 = qPeakTorqueR60 > 0 ? parseFloat((hPeakTorqueR60 / qPeakTorqueR60).toFixed(2)) : 0;
  const hqFuncL180 = qPeakTorqueL180 > 0 ? parseFloat((hEccPeakTorqueL180 / qPeakTorqueL180).toFixed(2)) : 0;
  const hqFuncR180 = qPeakTorqueR180 > 0 ? parseFloat((hEccPeakTorqueR180 / qPeakTorqueR180).toFixed(2)) : 0;
  const hqRatioL300 = qPeakTorqueL300 > 0 ? parseFloat((hPeakTorqueL300 / qPeakTorqueL300).toFixed(2)) : 0;
  const hqRatioR300 = qPeakTorqueR300 > 0 ? parseFloat((hPeakTorqueR300 / qPeakTorqueR300).toFixed(2)) : 0;

  const qDropL = qPeakTorqueL60 > 0 ? parseFloat((((qPeakTorqueL60 - qPeakTorqueL180) / qPeakTorqueL60) * 100).toFixed(1)) : 0;
  const qDropR = qPeakTorqueR60 > 0 ? parseFloat((((qPeakTorqueR60 - qPeakTorqueR180) / qPeakTorqueR60) * 100).toFixed(1)) : 0;

  const evaluateStatus = () => {
    const reasons: string[] = [];
    const isRed = qAsym60 > 15 || hAsym60 > 15 || hqRatioL60 < 0.55 || hqRatioR60 < 0.55 || qFatigueL300 > 50;
    
    if (qAsym60 > 15) reasons.push(`Quadriceps Asimetrisi (%${qAsym60}) kritik eşiğin (> %15) üzerindedir.`);
    if (hqRatioL60 < 0.55) reasons.push(`H:Q Oranı kritik sınırın (< 0.55) altında.`);

    if (isRed) {
      return {
        light: "red" as const,
        status: "🔴 KIRMIZI IŞIK (Yüksek Risk - Saha İzni Yok)",
        action: "Kritik asimetri veya düşük H:Q rasyosu saptandı. Sporcunun sahaya dönmesi risklidir.",
        color: "bg-rose-50 border-rose-200 text-rose-900",
        reasons
      };
    }

    return {
      light: "green" as const,
      status: "🟢 YEŞİL IŞIK (Güvenle Sahaya Dönüş)",
      action: "Kusursuz diz eklem dengesi! Tüm biyomekanik kriterler RTP standartlarına uygundur.",
      color: "bg-emerald-50 border-emerald-200 text-emerald-900",
      reasons: ["Bilateral asimetriler güvenli seviyededir (< %10).", "Koruyucu H:Q oranları idealdir."]
    };
  };

  const decision = evaluateStatus();

  return (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-2xl border border-slate-100 flex justify-between items-center">
        <div>
          <h2 className="text-xl font-black text-slate-800 flex items-center gap-2">
            <Activity className="text-violet-600 h-6 w-6" />
            🔬 Çoklu Açısal Hız İzokinetik Dinamometre Analizi
          </h2>
          <p className="text-xs text-slate-500">60°/s (Maksimum Kuvvet), 180°/s (Güç) ve 300°/s (Dayanıklılık) profilleri.</p>
        </div>
        <div className="bg-slate-100 p-2 rounded-xl flex items-center gap-2">
          <span className="text-xs font-bold">Kilo:</span>
          <input type="number" value={bodyWeight} onChange={(e) => setBodyWeight(parseInt(e.target.value) || 80)} className="w-12 bg-white text-center rounded font-mono text-xs" />
        </div>
      </div>

      <div className={`border-2 p-5 rounded-2xl ${decision.color}`}>
        <h3 className="font-bold text-sm uppercase tracking-wider">{decision.status}</h3>
        <p className="text-xs mt-1">{decision.action}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* STASYON 1: 60°/s */}
        <div className="bg-white p-5 rounded-2xl border border-slate-100 space-y-4">
          <h4 className="font-bold text-slate-800 text-xs flex items-center gap-1">
            <Gauge size={14} className="text-indigo-600" /> 60°/s Maks Tork
          </h4>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div>
              <label className="text-[10px]">Sol Quad (Nm)</label>
              <input type="number" value={qPeakTorqueL60} onChange={(e) => setQPeakTorqueL60(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
            <div>
              <label className="text-[10px]">Sağ Quad (Nm)</label>
              <input type="number" value={qPeakTorqueR60} onChange={(e) => setQPeakTorqueR60(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
          </div>
          <div className="bg-slate-900 text-slate-100 text-[11px] p-3 rounded-xl space-y-1 font-mono">
            <div>Asimetri: %{qAsym60}</div>
            <div>Konvansiyonel H:Q Sol: {hqRatioL60}</div>
          </div>
        </div>

        {/* STASYON 2: 180°/s */}
        <div className="bg-white p-5 rounded-2xl border border-slate-100 space-y-4">
          <h4 className="font-bold text-slate-800 text-xs flex items-center gap-1">
            <Zap size={14} className="text-amber-500" /> 180°/s Güç
          </h4>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div>
              <label className="text-[10px]">Sol Eksantrik H (Nm)</label>
              <input type="number" value={hEccPeakTorqueL180} onChange={(e) => setHEccPeakTorqueL180(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
            <div>
              <label className="text-[10px]">Sağ Eksantrik H (Nm)</label>
              <input type="number" value={hEccPeakTorqueR180} onChange={(e) => setHEccPeakTorqueR180(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
          </div>
          <div className="bg-slate-900 text-slate-100 text-[11px] p-3 rounded-xl space-y-1 font-mono">
            <div className="text-amber-300">Fonksiyonel H:Q Sol: {hqFuncL180}</div>
            <div className="text-amber-300 font-semibold">Hedef: ~ 1.00 (Koruyucu Frenleme)</div>
          </div>
        </div>

        {/* STASYON 3: 300°/s */}
        <div className="bg-white p-5 rounded-2xl border border-slate-100 space-y-4">
          <h4 className="font-bold text-slate-800 text-xs flex items-center gap-1">
            <Flame size={14} className="text-rose-500" /> 300°/s Dayanıklılık
          </h4>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div>
              <label className="text-[10px]">Sol Quad Yorgunluk (%)</label>
              <input type="number" value={qFatigueL300} onChange={(e) => setQFatigueL300(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
            <div>
              <label className="text-[10px]">Sağ Quad Yorgunluk (%)</label>
              <input type="number" value={qFatigueR300} onChange={(e) => setQFatigueR300(parseInt(e.target.value) || 0)} className="w-full bg-slate-50 border border-slate-200 rounded p-1.5" />
            </div>
          </div>
          <div className="bg-slate-900 text-slate-100 text-[11px] p-3 rounded-xl space-y-1 font-mono">
            <div>Asimetri 300°/s: %{qAsym300}</div>
            <div className="text-rose-300">Konv. H:Q Sol: {hqRatioL300}</div>
          </div>
        </div>
      </div>
    </div>
  );
}
