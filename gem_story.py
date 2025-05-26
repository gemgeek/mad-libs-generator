# Mad Libs - GEM Geek Headquarters Visit 💻👩🏽‍💻✨

# Get user inputs
your_name = input("What's your name? ")
tech_gadget = input("Name a tech gadget: ")
adjective = input("Describe how you felt: ")
verb = input("What were you doing there? (e.g., coding, designing): ")
snack = input("Name a snack you love: ")

# Conditional twist
if verb.lower() == "coding":
    highlight = "You cracked a major bug and everyone cheered! 🥳"
else:
    highlight = f"Everyone was amazed by your {verb} skills. 🌟"

# Build the story
story = f"""
Today, {your_name} visited the legendary GEM Geek Headquarters! 🏢✨
Armed with a {tech_gadget}, you walked into the sleek, pastel-colored lobby. 💼
You felt so {adjective} as you started {verb} in the innovation lab. 🚀
During the break, you munched on your favorite snack — {snack}. 🍿
{highlight}
It was a day to remember, and the GEM crew couldn’t stop talking about you! 💖
"""

# Show the story
print(story)
