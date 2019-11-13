def mod(a, b):
    while(a>b):
        a = a - b
    return a

def main():
    time = input()
    words = time.split(':')
    if len(words) < 2:
        #print("0:0")
        return -1
    hours = int(words[0])
    if hours < 1 or hours > 100:
        #print("0:0")
        return -1
    minutes = int(words[1])
    if minutes < 0 or minutes > 100000:
        #print("0:0")
        return -1


    M = int(input())
    if M < 1 or M > 10000:
        return -1
    H = int(input())
    if H < 1 or H > 10000:
        return -1

    total_time = minutes + hours*H
    result = total_time/M
    result_h = result//60
    result_m = result - result_h*60
    print(str(int(mod(result_h, 24))) + ":" + str(int(result_m)))
    return result

main()
