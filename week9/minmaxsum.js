let miniMaxSum = (arr) => {
    arr.sort((a,b) => a - b);
    let a = arr.reduce((a,b) => a +b,0) - arr[arr.length-1]
    let b = arr.reduce((a,b) => a +b,0) - arr[0]
    return `${a} ${b}`

}

console.log(miniMaxSum([1,2,3,4,5]))
console.log(miniMaxSum([7,69, 2, 221, 8974]))