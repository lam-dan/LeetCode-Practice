/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) return arr
    let res = [];
    for (const ele of arr) {
        if (Array.isArray(ele)) {
            res.push(...flat(ele, n-1))
        }
        else {
            res.push(ele)
        }
    }
    return res
};