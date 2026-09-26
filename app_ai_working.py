import tkinter as tk
from openai import OpenAI
client = OpenAI()
root = tk.Tk()

root.title("SecondLife")
root.geometry("900x600")
root.configure(bg="#F4FFF8")

title = tk.Label(
    root,
    text="♻️ SecondLife",
    font=("Arial", 32, "bold"),
    bg="#F4FFF8",
    fg="#16803A"
)
title.pack(pady=(50, 10))

subtitle = tk.Label(
    root,
    text="Don't throw it away — give it a second life!",
    font=("Arial", 16),
    bg="#F4FFF8",
    fg="#444444"
)
subtitle.pack(pady=10)

description = tk.Label(
    root,
    text="Tell us what you have, and we'll show you creative ways to reuse it.",
    font=("Arial", 13),
    bg="#F4FFF8",
    fg="#555555"
)
description.pack(pady=10)
question = tk.Label(
    root,
    text="What item do you want to give a second life?",
    font=("Arial", 16, "bold"),
    bg="#F4FFF8",
    fg="#16803A"
)
question.pack(pady=(40, 10))

item_entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=35,
    justify="center",
    relief="solid",
    bd=1
)

item_entry.pack(pady=10)
item_entry.insert(0, "Example: milk carton, cardboard box, bottle")
def clear_example(event):
    if item_entry.get() == "Example: milk carton, cardboard box, bottle":
        item_entry.delete(0, tk.END)

item_entry.bind("<FocusIn>", clear_example)
def ask_ai(item):
    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=f"""You are the AI inside an app called SecondLife.
A user has an unwanted household item: {item}

Give ONE creative, practical way to reuse or upcycle it.
Keep the answer short and beginner-friendly.
Include:
♻️ Second Life Idea
🛠️ How to make it (3-5 simple steps)
🌱 Environmental benefit
"""
        )
        return response.output_text
    except Exception as e:
        return f"AI ERROR: {e}"

