function diagonalDifference(arr) {
    // Write your code here
    if(arr.length == 9){
        let d1 = arr[0] + arr[4] + arr[8]
        let d2 = arr[2] + arr[4] + arr[6]
        let difference = d1 - d2;
        if(difference < 0){
            difference *= -1
        }
        return difference
    }

}
array = [11,2 ,4
    ,4 ,5 ,6
    ,10 ,8 ,-12]

diagonalDifference(array)

    
