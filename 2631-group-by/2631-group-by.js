/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let groupMap = {}
    if (this.length === 0){
        return {}
    }
    for (let i = 0; i < this.length; i++) {
        const obj = this[i]
        const id = fn(obj)
        if (Object.hasOwn(groupMap, id)){
            groupMap[id].push(obj)
        } else {
            groupMap[id] = [obj]
        }
    }
    return groupMap
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */