function overAchievers(str){
    //PARENTH
    countParenth = 0;
    countSquig = 0;
    countBracket = 0;
    //LOOP
    for(var i = 0; i<str.length;i++){

            //TESTING FOR SWITCH STATEMENTS::
        // switch(str.charAt(i)){
        //     case "(":
        //         countParenth ++;
        //         break;
        //     case ")":
        //         countParenth --;
        //         break;
        //     case "{":
        //         countSquig ++;
        //         break;
        // }


        //PARENTH
        if(str.charAt(i) == "("){
            countParenth += 1;
        }
        if(str.charAt(i) == ")"){
            countParenth -= 1;
        }
        if(countParenth < 0){
            return false;
        }
        //SQUIGILLY
        if(str.charAt(i) == "{"){
            countSquig += 1;
        }
        if(str.charAt(i) == "}"){
            countSquig -= 1;
        }
        if(countSquig < 0){888
            return false;
        }
        //BRACKETS
        if(str.charAt(i) == "["){
            countBracket += 1;
        }
        if(str.charAt(i) == "]"){
            countBracket -= 1;
        }
        if(countBracket < 0){
            return false;
        }
    }
    return(countParenth != 0 || countSquig != 0 || countBracket !=0)
    
}
console.log(overAchievers("[](){}}"));