func searchInsert(nums []int, target int) int {
    var pos int
    
    for i, v := range nums {
        if target <= v {
            pos = i
            break
        }
    pos = len(nums)
    }
    
    return pos
}
