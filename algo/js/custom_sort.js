// quick sort
function quick_sort(nums, low, high) {
  if (low >= high) {
   return nums 
  }
  let i = partitions(nums, low, high)
  quick_sort(nums, 0, i-1)
  quick_sort(nums, i+1, high)
  return nums
}
function partitions(nums, low, high) {
  pivot = nums[high]
  let i = low
  let j = low
  while (j<high) {
    if (nums[j] < pivot) {
      [nums[j], nums[i]] = [nums[i], nums[j]] 
      i++
    }
    j++
  }
  [nums[i], nums[high]] = [nums[high], nums[i]] 
  return i
}

// merge sort
function merge_sort(nums) {
  if (nums.length <= 1) {
    return nums
  }
  let mid = Math.trunc(nums.length/2)
  return merge( 
    merge_sort(nums.slice(0, mid)),
    merge_sort(nums.slice(mid))
  ) 
}
function merge(nums_1, nums_2) {
  let i = 0
  let j = 0
  let res = []
  while(i < nums_1.length && j < nums_2.length){
    if (nums_1[i]<=nums_2[j]) {
      res.push(nums_1[i])
      i++
    } else {
      res.push(nums_2[j])
      j++
    }
  }
  if (i < nums_1.length) {
    res = res.concat(nums_1.slice(i))
  } else if (j < nums_2.length){
    res = res.concat(nums_2.slice(j))
  }
  return res
}

// bubble sort
function bubble_sort(nums) {
  let i = nums.length-1
  let sorted = false
  while(i > 0 && !sorted){
    sorted = true
    for (let j = 0; j < i; j++) {
     if (nums[j] > nums[j+1]) {
       [nums[j], nums[j+1]] = [nums[j+1], nums[j]]
       sorted = false
     } 
    }
    i--
  }
  return nums
}

// insert sort
function insert_sort() {
}

// selection sort
function selection_sort() {
}

// test
let list = [23, 87, 15, 92, 44, 78, 36, 11, 55, 90, 62, 5, 31, 74, 98, 20, 66, 47, 83, 29]
console.log("quick_sort")
console.log(quick_sort(list, 0, list.length-1))
console.log("merge_sort")
console.log(merge_sort(list))
console.log("bubblesort")
console.log(bubble_sort(list))
console.log("insert_sort")
console.log(insert_sort())
console.log("selection_sort")
console.log(selection_sort())
