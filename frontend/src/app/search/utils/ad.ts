export interface Price {
  record_ts: number;
  cena: number;
}

export interface Ad {
  id: number;
  referencna_st: number;
  url: string;
  naslov: string;
  posredovanje: string;
  agencija: string | null;
  vrsta: string;
  tip: string | null;
  velikost: number;
  zemljisce: number | null;
  leto_izgradnje: number | null;
  nadstropje: string | null;
  regija: string;
  detected_ts: number;
  updated_ts: number;
  price_data: Price[];
}

export interface SimilarAd {
  referencna_st: number;
  naslov: string;
  vrsta: string;
  tip: string | null;
  velikost: number;
  leto_izgradnje: number | null;
  nadstropje: string | null;
  regija: string;
  cena: number;
}

export interface SimilarAds {
  similar_oglasi: SimilarAd[];
}
