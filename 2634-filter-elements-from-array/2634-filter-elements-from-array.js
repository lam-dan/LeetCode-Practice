/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let result = []
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            result = [...result, arr[i]]
        }
    }
    return result
};

// function greaterThan10(n) {
//     return n > 10
// }

// filteredArr(arr, greaterThan10) // [10, 20]