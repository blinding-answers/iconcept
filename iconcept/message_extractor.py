from typing import Union


def extract_datagram(message: str, header: str, length: int) -> Union[str, None]:
    header_upper = header.upper()
    message_upper = message.upper()
    if header_upper not in message_upper:
        return None

    start_of_header = message_upper.index(header_upper)
    extracted_message = message[start_of_header:start_of_header + length]
    if len(extracted_message) < length:
        return None

    return extracted_message
