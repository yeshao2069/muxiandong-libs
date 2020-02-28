let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
/** *  
* @param {*原始数组} arr  
* @param {*字符串中夹杂的字符，可以为空‘’} sp_str  
* 数组转字符串 
**/
function ArrayToString(arr, join_str) {
    return arr.join(join_str);
}
let join_str = '';
let newarr = ArrayToString(arr, join_str);
console.log('-----ArrayToString', newarr);