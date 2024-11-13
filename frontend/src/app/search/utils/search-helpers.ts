export const isAdActive = (recordTs: number): boolean => {
  // convert from s to ms
  recordTs = recordTs * 1000;
  const currentTs = Date.now();

  const tsDelta = currentTs - recordTs;
  const fifteenDays = 1296000000; // in miliseconds

  // ad is considered active if delta is less than 15 days meaning crawler detected the ad in the last 15 days.
  if (tsDelta < fifteenDays) {
    return true;
  } else {
    return false;
  }
};

export interface SearchBarOptions {
  layout: string;
  placeholderText: string;
  miniButton: boolean;
}
