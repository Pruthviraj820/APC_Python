def count_char(s, ch):
    count = 0
    for i in range(len(s)):
        if s[i] == ch:
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    ch = input().strip()
    print(count_char(s, ch))
