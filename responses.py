from TrainDelayFunction import TrainDelays


def handle_response(message: str) -> str:

    p_message = message.lower()


    if p_message == f'!delay':
        default_FROM = "WRONKI"
        default_To = "POZNAŃ GŁÓWNY"
        return TrainDelays(default_FROM, default_To)

    FROM, TO = p_message.split()[1], p_message.split()[2]

    print(FROM,TO)

    if p_message == "!delay" + ' ' + FROM + ' ' + TO:
        return TrainDelays(FROM, TO)

    if p_message == 'help':
        return "Default start station is WRONKI, default destination station is POZNAŃ GŁÓWNY, if you would like to check delays between those, you can use '!delays'. To change start and destination stations use '!delays FROM_STATION TO_STATION'"

    else:
        return "I don't know this command, please use !help"

