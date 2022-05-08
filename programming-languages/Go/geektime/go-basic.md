 ## 包声明
 1. 语法形式：package xxxx 
 2. 字母和下划线的组合 
 3. 可以和文件夹不同名字 
 4. 同一个文件夹下的声明一致
 5. 引入包语法形式：import [alias] xxx 
 6. 如果一个包引入了但是没有使用，会报错 
 7. 匿名引入：前面多一个下划线

## string
len:
- string 的长度很特殊：
- 字节长度：和编码无关，用 len(str)获取
- 字符数量：和编码有关，用编码库来计算
```go
import "unicode/utf8"

func main() {
    println(len( "你好"))/ /输出6
    println(utf8.RuneCountInString("你好"))//输出 2
    println(utf8.RuneCountInString("你好ab"))//输出4
}
```

### strings
string 的拼接直接使用+号就可以。golang不支持string和别的类型拼接。
1. 查找和替换 
2. 大小写转换 
3. 子字符串相关 
4. 相等

### rune