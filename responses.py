from TrainDelayFunction import TrainDelays


def handle_response(message: str) -> str:

    p_message = message.lower()

    if p_message == f'!delay':
        default_FROM = "WRONKI"
        default_To = "POZNAŃ GŁÓWNY"
        return TrainDelays(default_FROM, default_To)

    if p_message == '!help':
        return "Default start station is WRONKI, default destination station is POZNAŃ GŁÓWNY, if you would like to check delays between those, you can use just '!delays'. " \
               "To change start and destination stations use '!delays FROM_STATION TO_STATION'. If your choosen station is a two-part word, please enter it like this: 'POZNAŃ_GŁÓWN'"

    FROM, TO = p_message.split()[1], p_message.split()[2]

    if p_message == "!delay" + ' ' + FROM + ' ' + TO:
        return TrainDelays(FROM.strip().replace('_', ' '), TO.strip().replace('_', ' '))
    else:
        return None

