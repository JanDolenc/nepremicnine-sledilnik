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
