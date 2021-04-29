// function rSigma(num){
//     if(num === 1) return 1;
//     return num * rSigma(num -= 1);
// }

// console.log(rSigma(5));


function rSigma(arr){
    if(arr.length === 0) return arr;
    arr.pop();
    console.log(arr);
    return rSigma(arr);
    
}

var array = [0,1,2,3,4,5];
console.log(rSigma(array));