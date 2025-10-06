/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // Base Case
    let result = []
    function dfs(arr, n) {
        for (let i = 0; i < arr.length; i++) {
            const obj = arr[i]
            if (Array.isArray(obj) && n > 0){
                dfs(obj, n - 1)
            } else {
                result.push(obj)
            }
        }
    }
    dfs(arr, n)
    return result
};