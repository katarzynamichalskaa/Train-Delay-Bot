from TrainDelayFunction import TrainDelays


def handle_response(message: str) -> str:

    p_message = message.lower()

    if p_message == '!delay':
        return TrainDelays()

