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
  if (typeof o1 !== "object" || typeof o2 !== "object") return false; 

  const a1 = Array.isArray(o1), a2 = Array.isArray(o2);
  if (a1 !== a2) return false;

  if (a1 && a2) {
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
    if (Object.keys(o1).length !== Object.keys(o2).length) {
        return false;
    }
    for (const [key, value] of Object.entries(o1)) {
        // Check if keys are not equal
        if (!Object.hasOwn(o2, key)) {
            return false;
        }
        // Check if values are not equal
        if (!areDeeplyEqual(value, o2[key])) {
            return false;
        }
    }
  }



  return true;
};