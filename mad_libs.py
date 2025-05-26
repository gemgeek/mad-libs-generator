# Mad Libs Generator - Cute Zoo Adventure 🐵🦁💕

# Step 1: Get user inputs
adjective1 = input("Enter a cute adjective: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter your favorite animal: ")
verb = input("Enter a verb (e.g. dancing, singing): ")
emotion = input("Enter an emotion: ")

# Step 2: Add a conditional twist based on the emotion
if emotion.lower() == "happy":
    ending = "It was the best day ever! 🥳"
else:
    ending = f"But somehow, I still felt {emotion} inside. 🤔"

# Step 3: Build the story
story = f"""
On a {adjective1} afternoon, I visited the magical zoo. 🌈
There, I saw a {adjective2} {animal} {verb} near the fountain! 🐾
Everyone around started laughing and clapping. 🎉
{ending}
"""

# Step 4: Print the story
print(story)
