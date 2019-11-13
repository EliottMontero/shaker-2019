
def main():
    p = int(input())
    if p < 0 or p > 1000000:
        return -1
    b = int(input())
    if b < 0 or b > 1000000:
        return -1
    f = int(input())
    if f < 0 or f > 1000000:
        return -1
    result = p - 4*b - 500*f
    if result < 0:
        result = 0
    print(result)
    return result

main()
