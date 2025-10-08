/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) return "null"
    if (object === undefined) return "undefined"
    if (Number.isNaN(object)) return "NaN"
    if (typeof object === "boolean") {
        return object
    }

    if (typeof object === "string") {
        // console.log("String", object)
        return `"${object}"`; // handles strings
    }
    if (typeof object !== "object") { //handles primitives
        // console.log("handle primitives", object)
        return String(object)
    }
    if (Array.isArray(object)){
        // console.log("Crazy nested conversion", `[${obj.map(convertObjectToString).join(",")}]`)
        return `[${object.map(jsonStringify).join(",")}]`
    }
    // Base Cases
    // Objects - checked
    // Arrays
    // Primitives - check
    // null - check
    // undefined - check
    // NaN - check

    // Recursively Handling Object Conversion to String 
    if (typeof object === "object"){
        const entries = Object.entries(object).map(([key, value]) => {
            return `"${key}":${jsonStringify(value)}` // Recursion handles nested objects
        })
        return `{${entries.join(",")}}`
    }
    return false
};