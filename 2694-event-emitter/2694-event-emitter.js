class EventEmitter {
    constructor() {
        this.events = {} // keys are events, values are array of cb functions as their corresponding values
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
     // callbacks = event handlers
    subscribe(eventName, callback) {
        if (!Object.hasOwn(this.events, eventName)) {
            this.events[eventName] = []
        }
        this.events[eventName].push(callback)

        return {
            unsubscribe: () => {
                this.events[eventName] = this.events[eventName].filter((fn) => fn !== callback) // need to reassign because this is a new array
                // Avoid memory leaks if we filter out all call backs
                // and there are none left for matching our current callback
                if (this.events[eventName].length === 0) {
                    delete this.events[eventName]
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let result = []
        if (Object.hasOwn(this.events, eventName)){
            this.events[eventName].map((fn) => {
                result.push(fn(...args));
            })
        } else {
            return []
        }   
        return result
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */