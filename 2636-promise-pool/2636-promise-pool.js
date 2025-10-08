/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
  // Shared index across all workers.
  // Each worker grabs the next function index and increments `i`.
  let i = 0;

  /**
   * A worker represents one "concurrent slot" in the pool.
   * - It runs tasks one by one (sequentially) inside its own loop.
   * - But multiple workers run concurrently with each other.
   */
  async function worker() {
    // Keep picking tasks until there are no more left
    while (i < functions.length) {
      const idx = i++;          // Reserve the next function index atomically
      await functions[idx]();   // Run that async function (pauses this worker only)
      // While this worker awaits, other workers continue running their own tasks
    }
    // When i >= functions.length, this worker has nothing left to do and exits.
  }

  // Create up to `n` workers (or fewer if fewer functions exist).
  const k = Math.min(n, functions.length);

  /**
   * This line starts all workers immediately.
   * - Each call to worker() begins executing right away (async functions start instantly).
   * - Each worker() returns a Promise representing its eventual completion.
   * - Therefore, we now have `k` concurrent worker Promises running in parallel.
   */
  const workers = Array(k).fill(0).map(() => worker());

  /**
   * Wait until ALL workers have finished.
   * - Promise.all() waits for all worker Promises to resolve.
   * - Each worker runs sequentially inside its loop,
   *   but all workers run concurrently across the pool.
   * - As a result, at most `n` async tasks are ever pending at once.
   */
  await Promise.all(workers);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */