package main

import (
	"fmt"
	"strconv"
	"io/ioutil"
)

func proddigits(str string) int {
	ans := 1
	for i := 0; i < len(str); i++ {
		num, err := strconv.Atoi(string(str[i]))
		if err != nil {
			fmt.Print(err)
		}
		ans = ans*num
	}
	return ans
}

func main() {
	b, err := ioutil.ReadFile("data.txt")
	if err != nil {
		fmt.Print(err)
	}

	str := string(b)
	maxnum := 0
	maxset := ""
	for i:=12; i<1000; i++ {
		substring := str[i-12:i+1]
		a := proddigits(substring)
		if maxnum < a {
			maxnum = a
			maxset = substring
			//fmt.Println(substring)
		}
	}
	fmt.Println(maxnum)
	fmt.Println(maxset)
}