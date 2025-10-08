/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null){
        return "null"
    }

    if (Array.isArray(object)) {
        const elements = object.map((element) => jsonStringify(element))
        return `[${elements.join(',')}]`
    }

    if (typeof object === "object") {
        const result = Object.entries(object).map(([key, value]) =>
            `"${key}":${jsonStringify(value)}`);
        return `{${result.join(',')}}`;
    }

    if (typeof object === 'string') {
        return `"${object}"`
    }
    return String(object)
    
};