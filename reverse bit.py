def rev(btValue):
    btValue = (btValue>>3) | (btValue<<4)
    btValue = ((btValue & 0x4C)>>2) | ((btValue & 0x03)<<2)|((btValue & 0x30)<<1)
    btValue = ((btValue & 0x4A )>>1) | ((btValue & 0x25)<<1)|(btValue & 0x10)
    return btValue

# for i in range(128):
#     print(i, rev(i))

def rev_64(input_index):
    input_index = (input_index >> 3) | (input_index << 3)
    input_index = ((input_index & 0x1B) << 1) | ((input_index & 0x24) >> 2)
    input_index = ((input_index & 0x24) >> 1) | ((input_index & 0x12) << 1) | (input_index & 0x09)
    return bin(input_index)

for i in range(64):
    s = bin(i)
    if len(s) < 8:
        s = s[0:2]+'0'*(8-len(s))+s[2:]
    s_ = rev_64(i)
    if len(s_) < 8:
        s_ = s_[0:2] + '0'*(8-len(s_)) + s_[2:]
    print(s, s_, s==(s_[0:2]+s_[2:][::-1]))