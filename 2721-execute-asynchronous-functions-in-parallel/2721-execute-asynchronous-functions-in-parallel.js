/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    if (functions.length === 0) {
        return ([])
    }
    return new Promise( async (resolve, reject) => {
        try {
            const promises = functions.map((n)=> n())
            const results = await Promise.all(promises)
            resolve(results)
        } catch (err) {
            reject(err)
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */