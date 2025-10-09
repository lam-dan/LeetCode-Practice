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

  const s1Count = new Array(26).fill(0); // counts for s1
  const s2Count  = new Array(26).fill(0); // counts for current window in s2

  // Build counts for s1 and the initial window of s2 (length = s1.length)
  for (let i = 0; i < s1.length; i++) {
    s1Count[s1.charCodeAt(i) - 97]++;
    s2Count[s2.charCodeAt(i) - 97]++;
  }

  // Check initial window
  if (equalBuckets(s1Count, s2Count)) return true;

  // Slide the fixed-size window across s2
  for (let l = 0, r = s1.length; r < s2.length; r++, l++) {
    s2Count[s2.charCodeAt(r) - 97]++; // add right char
    s2Count[s2.charCodeAt(l) - 97]--; // remove left char
    if (equalBuckets(s1Count, s2Count)) return true;
  }
  return false;
};

// Helper: do all 26 buckets match?
const equalBuckets = (s1Count, s2Count) => {
  for (let i = 0; i < 26; i++) {
    if (s1Count[i] !== s2Count[i]) return false;
  }
  return true;
}