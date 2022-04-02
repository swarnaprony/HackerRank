if __name__ == '__main__':
    number_english = int(input())
    english_roll = set(map(int,input().split()))
    number_french = int(input())
    french_roll = set(map(int,input().split()))
    total_subscription = number_english + number_french - len((english_roll.intersection(french_roll)))
    print(total_subscription)