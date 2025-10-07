/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
  let i = 0; // shared cursor

  async function worker() {
    while (i < functions.length) {
      const idx = i++;
      await functions[idx]();
    }
  }

  const k = Math.min(n, functions.length);
  await Promise.all(Array(k).fill(0).map(() => worker()));
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */