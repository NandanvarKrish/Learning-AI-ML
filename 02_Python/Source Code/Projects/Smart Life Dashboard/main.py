# IMPORTS
import random
import datetime
import json
import os

# APP INFO
APP_NAME = 'Smart Life Dashboard'
VERSION = '1.0'
MIN_SCORE = 5 # below this = roast
STREAK_GOAL = 7 # consecutive days above MIN_SCORE
HISTORY_FILE = 'history.json'

# Session vars (Filled later)

user_name = ''
mood_score = 0
habit_score = 0.0
is_weekend = False

#REQUIRED DATA

ROAST_MESSAGES = [
'That score is embarrassing. What happened?',
'My grandma scores higher and she has dial-up.',
'Rock bottom has a basement. You found it.',
'One habit. Out of four. Yikes.',
]

PRAISE_MESSAGES = [
'Absolutely locked in. This is the way.',
'Top 1% day. Document this feeling.',
]

HABITS = ['Exercise','Read 30 min','No junk food','Meditate']

# FUNCTIONS

def show_banner():
    print("=" * 50)
    print(f"{APP_NAME} v{VERSION}")
    print("=" * 50)

def collect_morning_info(greetings):
    print(f"\n{greetings}")
    name = input("Your Name: ").strip() or 'Human'
    mood = input("Enter one word for your mood: ").strip()
    score = input("Mood Score (1-10) : ").strip()
    sleep = input("Hours of sleep Last Night: ").strip()
    print(f"\nGot it, {name}! | Mood: {mood} | score:n {score} | Sleep: {sleep}Hrs")
    return name, mood, score, sleep

def mood_tier(score):
    if score >= 9:
        return 'Excellent'
    elif score >= 7:
        return 'Good'
    elif score >= 5:
        return 'Okay'
    elif score >= 3:
        return 'Rough'
    else:
        return 'Disaster'
    
def get_reaction(daily_score):
    if daily_score >= 8:
        return 'CRUSHING IT!, Keep it UP.'
    elif daily_score >= 6:
        return 'DECENT!, Cold push Harder.'
    elif daily_score >= 4:
        return 'MEDIOCRE!, You know what to fix.'
    else:
        return 'YIKES!, Tomorrow is another chance'


def run_habit_checkin():
    results = {}
    print("\n--- Habit Checkin ---")
    
    for habit in HABITS:
        while True:
            ans = input(f"{habit}? (y/n): ").lower().strip()

            if ans in ('y', 'n'):
                results[habit] = (ans == 'y')
                break
            else:
                print(' y or n only.')
    
    done = sum(1 for v in results.values() if v)
    return results, done / len(HABITS)

def get_message(score):
    if score >= 8:
        return random.choice(PRAISE_MESSAGES)
    elif score < 5:
        return random.choice(ROAST_MESSAGES)
    
    return 'Solid. Keep building.'

def build_day_entry(name, mood_score, mood_word, sleep, habit_results, daily_score, streak):
    return {
        'date' : str(datetime.date.today()),
        'name' : name,
        'mood_score' : mood_score,
        'sleep' : sleep,
        'habits' : habit_results, # dict: habit -> bool
        'daily_score' : round(daily_score, 2),
        'streak' : streak,
    }

def calculate_daily_score(mood_score, habit_score, sleep_hours):
    sleep_norm = min(sleep_hours/8.0, 1.0)
    score = (mood_score/10) * 0.5 + habit_score * 0.4 + sleep_norm*0.1
    
    return round(score * 10, 2) # scale to 0-10

def count_streak(history, threshold = 7.0):
    streak = 0
    for entry in reversed(history):
        if entry['daily_score'] >= threshold:
            streak += 1
        else:
            break

    return streak

def log_event(*messages):
    ts = datetime.datetime.now().strftime('%H:%M')
    for msg in messages:
        print(f"[{ts}] {msg}")

def calculate_score_v2(mood, habits, sleep, **weights):
    wm = weights.get('mood', 0.5)
    wh = weights.get('habits', 0.4)
    ws = weights.get('sleep', 0.1)

    return round((mood/10*wm + habits*wh + min(sleep/8,1)*ws)*10, 2)

def get_greeting():
    h = datetime.datetime.now().hour

    if h < 12:
        return '🌞 Good Morning'
    elif h < 17:
        return '🕑 Good Afternoon'
    else:
        return '🌃 Good Evening'

def is_weekend():
    return datetime.date.today().weekday()

def safe_load_history(path):
    if not os.path.exists(path):
        return []
    
    if os.path.getsize(path) == 0:
        return []
    
    with open(path) as f:
        return json.load(f)

def save_entry(entry):
    history = safe_load_history(HISTORY_FILE)
    history.append(entry)

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)
    
    print(f"Entry Saved. Total sessions : {len(history)}")

def display_all_stats():
    history = safe_load_history(HISTORY_FILE)

    if not history:
        print("No History yet!")
        return 
    scores = [e['daily_score'] for e  in history]

    print(f"Sessions: {len(history)} | Avg: {sum(scores)/len(scores):.1f}")
    print(f"Best: {max(scores)} | Worst: {min(scores)} | Streak: {count_streak(history)}d")

def validate_int_input(score):
    if not score.isdigit():
        return "Error"
    elif int(score) < 1 or int(score) > 10:
        return "Range Error"

def validate_float_input(score):
    if not score.isdigit():
        return "Error"
    elif int(score) < 1 or int(score) > 10:
        return "Range Error"

def validate_int_input(score_str, min_val, max_val):
    while True:
        if not score_str.isdigit():
            print("⚠️ Error! Please enter a valid whole number.")
        elif int(score_str) < min_val or int(score_str) > max_val:
            print(f"⚠️ Range Error! Enter {min_val}-{max_val}.")
        else:
            return int(score_str)
        
        score_str = input(f"Retry ({min_val}-{max_val}): ").strip()

def validate_float_input(score_str, min_val, max_val):
    while True:
        clean = score_str.replace('.', '', 1)

        if not clean.isdigit() or score_str.count('.') > 1:
            print("⚠️ Error! Please enter a valid number (e.g., 7.5).")
        elif float(score_str) < min_val or float(score_str) > max_val:
            print(f"⚠️ Range Error! Enter {min_val}-{max_val}.")
        else:
            return float(score_str)
        
        score_str = input(f"Retry ({min_val}-{max_val}): ").strip()

#Lambdas

top_days = lambda h: sorted(h, key=lambda e: e['daily_score'], reverse=True)[:5]
predict = lambda h: round(sum(e['daily_score'] for e in h[-3:])/3, 1) if h else 0

#Main Function (Combining all the functions)

def main():
    show_banner()
    greeting = get_greeting()
    name, mood_word, mood_str, sleep_str, = collect_morning_info(greeting)
    mood_score = validate_int_input(mood_str, 1, 10)
    sleep_hours = validate_float_input(sleep_str, 0, 24)
    habit_results, habit_score = run_habit_checkin()
    history = safe_load_history(HISTORY_FILE)
    streak = count_streak(history)
    daily_score = calculate_daily_score(mood_score, habit_score, sleep_hours)
    entry = build_day_entry(name, mood_score, mood_word, sleep_hours, habit_results, daily_score, streak)
    save_entry(entry)
    reaction = get_reaction(daily_score)
    tomorrow = predict(history + [entry])
    print(f"Score: {daily_score}/10 | Streak: {streak} days")
    print(f"{reaction}")
    print(f"Tomorrow Prediction: {tomorrow}/10")
    display_all_stats()

if __name__ == '__main__':
    main()
