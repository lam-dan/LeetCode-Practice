/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    console.log("functions", functions)

    return function(x) {
        let accum = x
        for(let i = functions.length-1; i >= 0; i--){
            accum = functions[i](accum)
        }
        return accum
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */