package main

import "unicode/utf8"

func main() {
	println(len("你好"))                      //输出6
	println(utf8.RuneCountInString("你好"))   //输出 2
	println(utf8.RuneCountInString("你好ab")) //输出4
}
