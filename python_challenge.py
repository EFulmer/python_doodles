def zero():
    return 2 ** 38

def one():
    from string import ascii_lowercase
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    rot2 = ''

    for c in text:
        if c in ascii_lowercase:
            c_pos = ascii_lowercase.find(c)
            rot2 += ascii_lowercase[ (c_pos + 2) % 26 ]
        else:
            rot2 += c

    return rot2

def one_alt():
    from string import ascii_lowercase
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    rot2 = ascii_lowercase[2:] + ascii_lowercase[:2]
    trans_tbl = str.maketrans(ascii_lowercase, rot2)
    return text.translate(trans_tbl)
