/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
  // Base case 1: null or primitive → return as-is
  if (obj === null || typeof obj !== "object") {
    return obj;
  }

  // Base case 2: handle arrays
  if (Array.isArray(obj)) {
    const result = [];
    for (const val of obj) {
      if (!val) continue; // skip falsy values
      const compacted = compactObject(val); // recurse into nested objects/arrays
      if (compacted) result.push(compacted);
    }
    return result;
  }

  // Base case 3: handle plain objects
  const result = {};
  for (const [key, val] of Object.entries(obj)) {
    if (!val) continue; // skip falsy values
    const compacted = compactObject(val);
    if (compacted) result[key] = compacted;
  }
  return result;
};