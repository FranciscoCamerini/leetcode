package main

import (
	"fmt"
)

func isPalindrome(x int) bool {
	str := fmt.Sprint(x)
	reverse_str := ""

	for i := len(str); i > 0; i-- {
		reverse_str += string(str[i-1])
	}

	return str == reverse_str
}

func main() {
	fmt.Println(isPalindrome(121))
}
