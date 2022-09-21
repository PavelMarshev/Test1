if __name__ == "__main__":
    HEIGHT = 190
    WEIGHT = 75
    STEPS_NUMBER = 1000
    ACTIVITY_TIME = 60  # minutes

    step_length = HEIGHT / 4 + 0.37
    distance = step_length * STEPS_NUMBER
    speed = distance / ACTIVITY_TIME

    calories = 0.035 * WEIGHT + speed**2 / HEIGHT * 0.029 * WEIGHT
    if distance < 2:
        then: print('Ходи больше!')
    elif distance < 4 and distance > 2:
        then: print('Уже лучше, но мало!')
    elif distance > 4:
        then: print('Продолжай в том же духе!')
    print(distance)