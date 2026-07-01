export interface Player {
  id: string;
  name: string;
  rtpStage: string; // e.g., "Aşama 1: Klinik", "Aşama 2: Düz Koşu", etc.
  
  // Current test/RTP thresholds
  vasPain: number;        // 0-10
  asymmetry: number;      // ForceDecks Eccentric Braking Asymmetry (%)
  hqRatio: number;        // Isokinetic H:Q Ratio
  nordbordDrop: number;   // NordBord Force Drop (%)
  
  // PDF Section 2 - Device-based Test Batteries & Metrics Schema
  rsi_modified: number;              // ForceDecks CMJ (Dinamik) - Float
  ecc_decel_impulse_asym: number;    // ForceDecks CMJ (Frenleme) - Float (%)
  rfd_0_200ms: number;               // ForceDecks IMTP (İzometrik) - Integer (N/s)
  nordbord_peak_force_asym: number;  // NordBord Nordic Hamstring Asymmetry - Float (%)
  nordbord_peak_force_total: number; // NordBord Nordic Hamstring Total Force - Integer (N)
  add_abd_ratio: number;             // ForceFrame Groin Squeeze Ratio - Float
  groin_peak_force_asym: number;     // ForceFrame Groin Squeeze Asymmetry - Float (%)
  hq_ratio_60: number;               // İzokinetik H:Q 60°/s - Float
  quad_peak_torque_bw: number;       // İzokinetik 60°/s relative power - Float (Nm/kg)
  
  // Bi-Weekly neuromuscular metrics
  eccentricBrakingAsymmetry: number;
  rsiModified: number;
  hamstringAsymmetry: number;
  hamstringPeakForce: number;
  adductionsAbductionsRatio: number;
  
  // Monthly isokinetic metrics
  quadricepsPeakTorque: number; // Defaults to 60°/s
  hamstringPeakTorque: number;  // Defaults to 60°/s
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
  type: string; // "Saha İdmanı" | "Gym / Kuvvet Seansı" | etc.
  warmup: string;         // 1-) Isınma
  coreActivation: string; // 2-) Core-Aktivasyon
  plyoSaq: string;        // 3-) Pliometri ve Saq
  resistance: string;     // 4-) Direnç
  energyProtocol: string; // 5-) Metabolik
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

  // PDF Section 3 - Daily Internal Load & Clinical Response Metrics
  vas_pain_score: number;             // Integer (0-10) - Visual Pain Scale
  session_rpe: number;                // Integer (1-10) - Session RPE
  daily_training_duration: number;    // Integer (minutes) - Training duration
  sRPE: number;                       // Integer - calculated as session_rpe * daily_training_duration
  sleep_score: number;                // 1-5 morning sleep rating
  fatigue_score: number;              // 1-5 morning fatigue rating
  stress_score: number;               // 1-5 morning stress rating
  wellness_score: number;             // Float - average of sleep, fatigue, and stress (1-5)
}
