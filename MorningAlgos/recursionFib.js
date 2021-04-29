function rfib(num){
    num = Math.floor(num)
    if(num < 0) return 0;
    if(num ==0) return 0;
    if(num == 1) return 1;
    return (rfib(num-2) + rfib(num-1))
}
console.log(rfib(7))
// function rSigma(num){
//     if(num === 1) return 1;
//     return num * rSigma(num -= 1);
// }

// console.log(rSigma(5));



