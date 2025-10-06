/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // Base Case
    if (n === 0) {
        return arr
    }
    let result = []
    for (let i = 0; i < arr.length; i++) {
        const obj = arr[i]
        if (Array.isArray(obj)){
            result.push(...flat(obj, n - 1))
        } else {
            result.push(arr[i])
        }
    }
    return result
};