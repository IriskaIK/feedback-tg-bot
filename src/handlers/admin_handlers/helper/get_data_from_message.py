import re
from aiogram.types import Message

ID_PATTERN = re.compile(pattern=r"#id\d{1,}[\s]?")
MESSAGE_ID_PATTERN = re.compile(pattern=r"#msgid\d{1,}[\s]?")
USERNAME_PATTERN = re.compile(r"username:\s(\S+)")
FIRST_NAME_PATTERN = re.compile(r"first_name:\s([^\n]+)")
LAST_NAME_PATTERN = re.compile(r"last_name:\s([^\n]+)")
LANGUAGE_CODE_PATTERN = re.compile(r"language_code:\s(\S+)")
USER_MESSAGE_PATTERN = re.compile(r"language_code:\s\S+\n\n(.+?)(?:\nAnswered🟢)?$", re.DOTALL)

def extract_id(message: Message) -> dict:
    text = (message.text if message.text else message.caption)
    # .replace("Not Answered🔴", "Answered🟢")
    user_id_match = ID_PATTERN.search(text)
    msg_id_match = MESSAGE_ID_PATTERN.search(text)
    username_match = USERNAME_PATTERN.search(text)
    first_name_match = FIRST_NAME_PATTERN.search(text)
    last_name_match = LAST_NAME_PATTERN.search(text)
    language_code_match = LANGUAGE_CODE_PATTERN.search(text)
    user_message_match = USER_MESSAGE_PATTERN.search(text)
    answered_match = "Answered🟢" in text


    u_id = int(user_id_match.group().replace("#id", "")) if user_id_match else None
    m_id = int(msg_id_match.group().replace("#msgid", "")) if msg_id_match else None
    username = username_match.group(1) if username_match else None
    first_name = first_name_match.group(1) if first_name_match else None
    last_name = last_name_match.group(1) if last_name_match else None
    language_code = language_code_match.group(1) if language_code_match else None
    user_message = user_message_match.group(1).strip() if user_message_match else None

    return {
        "user_id": u_id,
        "msg_id": m_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "language_code": language_code,
        "user_message": user_message,
        "answered": answered_match
    }


__all__ = ["extract_id"]
