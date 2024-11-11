#!/usr/bin/python3
# ChatGTP-Tarot script to get readings

from openai import OpenAI
import random
import json
import sys

apikey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Get your API key from the OpenAI website

cards = {
	"The fool": "fool",
	"The magician": "magician",
	"The high priestess": "priestess",
	"The empress": "empress",
	"The emperor": "emperor",
	"The hierophant": "hierophant",
	"The lovers": "lovers",
	"The chariot": "chariot",
	"Strength": "strength",
	"The hermit": "hermit",
	"The wheel of fortune": "wheel",
	"Justice": "justice",
	"The hanged man": "hanged",
	"Death": "death",
	"Temperance": "temperance",
	"The devil": "devil",
	"The tower": "tower",
	"The star": "star",
	"The moon": "moon",
	"The sun": "sun",
	"Judgement": "judgement",
	"The world": "world",
	"Two of Cups": "cups",
	"Three of Cups": "cups",
	"Four of Cups": "cups",
	"Five of Cups": "cups",
	"Six of Cups": "cups",
	"Seven of Cups": "cups",
	"Eight of Cups": "cups",
	"Nine of Cups": "cups",
	"Ten of Cups": "cups",
	"Ace of Cups": "cups",
	"Knight of Cups": "cups",
	"Queen of Cups": "cups",
	"King of Cups": "cups",
	"Page of Cups": "cups",
	"Two of Pentacles": "pentacles",
	"Three of Pentacles": "pentacles",
	"Four of Pentacles": "pentacles",
	"Five of Pentacles": "pentacles",
	"Six of Pentacles": "pentacles",
	"Seven of Pentacles": "pentacles",
	"Eight of Pentacles": "pentacles",
	"Nine of Pentacles": "pentacles",
	"Ten of Pentacles": "pentacles",
	"Ace of Pentacles": "pentacles",
	"Knight of Pentacles": "pentacles",
	"Queen of Pentacles": "pentacles",
	"King of Pentacles": "pentacles",
	"Page of Pentacles": "pentacles",
	"Two of Wands": "wands",
	"Three of Wands": "wands",
	"Four of Wands": "wands",
	"Five of Wands": "wands",
	"Six of Wands": "wands",
	"Seven of Wands": "wands",
	"Eight of Wands": "wands",
	"Nine of Wands": "wands",
	"Ten of Wands": "wands",
	"Ace of Wands": "wands",
	"Knight of Wands": "wands",
	"Queen of Wands": "wands",
	"King of Wands": "wands",
	"Page of Wands": "wands",
	"Two of Swords": "swords",
	"Three of Swords": "swords",
	"Four of Swords": "swords",
	"Five of Swords": "swords",
	"Six of Swords": "swords",
	"Seven of Swords": "swords",
	"Eight of Swords": "swords",
	"Nine of Swords": "swords",
	"Ten of Swords": "swords",
	"Ace of Swords": "swords",
	"Knight of Swords": "swords",
	"Queen of Swords": "swords",
	"King of Swords": "swords",
	"Page of Swords": "swords"
}

with open("readings.json", "r") as fd:
	readings = json.loads(fd.read())

i = 0
while i < int(sys.argv[1]):
	[card1, card2, card3] = random.sample(list(cards), 3)
	[img1, img2, img3] = [cards[k] for k in [card1, card2, card3]]

	repeat = False
	for r in readings:
		if r['cards'] == [card1, card2, card3]:
			print("Repeat!!!")
			repeat = True

	if not repeat:
		client = OpenAI(api_key=apikey)
		completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "'Give me a one paragraph tarot reading if I pull the cards " + card1 + ", " + card2 + " and " + card3}])
		reading = {
			'message': completion.choices[0].message.content,
			'cards': [card1, card2, card3],
			'images': [img1, img2, img3]
		}
		print(reading)
		readings.append(reading)
		i += 1

with open("readings.json", "w") as fd:
	json.dump(readings, fd, ensure_ascii=False, indent=4)
