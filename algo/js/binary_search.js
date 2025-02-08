function binary_search(list_element, target) {
  let low = 0
  let high = list_element.length - 1
  while (low <= high) {
    let mid = Math.trunc((high+low)/2)
    console.log("mid: "+mid)
    if (list_element[mid] === target){
      return mid
    }
    if (list_element[mid] < target){
      low = mid + 1
    }
    if (list_element[mid] > target){
      high = mid - 1
    }
  }
  return null
}
let test = [ 1,2,3,4,5,6,7,8,8,45,66,67,87,90,123,234,300,350,400]
console.log(binary_search(test, 401))
console.log(binary_search(test, 8))
console.log(binary_search(test, 66))
