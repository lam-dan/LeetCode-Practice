/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) return "null"
    if (object === undefined) return "undefined"
    if (Number.isNaN(object)) return "NaN"

    if (typeof object === "boolean") {
        // console.log("boolean", object)
        return object
    }

    if (object === null) return null
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
    function convertObjectToString(obj){
        if (obj === null) return "null" // handling null
        if (obj === undefined) return "undefined"
        if (Number.isNaN(obj)) return "NaN"
        // Base Cases for a value that is a "a"
        
        if (typeof obj === "string") {
            // console.log("String", obj)
            return `"${obj}"`; // handles strings
        }

        // Edge case where value is null but needs to have double quotes "null"
        // typeof obj is actually an object so we just need to do a direct comparison
        if (typeof obj !== "object") { //handles primitives
            // console.log("handle primitives", obj)
            return String(obj)
        }

        if (Array.isArray(obj)){
            // console.log("Crazy nested conversion", `[${obj.map(convertObjectToString).join(",")}]`)
            return `[${obj.map(convertObjectToString).join(",")}]`
        }

        const entries = Object.entries(obj).map(([key, value]) => {
            return `"${key}":${convertObjectToString(value)}` // Recursion handles nested objects
        })
        return `{${entries.join(",")}}`
    }
    if (typeof object === "object"){
        const entries = Object.entries(object).map(([key, value]) => {
            return `"${key}":${jsonStringify(value)}` // Recursion handles nested objects
        })
        return `{${entries.join(",")}}`
    }



    // console.log("object at bottom", object)

    return false
    
};