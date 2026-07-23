import random

def play_game():
    choices = ["가위", "바위", "보"]
    computer = random.choice(choices)
    
    player = input("가위, 바위, 보 중 하나를 입력하세요: ")
    print(f"컴퓨터: {computer} vs 당신: {player}")
    
    if player == computer:
        print("비겼습니다!")
    # TODO: 승패 로직 구현 필요
    
if __name__ == "__main__":
    play_game()