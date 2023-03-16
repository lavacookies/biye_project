import pyttsx3

engine = pyttsx3.init()

text = "I like to eat, eat, eat apples and bananas.?"

engine.say(text)

engine.runAndWait()
