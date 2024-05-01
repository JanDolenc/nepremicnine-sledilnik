export interface MedianObject {
  regija: string;
  hisa: number;
  stanovanje: number;
}

export interface Median {
  period: string;
  median: MedianObject[];
}
