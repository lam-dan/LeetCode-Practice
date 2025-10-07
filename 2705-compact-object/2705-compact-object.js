/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
  // If it's not an object (primitive), return directly
  if (obj === null || typeof obj !== "object") return obj;

  // Root type
  const result = Array.isArray(obj) ? [] : {};
  const stack = [{ source: obj, target: result }];

  while (stack.length > 0) {
    const { source, target } = stack.pop();

    if (Array.isArray(source)) {
      for (const value of source) {
        if (Boolean(value)) {
          if (typeof value === "object" && value !== null) {
            const newTarget = Array.isArray(value) ? [] : {};
            target.push(newTarget);
            stack.push({ source: value, target: newTarget });
          } else {
            target.push(value);
          }
        }
      }
    } else {
      for (const [key, value] of Object.entries(source)) {
        if (Boolean(value)) {
          if (typeof value === "object" && value !== null) {
            const newTarget = Array.isArray(value) ? [] : {};
            target[key] = newTarget;
            stack.push({ source: value, target: newTarget });
          } else {
            target[key] = value;
          }
        }
      }
    }
  }

  return result;
    
};