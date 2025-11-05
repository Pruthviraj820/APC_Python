def count_char(s,ch):
    parts = []
    for i in range(len(s)):
        if s[i]!=ch:
            parts.append(s[i])
        result="".join(parts)
    return result
if __name__ == "__main__":
    s = "a b c d"
    ch = " "
    print(count_char(s, ch))