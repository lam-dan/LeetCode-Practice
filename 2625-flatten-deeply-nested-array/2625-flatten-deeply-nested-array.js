/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // Array map only seeds from left to right, so seed from right to left instead to preserve ordering
    let stack = []
    for (let i = arr.length - 1; i >= 0; i--) {
        stack.push([arr[i], n])
    }
    const res = []

    while (stack.length > 0) {
        const [obj, depth] = stack.pop()
        if (Array.isArray(obj) && depth > 0) {
            for(let i = obj.length - 1; i >= 0; i--) {
                stack.push([obj[i], depth - 1])
            }
        } else {
            res.push(obj)
        }
    }
    return res
};