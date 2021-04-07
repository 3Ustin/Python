function palindrome(str) {
    var longPal = "";
    var temp = str;
    var array = str.split("");
    for(var i = 0; i < array.length; i++){
        var k = 1
        var isChecking = true
        while(isChecking == true){
            isChecking = false;
            if(array[i-k] == array[i+k]){
                isChecking = true
                longPal = temp.substr(i-k,i+k);
            }
            k++
        }
    }
    array = array.reverse();
    array= array.join("");
    if(array == temp){
        return(longPal);
    }
    else {
        return(longPal);
    }
}

console.log(palindrome("happy, gog, racecarqwertyuiopoiuytrewq"));
console.log(palindrome("racecarracecarracecar lsakfj ;aklhdf am; fie qwertyuiopoiuytrewqdakj  zxcvbnm,./';lkjhgfdsasdfghjkl;'/.,mnbvcxz"));