from math import pi

def main():
    tape_length = int(input())
    ball_num = int(input())
    balls = []
    
    for i in range(ball_num):
        ball = input().split()
        balls.append([int(ball[1])*2*pi, int(ball[0])])    
    balls.sort()

    total = 0
    for ball in balls:
        while ball[1] > 0:
            if tape_length >= ball[0]:
                tape_length -= ball[0]
                ball[1] -= 1
                total += 1
            else:
                break
    print(total)
        

main()