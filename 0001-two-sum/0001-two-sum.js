/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 // target = nums[0] + nums[1];
var twoSum = function(nums, target) {
    let map = new Map();
    let result = [];
    
    nums.forEach((num, i) => {
        const diff = target - num;
        if (map.has(diff) && map.get(diff) !== i) {
            result.push(i, map.get(diff));
        }
        map.set(num, i);
    });

    return result;
};