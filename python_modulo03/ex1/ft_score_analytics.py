import sys

if __name__ == "__main__":
    list_int = []
    for arg in sys.argv[1:]:
        try:
            int(arg)
            list_int.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if len(list_int) > 0:
        print(f"Scores processed: {list_int}")
        print(f"Total players: {len(list_int)}")
        print(f"Total score: {sum(list_int)}")
        print(f"Avarage score: {sum(list_int) / len(list_int)}")
        print(f"High score: {max(list_int)}")
        print(f"Low score: {min(list_int)}")
        print(f"Score range: {max(list_int) - min(list_int)}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")