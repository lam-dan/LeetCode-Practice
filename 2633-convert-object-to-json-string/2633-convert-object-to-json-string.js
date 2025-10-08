/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    // Base Cases - Recursive Approach
    // Objects - checked
    // Arrays - Check
    // Primitives - check
    // null - check
    // undefined - check
    // NaN - check

    // Handle Falsies
    if (object === null) return String(object)
    if (object === undefined) return String(object)
    if (Number.isNaN(object)) return String(object)

    // Handle Primitives - Strings, Booleans, Numbers
    if (typeof object === "boolean") {
        return String(object)
    } 
    if (typeof object === "string") {
        console.log("String", object)
        // return `"${object}"`; // handles strings
        // String("str") conversion returns just str
        //
        return `"${String(object)}"`

    }
    // 
    if (typeof object !== "object") { 
        // console.log("handle primitives", object)
        return String(object)
    }

    // Handle Arrays {}, since Arrays are technically objects as well, it goes before objects
    if (Array.isArray(object)){
        // console.log("Crazy nested conversion", `[${obj.map(convertObjectToString).join(",")}]`)
        return `[${object.map(jsonStringify).join(",")}]`
    }

    //Handle Objects {}
    // Recursively Handling Object Conversion to String 
    if (typeof object === "object"){
        const entries = Object.entries(object).map(([key, value]) => {
            return `"${key}":${jsonStringify(value)}` // Recursion handles nested objects
        })
        return `{${entries.join(",")}}`
    }
    return false
};