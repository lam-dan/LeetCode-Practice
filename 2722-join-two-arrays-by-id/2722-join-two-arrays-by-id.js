/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const newMap = new Map()
    for (obj of arr1) {
        newMap.set(obj.id, obj)
    }

    for (obj of arr2) {
        if (!newMap.has(obj.id)) {
            newMap.set(obj.id, obj)
        } else {
            // Merging Logic
            // Any mapping keys in our object have to be override by the current obj
            // Grab previous object

            const prevObj = newMap.get(obj.id)
            const merged = structuredClone({...prevObj, ...obj})
            newMap.set(obj.id, merged)
        }
    }
    console.log("newMap", Object.values(Object.fromEntries(newMap)))
    return Object.values(Object.fromEntries(newMap))
};