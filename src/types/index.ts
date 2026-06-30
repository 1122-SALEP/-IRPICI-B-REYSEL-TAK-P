export interface Player {
  id: string;
  name: string;
  age: number;
  position: string;
  injuryType: string;
  surgeryDate: string;
  phase: number;
  
  // Weekly metrics
  vasPain: number;
  yBalanceAsymmetry: number;
  nordbordForceDrop: number;
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
  hqRatio: number; // General (60°/s standard)
}

export interface WeeklyPlan {
  id: string;
  playerId: string;
  weekNumber: number;
  startDate: string;
  goals: string[];
  status: "active" | "completed";
}

export interface DailyPlan {
  id: string;
  playerId: string;
  date: string;
  type: string; // "Saha İdmanı" | "Gym / Kuvvet Seansı" | vb.
  warmup: string;         // 1-) Isınma & Mobilizasyon (RAMP)
  coreActivation: string; // 2-) Core-Aktivasyon
  plyoSaq: string;        // 3-) Pliometri ve Saq
  resistance: string;     // 4-) Direnç
  energyProtocol: string; // 5-) Metabolik
  targetDistance: number;
  targetHsr: number;
  targetRpe: number;
}
