import random

insults = [
    "Did you leave your brain in your other pants?",
    "I've seen rocks with better guessing skills.",
    "Are you guessing, or just throwing darts in the dark?",
    "Your guessing strategy is as solid as a chocolate teapot.",
    "I'd explain it to you, but I don't have any crayons.",
    "Did you consult a Magic 8-Ball for that one?",
    "You're not the sharpest tool in the shed, are you?",
    "I think my goldfish guesses better than you.",
    "Are you playing this game or just staring at the screen?",
    "Your logic is truly a mystery to the universe.",
    "A blindfolded monkey throwing darts would have done better.",
    "Even a broken clock is right twice a day, but not you.",
    "Did you just mash the keyboard and hope for the best?",
    "I've seen better luck from a potato.",
    "Are you actively trying to be wrong?",
    "That guess was so bad it offended my algorithms.",
    "You're making the random number generator look good.",
    "Did you pick that by throwing a shoe at the screen?",
    "I didn't know 'completely wrong' was an option, but here we are.",
    "Your luck is currently in the negatives.",
    "Did it take you all day to come up with that?",
    "Take your time, the universe is expanding anyway.",
    "I've seen glaciers move faster than your progress.",
    "Are you guessing or just meditating on the numbers?",
    "That was a bold guess. Boldly incorrect, but bold.",
    "I'd say 'good try', but we both know that's a lie.",
    "You're really committed to being wrong, I'll give you that.",
    "Is there a tutorial I can point you to?",
    "I'm starting to think you don't like winning.",
    "Effort: 10%. Accuracy: -50%.",
    "My CPU is overheating just processing how wrong you are.",
    "I'm a computer, and even I'm confused by your logic.",
    "Did you bypass the 'thinking' part of your brain?",
    "Error 404: Guessing skills not found.",
    "I'd reboot your brain, but it wouldn't help.",
    "Your guess just caused a stack overflow in my disappointment meter.",
    "Are you running on Windows 95? Because that guess is outdated.",
    "I've seen better code from a first-year student.",
    "Let me guess, you skipped the tutorial?",
    "My pixels are judging you right now.",
    "Wow, what a fascinating choice. Truly.",
    "I love how confident you were in that completely wrong number.",
    "That number is my favorite too! Just kidding, it's terrible.",
    "Did your horoscope tell you to pick that?",
    "I'm saving that guess in a museum of bad decisions.",
    "You have a real talent for missing the point.",
    "If being wrong was an Olympic sport, you'd have gold.",
    "I'd tell you to go outside, but you'd probably guess the weather wrong too.",
    "That guess was so far off it's in a different time zone.",
    "Keep guessing! It's almost cute how lost you are."
]

def easy():
    num = random.randint(1,10)
    total_attempts =  3

    for i in range(1, total_attempts + 1, 1):
        n = int(input("Guess: "))

        if i == 3:
            print("Attempts over!")
            print("You're such a great Looser 🙃")
            break
        
        if n > num:
            print("="*20)
            print("Too HIGH")
            print("="*20)
        elif n < num:
            print("="*20)
            print("Too LOW")
            print("="*20)

        if n == num:
            print("="*50)
            print("You Won 🏆")
            print("="*50)
            break
        
        else:
            print("Try again!")
            total_attempts -= 1
            print(f"{total_attempts} attempts left!")
            print("="*50)
            print(insults[random.randint(1,50)])
            print("="*50)
            continue
def medium():
    num = random.randint(1,50)
    total_attempts =  5

    for i in range(1, total_attempts + 1, 1):
        n = int(input("Guess: "))

        if i == 5:
            print("Attempts over!")
            print("You're such a great Looser 🙃")
            break
        
        if n > num:
            print("="*20)
            print("Too HIGH")
            print("="*20)
        elif n < num:
            print("="*20)
            print("Too LOW")
            print("="*20)

        if n == num:
            print("="*50)
            print("You Won 🏆")
            print("="*50)
            break
        
        else:
            print("Try again!")
            total_attempts -= 1
            print(f"{total_attempts} attempts left!")
            print("="*50)
            print(insults[random.randint(1,50)])
            print("="*50)
            continue

def hard():
    num = random.randint(1,100)
    total_attempts =  10

    for i in range(1, total_attempts + 1, 1):
        n = int(input("Guess: "))

        if i == 10:
            print("Attempts over!")
            print("You're such a great Looser 🙃")
            break
        
        if n > num:
            print("="*20)
            print("Too HIGH")
            print("="*20)
        elif n < num:
            print("="*20)
            print("Too LOW")
            print("="*20)

        if n == num:
            print("="*50)
            print("You Won 🏆")
            print("="*50)
            break
        
        else:
            print("Try again!")
            total_attempts -= 1
            print(f"{total_attempts} attempts left!")
            print("="*50)
            print(insults[random.randint(1,50)])
            print("="*50)
            continue

def impossible():
    num = random.randint(1,1000)
    total_attempts =  20

    for i in range(1, total_attempts + 1, 1):
        n = int(input("Guess: "))

        if i == 20:
            print("Attempts over!")
            print("You're such a great Looser 🙃")
            break
        
        if n > num:
            print("="*20)
            print("Too HIGH")
            print("="*20)
        elif n < num:
            print("="*20)
            print("Too LOW")
            print("="*20)

        if n == num:
            print("="*50)
            print("You Won 🏆")
            print("="*50)
            break
        
        else:
            print("Try again!")
            total_attempts -= 1
            print(f"{total_attempts} attempts left!")
            print("="*50)
            print(insults[random.randint(1,50)])
            print("="*50)
            continue
        

print("=== Choose Your difficulty ===")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")
print("4. Impossible (1-1000)")

choice = int(input("Enter your choice(1-4): "))

match(choice):
    case 1:
        print(f"Total Attempts: 3")
        easy()
    case 2:
        print(f"Total Attempts: 5")
        medium()
    case 3:
        print(f"Total Attempts: 10")
        hard()
    case 4:
        print(f"Total Attempts: 20")
        impossible()
    case _:
        print("Make a right choice you Bitch")