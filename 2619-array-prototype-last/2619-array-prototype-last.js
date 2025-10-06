/**
 * @return {null|boolean|number|string|Array|Object}
 */

 // "this" always calls the object that called this prototype function
Array.prototype.last = function() {
    if(this.length === 0){
        return -1
    }
    return this.at(-1)
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */