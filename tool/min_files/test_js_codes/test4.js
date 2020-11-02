/** *  
* @param {*字符串数组} strArr 
*/
let strArr = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ];
function strArrToNumArr(strArr) {
    let NumArr = [];
        for (let i = 0; i < strArr.length; ++i) {
                NumArr.push(parseInt(strArr[i]));    
       } 
          return NumArr;
}
let NumArr = strArrToNumArr(strArr);
console.log('------strArrToNum', NumArr);