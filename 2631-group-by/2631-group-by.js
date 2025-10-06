/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let groupMap = new Map()
    if (this.length === 0){
        return {}
    }
    for (let i = 0; i < this.length; i++) {
        const obj = this[i]
        const id = fn(this[i])
        if (groupMap.has(id)){
            groupMap.set(id, [...groupMap.get(id), obj])
        } else {
            groupMap.set(id, [obj])
        }
    }
    return Object.fromEntries(groupMap)
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */