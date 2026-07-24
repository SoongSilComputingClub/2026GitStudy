import random

def play_game():
    choices = ["가위", "바위", "보"]
    computer = random.choice(choices)
    
    player = input("가위, 바위, 보 중 하나를 입력하세요: ")
    print(f"컴퓨터: {computer} vs 당신: {player}")
    
    if player == computer:
        print("비겼습니다!")
    elif(player=="가위" and computer=="보") or \
        (player=="바위" and computer=="가위") or \
        (player=="보" and computer=="바위"):
          print("당신의 완벽한 승리!")
    else:
      print("컴퓨터의 승리!")
    
if __name__ == "__main__":
    play_game()