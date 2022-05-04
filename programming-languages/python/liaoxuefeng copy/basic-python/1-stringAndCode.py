#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# use ord
print(ord('A'), ord('中'))

# use chr
print(chr(65), chr(20013))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# 'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

x = b'ABC'

# use encode
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'

# use decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# use len
# 计算str包含多少个字符
print(len('ABC'), len('中文'))

# bytes，len()函数就计算字节数
len(b'ABC')  # 3
len(b'\xe4\xb8\xad\xe6\x96\x87')  # 6
len('中文'.encode('utf-8'))  # 6

# 操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：见开头

# 格式化输出
print('Hello, %s' % 'world\n', 'Hi, %s, you have $%d.' % ('Michael', 1000000))



