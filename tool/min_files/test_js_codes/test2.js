/** *  
* @param {原始数组} arr  
* @param {按照多长进行分割} len  
*  将一个数组拆分成多个len长度数组 
*/
function split_array(arr, len) {
    var a_len = arr.length;   
    var result = [];    
    for (let i = 0; i < a_len; i += len) {
            result.push(arr.slice(i, i + len));
    }
    return result;
}

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
let s = split_array(arr, 2);
console.log('-----截断后的数组是-----', s);
//-----截断后的数组是----- [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7, 8 ], [ 9 ] ]