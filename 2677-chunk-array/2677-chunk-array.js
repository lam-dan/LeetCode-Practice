/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const final = []
    let result = []

    for (let i = 0; i < arr.length; i++) {
        if (result.length === size){
            final.push(result)
            result = []
        }
        result.push(arr[i])
    }

    if(result.length > 0) {
        final.push(result)
    }

    return final
    
};
