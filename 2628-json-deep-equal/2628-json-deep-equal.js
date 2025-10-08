/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // Hanle Strict Equalness Early on
  if (o1 === o2) return true;

  // Handle null and undefined
  if (o1 === null || o2 === null || o1 === undefined || o2 === undefined) return false;
  // Handles if one of the objects is undefined, but not null (javascript bug)
  if (typeof o1 !== "object" || typeof o2 !== "object") {
    return false; 
  }

  if (Array.isArray(o1) !== Array.isArray(o2)) {
    return false;
  } 

  if (Array.isArray(o1) && Array.isArray(o2)) {
    if (o1.length !== o2.length) {
        return false;
    }
    for (let i = 0; i < o1.length; i++) {
      if (!areDeeplyEqual(o1[i], o2[i])) {
        return false;
      }
    }
    return true;
  }

  // Case 1: Check if both are Objects
  if (typeof o1 === "object" && typeof o2 === "object") {
    const o1Entries = Object.entries(o1)
    const o2Entries = Object.entries(o2)
    // Check if the object's properties have the same lengths
    if (o1Entries.length !== o2Entries.length) {
        return false;
    }
    for (const [key, value] of o1Entries) {
        // Edge Case: Keys are out of order but exist in the other object
        // Thus, we need to check if one object doesn't have the other object's keys
        if (!Object.hasOwn(o2, key)) {
            return false;
        } else {
            // If the keys are equal then, check if values are not equal
            if (!areDeeplyEqual(value, o2[key])) {
                return false;
            }
        }
    }
    return true
  }
  return false;
};