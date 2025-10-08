/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */

 // Recursion Approach
var areDeeplyEqual = function(o1, o2) {
    // Base cases
    if (o1 === o2) return true

    if (typeof o1 !== "object" || typeof o2 !== "object") return false

    if (String(o1) !== String(o2)) return false

    if (Array.isArray(o1) && Array.isArray(o2)) {
        if (o1.length !== o2.length) {
            return false
        }
        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) {
                return false
            }
        }
        return true
    }

    if (typeof o1 === "object" && typeof o2 === "object") {
        console.log("BOTH OBJECTS")
        if (Object.keys(o1).length !== Object.keys(o2).length){
            return false
        }
        for (const [key, value] of Object.entries(o1)) {
            if (Object.hasOwn(o2, key)){
                if (!areDeeplyEqual(value, o2[key])) {
                    console.log("world")
                    return false
                }
                console.log("hello")
            } else {
                return false
            }
        }
        return true
    }

    return false

};