package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

func main() {
	const filename = "/Users/boodingtang/Desktop/backend-begin-boooding/programming-languages/go/basic/test.txt"
	//
	contents, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("%s\n", contents)
	}
	// or
	if contents, err := ioutil.ReadFile(filename); err == nil {
		fmt.Println(string(contents))
	} else {
		fmt.Println(err)
	}
}

// switch
func eval(a, b int, op string) int {
	var result int
	switch op {
	case "+":
		result = a + b
	case "-":
		result = a - b
	case "*":
		result = a * b
	case "/":
		result = a / b
	default:
		panic("unsupported operator:" + op)
	}
	return result
}

// for
func sum100() {
	sum := 0
	for i := 1; i < 100; i++ {
		sum = sum + i
	}
	fmt.Println(sum)
}

func DecimalToBinary(n int) string {
	result := ""
	for ; n > 0; n /= 2 {
		lsb := n % 2
		result = strconv.Itoa(lsb) + result
	}
	return result
}

func printFile(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
