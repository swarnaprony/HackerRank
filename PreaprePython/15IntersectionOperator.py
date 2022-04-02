# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    number_english = int(input())
    english_roll = set(map(str,input().split()))
    number_french = int(input())
    french_roll = set(map(str, input().split()))
    total_subscription = len(english_roll.intersection(french_roll))
    print(total_subscription)