from aiogram.types import Message


def generate_edited_message(message_data) -> str:
    return f"""
           #id{message_data['user_id']}
           <br/>
           #msgid{message_data['msg_id']}
           <br/>
           <kbd>
           username: {message_data['username']}
           <br/>
           first_name: {message_data['first_name']}
           <br/>
           last_name: {message_data['last_name']}
           <br/>
           language_code: {message_data['language_code']}
           <br/>
           </kbd>
           <br/>
           {message_data['user_message']}
           <br/>
            """


__all__ = ["generate_edited_message"]
