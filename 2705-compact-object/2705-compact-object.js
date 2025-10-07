/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (obj === null || typeof obj !== "object") { // has to be an array or object, otherwise we return primitives
        return obj
    }
    const root = Array.isArray(obj) ? [] : {}
    const stack = [[obj, root]]

    while (stack.length > 0) {
        const [currObj, newCurrObj] = stack.pop()

        if(Array.isArray(currObj)) { // Case 1: Current Layer is an array
            for (const val of currObj) {
                if (!val) {
                    continue;// Skip falsy values: false, 0, "", null, undefined, NaN
                } else if (typeof val === "object") {  // Not an object (plain objects, arrays, functions, special objects(Date, RegExp, Map, Set. etc))
                    const newSubObj = Array.isArray(val) ? [] : {} // Figure out what object
                    newCurrObj.push(newSubObj)
                    stack.push([val, newSubObj])
                } else { //Otherwise it's a an object
                    newCurrObj.push(val) // Push into array the primitive (ie, number, string, boolean, undefined, symbol, bigInt)
                }
            }
        } else { // Case 1: Current Layer is an object
            for (const [key, val] of Object.entries(currObj)) {
                if (!val) {
                    continue // Skip falsy values: false, 0, "", null, undefined, NaN
                    //Otherwise if it's another object we need to handle
                } else if (typeof val === "object") { // Is it an object (plain objects, arrays, functions, special objects(Date, RegExp, Map, Set. etc))
                    const newSubObj = Array.isArray(val) ? [] : {} // Figure out what object
                    newCurrObj[key] = newSubObj
                    stack.push([val, newSubObj])
                } else { // Otherwise it's a primitive value
                    newCurrObj[key] = val
                }
            }
        }
    }
    return root
};