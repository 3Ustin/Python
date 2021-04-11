// Change is inevitable (especially when breaking a twenty). Make generateCoinChange(cents). 
// Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. 
// Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).  
// Return the given number of coins in an object.


//WORKING FUNCTION
//
// function coins(coins){
//     var array = []
//     var quarterNum = 0;
//     if(coins >= 25){
//         quaterNum = Math.floor(coins/25);
//         coins -= quaterNum * 25;
//     }
//     var dimeNum = 0;
//     if(coins >= 10){
//         dimeNum = Math.floor(coins/10);
//         coins -= dimeNum * 10;
//     }
//     var nickelNum = 0;
//     if(coins >= 5){
//         nickelNum = Math.floor(coins/5);
//         coins -= nickel * 5;
//     }
//     var pennyNum = 0;
//     if(coins >= 1){
//         pennyNum = Math.floor(coins/1);
//         coins -= pennyNum * 1;
//     }
//     array.push(quarterNum);
//     array.push(dimeNum);
//     array.push(nickelNum);
//     array.push(pennyNum);
//     return array;
// }
// console.log(coins(12))




// function coins(coins){
//     //Object to store 
//     var object = {
//         "Quarters": 0,
//         "Dimes": 0,
//         "Nickels": 0,
//         "Pennies": 0
//     }
//     var array = [];
//     var quarterNum = 0;
//     if(coins >= 25){
//         quaterNum = Math.floor(coins/25);
//         coins -= quaterNum * 25;
//         object["Quarters"] = quarterNum;
//     }
//     var dimeNum = 0;
//     if(coins >= 10){
//         dimeNum = Math.floor(coins/10);
//         coins -= dimeNum * 10;
//         object["Dimes"] = dimeNum;
//     }
//     var nickelNum = 0;
//     if(coins >= 5){
//         nickelNum = Math.floor(coins/5);
//         coins -= nickelNum * 5;
//         object["Nickels"] = nickelNum; 
//     }
//     var pennyNum = 0;
//     if(coins >= 1){
//         pennyNum = Math.floor(coins/1);
//         coins -= pennyNum * 1;
//         object["Pennies"] = pennyNum;
//     }
//     array.push(quarterNum);
//     array.push(dimeNum);
//     array.push(nickelNum);
//     array.push(pennyNum);
//     return object;
// }
// console.log(coins(12))



function coins(coins){
    //Object to store 
    var object = {
        "Quarters": 0,
        "Dimes": 0,
        "Nickels": 0,
        "Pennies": 0
    }
    isCoin(coins, 25,"Quarters");
    isCoin(10,"Dimes");
    isCoin(5,"Nickels");
    isCoin(1,"Pennies");
    return object;
}
console.log(coins(12))

//IMPLEMENTING A FUNCTION TO DRY
function isCoin(coins, countNum,key){
    if(coins >= countNum){
        quaterNum = Math.floor(coins/countNum);
        coins -= quaterNum * countNum;
        object[key] = quarterNum;
    }
}