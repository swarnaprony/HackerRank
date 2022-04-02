if __name__ == '__main__':
    number_english = int(input("Number of students English: "))
    english_roll = set(input("Roll of students English: ").split())
    number_french = int(input("Number of students English: "))
    french_roll = set(input("Roll of students English: ").split())
    total_subscription = len(english_roll) + len(french_roll) - len((english_roll.intersection(french_roll)))
    print(total_subscription)

    print(number_english)
    print(len(english_roll))
    print(number_french)
    print(len(french_roll))
    print(len(english_roll.intersection(french_roll)))
    print(len(english_roll.union(french_roll)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    number_english = int(input())
    english_roll = set(map(str,input().split()))
    number_french = int(input())
    french_roll = set(map(str, input().split()))
    total_subscription = len(english_roll.union(french_roll))
    print(total_subscription)