from TrainDelayFunction import TrainDelays


def handle_response(message: str) -> str:

    p_message = message.lower()

    if p_message == '!delay':
        if TrainDelays() == 1:
            return 'There are no delays'
        else:
            return 'There are delays'
