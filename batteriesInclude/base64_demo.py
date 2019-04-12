"""
    base64是一种用64种字符表示二进制数据的方法，64种字符分别是A-Z，a-z，0-9，+，/
    将二进制数据每三个字节组成一组，3 * 8bit = 24bit，然后除以6，化成4组，每组6bit
    每组的6bit作为索引，查base64表，得到相应的四个字符，全部转化后的到字符串。
    base64会3字节的二进制数转化为4个字节，长度增加33%
    当二进制数据长度不是3的倍数的时候，base64会用\x00字节补足，然后在末尾加上1个或者2个‘=’号，表示补了几个字节，解码的时候会自动去掉
"""

import base64
import json

if __name__ == '__main__':
    bs = bytes('我', encoding='utf-8')
    print(len(bs), bs)
    b64 = base64.b64encode(bs)
    s64 = str(b64, encoding='utf-8')
    print(s64)
    bsu = bytes('我', encoding='unicode')
    print(len(bsu), bsu)
    json.dumps()
