/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    // Normalize if inputs may contain uppercase
  // s1 = s1.toLowerCase(); s2 = s2.toLowerCase();

  // Early exit: s1 can't fit into s2
  if (s1.length > s2.length) return false;

  const A = 'a'.charCodeAt(0);
  const need = new Array(26).fill(0); // counts for s1
  const win  = new Array(26).fill(0); // counts for current window in s2

  // Build counts for s1 and the initial window of s2 (length = s1.length)
  for (let i = 0; i < s1.length; i++) {
    need[s1.charCodeAt(i) - A]++;
    win [s2.charCodeAt(i) - A]++;
  }

  // Check initial window
  if (equalBuckets(need, win)) return true;

  // Slide the fixed-size window across s2
  for (let l = 0, r = s1.length; r < s2.length; r++, l++) {
    win[s2.charCodeAt(r) - A]++; // add right char
    win[s2.charCodeAt(l) - A]--; // remove left char
    if (equalBuckets(need, win)) return true;
  }

  return false;
};

// Helper: do all 26 buckets match?
function equalBuckets(need, win) {
  for (let i = 0; i < 26; i++) {
    if (need[i] !== win[i]) return false;
  }
  return true;
}