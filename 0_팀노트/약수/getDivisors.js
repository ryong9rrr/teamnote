const getDivisors = (number) => {
  if (number <= 0) throw new Error("자연수가 아니에요.");
  const limit = Math.floor(Math.sqrt(number));
  const divisors = [];
  for (let left = 1; left < limit + 1; left++) {
    if (number % left === 0) {
      const right = number / left;
      divisors.push(left);
      if (left !== right) {
        divisors.push(right);
      }
    }
  }
  return divisors;
};
