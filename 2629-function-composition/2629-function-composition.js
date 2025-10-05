/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        if (functions.length === 0) return x
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

let functions = [ x => x + 1,  x => x * x, x => x * 2]
 const fn = compose(functions)
 fn(4)