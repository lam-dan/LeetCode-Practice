/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
  if (o1 === o2) return true;

  // Handle null and non-objects early
  if (o1 === null || o2 === null) return false;
  if (typeof o1 !== "object" || typeof o2 !== "object") return false;

  const a1 = Array.isArray(o1), a2 = Array.isArray(o2);
  if (a1 !== a2) return false;

  if (a1 && a2) {
    if (o1.length !== o2.length) return false;
    for (let i = 0; i < o1.length; i++) {
      if (!areDeeplyEqual(o1[i], o2[i])) return false;
    }
    return true;
  }

  // plain objects
  if (typeof o1 === "object" && typeof o2 === "object") {
    if (Object.keys(o1).length !== Object.keys(o2).length) {
        return false;
    }
    for (const [key, value] of Object.entries(o1)) {
        if (!Object.hasOwn(o2, key)) {
            return false;
        }
        if (!areDeeplyEqual(value, o2[key])) {
            return false;
        }
    }
  }



  return true;
};