# J,A.R.V.I.S created by Anirudha BS

from modules.chat_pairs import chat_pairs
from modules.converse import Chat, reflections

pairs = chat_pairs()

print("Hi, I'm Jarvis, Your personal assistant\nSay quit to leave")

chat = Chat(pairs, reflections)

chat.converse()
