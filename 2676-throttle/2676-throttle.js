/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
/**
 * 2676. Throttle
 *
 * This throttle implementation:
 *  - Runs the function immediately on the first call
 *  - Starts a repeating timer that fires every `t` ms
 *  - While that timer is active, any new calls only update `argsToProcess`
 *  - Each timer tick executes `fn` once with the latest saved arguments
 *  - If no new arguments are saved by a tick, the interval stops (goes idle)
 */
var throttle = function (fn, t) {
  // When null → no timer is running, so we're idle and can run immediately.
  // When set → we have an active interval ticking every `t` ms.
  let intervalInProgress = null;

  // Latest arguments saved while throttling is active.
  // Each new call overwrites this until the next tick consumes them.
  let argsToProcess = null;

  /**
   * Runs every `t` ms once `setInterval()` starts.
   * Think of it as the "heartbeat" of this throttle.
   * - If there are pending args (argsToProcess ≠ null), run fn with them.
   * - If there are no pending args, stop the interval and go idle.
   */
  const intervalFunction = () => {
    if (argsToProcess === null) {
      // No calls since the last tick → nothing new to process.
      // Stop the interval so we don't keep looping unnecessarily.
      clearInterval(intervalInProgress);
      intervalInProgress = null; // return to idle state
    } else {
      // We have new arguments saved by the user calling throttled(...)
      // Run fn once with the most recent arguments.
      fn(...argsToProcess);

      // Clear the stored args — this tick has now handled them.
      argsToProcess = null;

      // The interval keeps running; if more calls arrive before the next tick,
      // they’ll set argsToProcess again and get processed on the next tick.
    }
  };

  /**
   * The wrapper function that users call instead of fn.
   * - If idle, run immediately and start the interval.
   * - If busy, just update argsToProcess with the latest args.
   */
  return function throttled(...args) {
    // This condition is checked *only* when the user (or an event)
    // calls throttled(). The interval does not re-enter this check.
    if (intervalInProgress) {
      // We’re still in the cooldown window.
      // Don’t run fn yet — simply remember these latest arguments.
      argsToProcess = args;
    } else {
      // We’re idle (no active interval), so run fn right away.
      fn(...args);

      // Start the repeating interval that will tick every `t` ms.
      // The first tick will happen t ms after this call (e.g., 50 + 70 = 120ms).
      // Each tick will decide whether to run fn again or stop.
      intervalInProgress = setInterval(intervalFunction, t);
    }
  };
};
/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */