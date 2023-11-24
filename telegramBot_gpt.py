import telegram
import asyncio
from openai import OpenAI

client = OpenAI(
        api_key='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'
        )

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

token = "6721469751:AAFB8RMFOy3NXaTjTVDdJ_sy8S9i8hPEO58"
bot = telegram.Bot(token = token)

text = completion.choices[0].message.content
public_chat_name = '@hxrintest'
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(bot.sendMessage(chat_id = public_chat_name, text = text))
