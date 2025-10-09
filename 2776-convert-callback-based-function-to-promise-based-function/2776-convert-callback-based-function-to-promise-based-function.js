/**
 * @param {Function} fn
 * @return {Function<Promise<number>>}
 */
var promisify = function(fn) {
    return function(...args) {
        return new Promise((resolve, reject) => {
            function callback(result, error) {
                if(error) {
                    reject(error)
                } else {
                    resolve(result)
                }
            }
            fn(callback,...args)
        })
    }
};

/**
 * const asyncFunc = promisify(callback => callback(42));
 * asyncFunc().then(console.log); // 42
 */