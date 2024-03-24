import tkinter as tk
import random

hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
]

# 国家列表
countries = ["CHINA", "USA", "UK"]

# 选择一个随机国家
def choose_country():
    return random.choice(countries).upper()

# 更新显示的单词
def update_displayed_word():
    displayed_word = " ".join([char if char in correct_guesses else "_" for char in selected_country])
    word_label.config(text=displayed_word)

# 处理一个猜测
def guess(letter):
    global chances, hangman_stage
    letter_buttons[letter].config(state="disabled")
    if letter in selected_country:
        correct_guesses.add(letter)
        update_displayed_word()
        if set(selected_country) == correct_guesses:
            status_label.config(text="You won!")
    else:
        chances -= 1
        hangman_stage += 1
        hangman_label.config(text=hangman_stages[hangman_stage])
        status_label.config(text=f"Chances left: {chances}")
        if chances == 0:
            status_label.config(text=f"Game Over! The correct word was: {selected_country}")

# 重置游戏
def reset_game():
    global selected_country, correct_guesses, chances, hangman_stage
    selected_country = choose_country()
    correct_guesses = set()
    chances = len(selected_country) + 2
    hangman_stage = 0
    hangman_label.config(text=hangman_stages[hangman_stage])
    update_displayed_word()
    status_label.config(text=f"Chances left: {chances}")
    for letter, btn in letter_buttons.items():
        btn.config(state="normal")

# 创建主窗口
root = tk.Tk()
root.title("Country Hangman Game")

# 初始化游戏变量
selected_country = choose_country()
correct_guesses = set()
chances = len(selected_country) + 2
hangman_stage = 0  # Hangman figure stage

# 用户界面元素
hangman_label = tk.Label(root, text=hangman_stages[hangman_stage], font=("Courier", 14), justify=tk.LEFT)
hangman_label.pack()

word_label = tk.Label(root, font=("Helvetica", 24))
word_label.pack()

status_label = tk.Label(root, text=f"Chances left: {chances}", font=("Helvetica", 14))
status_label.pack()

# 字母按钮
letter_buttons = {}
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    command = lambda ltr=letter: guess(ltr)
    button = tk.Button(root, text=letter, command=command)
    button.pack(side="left")
    letter_buttons[letter] = button

# 重置按钮
reset_button = tk.Button(root, text="New Game", command=reset_game)
reset_button.pack(side="bottom")

# 开始游戏
reset_game()  # 新游戏
root.mainloop()
