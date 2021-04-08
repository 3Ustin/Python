function bookIndex(arr){
    for(var i = 0; i < arr.length; i++){
        k = 1;
        var array = []
        var location = 0;
        var locationRange = 0;
        var isChecking = true
        while(isChecking == true){
            isChecking = false;
            if(arr[i+k] == arr[i] + k){
                isChecking = true
                location= arr[i];
                locationRange = arr[i + k]
            }
            k++
            console.log("'" + location + "-" + locationRange);
        }
        i += k;
    }
}
bookIndex([1,13,14,15,37,38,70]);
// function bookIndex(arr){
//     array = []
//     for(var i = 0; i < arr.length; i++){
//         var j = i;
//         var k = 0;
//         while(arr[i] + k == arr[i + k]){
//             k++;
//             j++;
//         }
//             array.push(arr[i]+k);
//             array.push(arr[j]);
//     }
//     console.log(array);
// }
//             if(arr[i+k] == arr[i] + k){
//                 isChecking = true
//                 location= arr[i];
//                 locationRange = arr[i + k]
//             }
//             k++
//             console.log("'" + location + "-" + locationRange);
//         }

//     }
// }