def find_second_life():
    item = item_entry.get().lower()
    if "cup" in item:
        idea = """☕ REUSED CUP MINI PLANTER

🧰 You need:
Used cup • Soil • Small plant or seeds • Small drainage holes

🛠 How to make it:
1. Wash and dry the cup.
2. Make a few small drainage holes in the bottom if the material allows it.
3. Add a little soil.
4. Add seeds or a small plant.
5. Fill around it with more soil.
6. Place it near sunlight.
7. Water lightly and watch it grow!

⭐ Difficulty: Easy     ⏱ About 5 minutes
♻️ Impact: Gives a disposable cup another useful purpose."""

    elif "bottle" in item:
          idea = """🌱 SELF-WATERING PLANTER

    🧰 You need:
    Plastic bottle • Cotton string • Scissors • Soil • Small plant

    🛠 How to make it:
    1. Cut the plastic bottle in half.
    2. Make a small hole in the bottle cap.
    3. Push a cotton string through the hole.
    4. Turn the top half upside down into the bottom half.
    5. Add soil and your small plant to the top.
    6. Add water to the bottom half.
    7. The string slowly carries water up to the soil!

    ⭐ Difficulty: Easy     ⏱ About 10 minutes
    ♻️ Impact: Gives one plastic bottle a second life."""
    elif "jar" in item:
        idea = """🫙 REUSED GLASS JAR ORGANIZER

     🧰 You need:
    Glass jar • Soap and water • Labels or decorations

🛠 How to make it:
1. Wash the jar thoroughly.
2. Remove the label.
3. Let the jar dry completely.
4. Decorate it if you want.
5. Add pencils, brushes, buttons, or small items.
6. Label the jar to keep things organized.

⭐ Difficulty: Easy     ⏱ About 5 minutes
♻ Impact: Reuses a glass jar instead of throwing it away."""

    elif "milk" in item or "carton" in item:
        idea = """" MILK CARTON BIRD FEEDER
    
🧰 You need:
Empty milk carton • Scissors • String • Birdseed • Small stick

🛠 How to make it:
1. Wash and completely dry the milk carton.
2. Cut an opening on one side of the carton.
3. Make a small hole below the opening.
4. Push a small stick through the hole for a perch.
5. Make a hole near the top and attach string.
6. Add birdseed inside the carton.
7. Hang it outside and watch for birds!

⭐ Difficulty: Easy     ⏱ About 15 minutes
♻️ Impact: Gives one milk carton a second life."""
    elif "can" in item or "tin can" in item:
        idea = """🥫 REUSED CAN PENCIL HOLDER

🧰 You need:
Empty can • Paper or fabric • Glue or tape • Markers

🛠 How to make it:
1. Wash and dry the can completely.
2. Make sure there are no sharp edges.
3. Wrap the outside with paper or fabric.
4. Decorate it with markers or stickers.
5. Place pencils, pens, or art supplies inside.

⭐ Difficulty: Easy     ⏱ About 10 minutes
♻ Impact: Turns an empty can into a useful desk organizer."""
    elif "cardboard" in item or "box" in item:
        idea = """📦 CARDBOARD DESK ORGANIZER

🧰 You need:
Cardboard box • Scissors • Glue or tape • Paper • Markers

🛠 How to make it:
1. Choose a clean cardboard box.
2. Cut the box to the height you want.
3. Cut extra cardboard pieces for dividers.
4. Place the dividers inside to create sections.
5. Secure them with glue or tape.
6. Cover or decorate the box with paper and markers.
7. Use it for pencils, school supplies, toys, or small items!

⭐ Difficulty: Easy     ⏱ About 15 minutes
♻️ Impact: Turns packaging waste into useful home storage."""
    elif "egg carton" in item or "egg box" in item:
        idea = """🥚 EGG CARTON MINI ORGANIZER

🧰 You need:
Empty egg carton • Markers or paint • Small items to organize

🛠 How to make it:
1. Clean and dry the egg carton.
2. Decorate the outside with markers or paint.
3. Use each compartment for a different small item.
4. Store buttons, beads, jewelry, LEGO pieces, screws, or craft supplies.
5. Label the sections if you want.
6. Close the carton when you're finished for easy storage.

⭐ Difficulty: Easy     ⏱ About 5 minutes
♻ Impact: Turns packaging waste into useful home storage."""
    elif "toilet paper" in item or "toilet roll" in item or "paper roll" in item or "cardboard tube" in item:
        idea = """📱 CARDBOARD ROLL PHONE STAND

🧰 You need:
Empty toilet roll • Scissors • Marker • Tape or decorations

🛠 How to make it:
1. Flatten the roll slightly so it stays steady.
2. Mark a slot on the top about the width of your phone.
3. Carefully cut the slot.
4. Place your phone in the slot to test the fit.
5. Decorate the roll with paper, markers, or stickers.
6. Use it as a simple desk phone stand.

⭐ Difficulty: Easy     ⏱ About 10 minutes
♻ Impact: Turns a cardboard tube into a useful phone accessory."""
    elif "can" in item:
        idea = """✏️ TIN CAN PENCIL HOLDER

🧰 You need:
Empty tin can • Colored paper • Glue or tape • Markers • Decorations

🛠 How to make it:
1. Wash and completely dry the empty can.
2. Make sure there are no sharp edges. Ask an adult for help if needed.
3. Measure and cut colored paper to fit around the can.
4. Wrap the paper around the can and secure it with glue or tape.
5. Decorate it with markers, stickers, or other safe materials.
6. Let everything dry.
7. Add pencils, pens, markers, or craft supplies!

⭐ Difficulty: Easy     ⏱ About 10 minutes
♻️ Impact: Turns an empty can into useful desk storage."""
    elif "paper" in item:
        idea = """🎁 RECYCLED PAPER GIFT BAG

🧰 You need:
Used paper • Scissors • Glue or tape • String • Markers

🛠 How to make it:
1. Choose a clean sheet of used paper.
2. Fold both sides toward the center.
3. Glue or tape the edges together.
4. Fold the bottom upward and secure it.
5. Open the bag carefully and shape the sides.
6. Make two small holes near the top.
7. Add string for handles and decorate your bag!

⭐ Difficulty: Easy     ⏱ About 10 minutes
♻️ Impact: Reuses paper and can replace a new gift bag."""
    else:
        idea = ask_ai(item)

    result_label.config(text=idea)
find_button = tk.Button(
    root,
    text="♻️ Find a Second Life",
    font=("Arial", 14, "bold"),
    bg="#16803A",
    fg="white",
    padx=25,
    pady=10,
    command=find_second_life,
)
find_button.pack(pady=20)
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#E8F5E9",
    fg="#16803A",
    wraplength=700,
    justify="center",
    padx=25,
    pady=20,
    relief="solid",
    bd=1
)
result_label.pack(pady=20)
root.bind("<Return>", lambda event: find_second_life())
root.mainloop()














