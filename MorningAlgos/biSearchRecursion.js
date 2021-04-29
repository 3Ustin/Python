function biSearch(arr,num){
    let start = 0, end = arr.length - 1;
    while(start <=end){
        let mid = Math.floor((start+end)/2);
        if(arr[mid] < num){
            return true;
        }
        else if (arr[mid] < num){
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }
    return false;
}

console.log(biSearch([1,3,5,7],4));