/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
  // Shared cursor: points to the next function to start
  // It's shared among all workers, so they pull tasks sequentially.
  let i = 0;

  /**
   * A "worker" represents one concurrent slot in the pool.
   * It continuously grabs the next available function (if any)
   * and executes it. When no functions remain, it exits.
   */
  async function worker() {
    // Keep looping until we've started all available functions
    while (i < functions.length) {
      const idx = i++;          // Claim the next function index
      await functions[idx]();   // Run that function and wait for it to finish
      // Once done, the loop continues — the worker picks the next pending function
    }
    // When i >= functions.length, this worker simply finishes.
  }

  // Determine how many workers to start — can't exceed the number of functions
  const k = Math.min(n, functions.length);

  // Create and start k workers. Each worker runs independently.
  const workers = Array(k).fill(0).map(() => worker());

  // Wait until all workers complete — meaning all functions have resolved
  await Promise.all(workers);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */