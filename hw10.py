import pickle

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f"#{i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("개인점수:", end=' ')
    for score in scores:
        print(score, end=' ')
    print()
    print(f"평균: {get_average(scores):.1f}")

def save_scores(scores):
    with open("score.bin", "wb") as file:
        pickle.dump(scores, file)

def load_scores():
    with open("score.bin", "rb") as file:
        return pickle.load(file)

def main():
    try:
        scores = load_scores()
        print("[파일 읽기]")
    except:
        print("[점수 입력]")
        scores = input_scores()
        save_scores(scores)

    print("\n[점수 출력]")
    show_scores(scores)

main()
