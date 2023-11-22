def time_to_text(number: int):
    hour = int(number / 60)
    minutes = number % 60
    print(f"{hour} heures and {minutes} minutes")

time_to_text(545)
time_to_text(55)
time_to_text(1238)
time_to_text(6721)