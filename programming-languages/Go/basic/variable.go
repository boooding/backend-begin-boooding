package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("hello, golang")
	variableZeroValue()
	var (
		aa = 3
		bb = 4
	)
	fmt.Println(aa, bb)
}

func variableZeroValue() {
	var a int
	var b string
	fmt.Printf("%d %q\n", a, b)
	variableTypeDeduction()
}

func variableTypeDeduction() {
	var a, b, c, d = 3, 4, true, "a"
	fmt.Println(a, b, c, d)
	variableShorter()
}

func variableShorter() {
	a, b, c, d := 3, 4, true, "a"
	fmt.Println(a, b, c, d)
	typeForeChange()
}

// build-in variable
// bool string
// (u)int, (u)int8, (U)int16, (u)int32, (u)int64, uintptr
// byte(8), rune(32)
// float32, float64, complex64, complex128

// type
func typeForeChange() {
	var a, b = 3, 4
	var c int
	c = int(math.Sqrt(float64(a*a + b*b)))
	fmt.Println(c)
	enums()
}

// const
// enums
func enums() {
	const (
		cpp = iota
		java
		python
		golang
	)
	fmt.Println(cpp, java, python, golang)
	const (
		b = 1 << (10 * iota)
		kb
		mb
		gb
		tb
		pb
	)
	fmt.Println(b, kb, mb, gb, tb, pb)
}
