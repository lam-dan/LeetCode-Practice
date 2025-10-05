/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let result = new Array(26)
    let size = 0

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            result[size] = arr[i]
            size++
        }
    }
    while (size < result.length) {
        result.pop()
    }
    return result
};

// function greaterThan10(n) {
//     return n > 10
// }

// filteredArr(arr, greaterThan10) // [10, 20]