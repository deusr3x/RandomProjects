package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(num int) bool {
	strnum := strconv.Itoa(num)
	// fmt.Println(strnum)
	// fmt.Println(len(strnum))
	// fmt.Println(len(strnum)/2)
	leng := len(strnum)
	for i:=0; i < len(strnum)/2; i++ {
		if strnum[i] != strnum[leng-1 - i] {
			return false
		}
		
	}
	return true
}

func main() {
	// fmt.Println(isPalindrome(9009))
	// fmt.Println(isPalindrome(91019))
	// fmt.Println(isPalindrome(910134))
	k:=0
	for i:=999; i > 99; i-- {
		for j:=999; j > 99; j-- {
			ans := isPalindrome(i*j)
			if ans {
				// fmt.Println(ans)
				// fmt.Println(i*j)
				// fmt.Println(i)
				// fmt.Println(j)
				if k < i*j {
					k = i*j
				}
			}
		}
	}
	fmt.Println(k)
}