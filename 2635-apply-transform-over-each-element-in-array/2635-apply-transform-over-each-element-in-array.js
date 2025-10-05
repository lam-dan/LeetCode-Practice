/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArray = Array.from({length:arr.length})
    
    for (let i = 0; i < arr.length; i++){
        newArray[i] = fn(arr[i], i )
    }
    return newArray
};


function plusOne(n) {
    return n + 1
}

map([1,2,3], plusOne)