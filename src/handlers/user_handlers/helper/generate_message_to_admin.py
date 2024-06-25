from aiogram.types import Message


def generate_message_to_admin(message: Message) -> str:
    return f"""
           #id{message.from_user.id}
           <br/>
           #msgid{message.message_id}
           <br/>
           <kbd>
           username: {message.from_user.username}
           <br/>
           first_name: {message.from_user.first_name}
           <br/>
           last_name: {message.from_user.last_name}
           <br/>
           language_code: {message.from_user.language_code}
           <br/>
           </kbd>
           <br/>
            """


__all__ = ["generate_message_to_admin"]
