if __name__ == '__main__':
    d = []
    values = set()
    for i in range(int(input())):
        name = input()
        score = float(input())
        d.append((name, score))
        values.add(score)
    values = sorted(values)
    secondLowest = values[1]
    d = sorted(d, key=lambda tup: tup[0])

    for key, value in d:
        if value == secondLowest:
            print(key)


