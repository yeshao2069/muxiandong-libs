let testArr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
 let needFindData = [4, 5, 9];
 function IsHaveData(srcArr, checkArr) {
     let checklen = checkArr.length;
     let checkArrCnt = 0;    
     let bIsFindData = false;    
     let tempSrcArr = testArr.concat();    
     for (let i = 0; i < checkArr.length; ++i) {
             for (let j = 0; j < tempSrcArr.length; ++j) {
                         if(checkArr[i] === tempSrcArr[j]) { 
                                        ++checkArrCnt;                
                                        tempSrcArr.splice(j, 1);                
                                        if(checkArrCnt === checklen){
                                                            bIsFindData = true;                    
                                                            console.log('已经全部找到');                    
                                                            break;                
                                                            }            
                    }        
      }    
    }    //return {result:bIsFindData, remainArr: tempSrcArr};    
    if(bIsFindData){
           srcArr.length = 0;
           for (let j = 0; j < tempSrcArr.length; ++j) {
                 srcArr.push(tempSrcArr[j]);
          }
   }
   return bIsFindData;
}
let obj = IsHaveData(testArr, needFindData);
console.log('testArr',testArr);
console.log("--obj--%o", obj);