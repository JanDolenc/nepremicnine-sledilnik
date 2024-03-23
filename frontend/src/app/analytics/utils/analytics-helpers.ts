import { ActiveAd, RegijaVrstaCount } from './active-ads';

export const getCurrentYearMonth = (): {
  year: number;
  month: number;
} => {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  console.log(typeof year);
  return { year, month };
};

/**
 *
 * @param activeAds
 * Group ads in groups of: regija, vrsta and count.
 * The count for each tip is sumed into one value.
 * Example: { "regija": "Gorenjska","vrsta": "Hiša", "count": 304 }
 */
export const groupAdsRegijaVrsta = (
  activeAds: ActiveAd[]
): RegijaVrstaCount[] => {
  return activeAds.reduce((acc: any, ad: ActiveAd) => {
    // Find the existing group for the current regija and vrsta, or create a new one
    let group = acc.find(
      (g: RegijaVrstaCount) => g.regija === ad.regija && g.vrsta === ad.vrsta
    );
    if (!group) {
      group = { regija: ad.regija, vrsta: ad.vrsta, count: 0 };
      acc.push(group);
    }

    group.count += ad.count;

    return acc;
  }, [] as { regija: string; vrsta: string; count: number }[]);
};
