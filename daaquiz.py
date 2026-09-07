import tkinter as tk
from tkinter import messagebox
import random


# ============================================================
# PREMIUM DAA QUIZ
# ============================================================

# ------------------------------------------------------------
# COLORS - PARKAI INSPIRED DARK UI
# ------------------------------------------------------------

C = {
    "bg": "#030817",
    "bg2": "#06101f",

    "card": "#0b1426",
    "card2": "#101a2e",
    "option": "#111a2c",
    "option_hover": "#17253b",

    "border": "#1b2a42",
    "border2": "#263957",

    "text": "#f5f7fb",
    "muted": "#8493aa",

    "cyan": "#16d9c5",
    "cyan_dark": "#0e9f94",

    "blue": "#1785c5",
    "blue_dark": "#12649b",

    "green": "#18c58b",
    "green_dark": "#087a58",

    "red": "#ef5350",
    "yellow": "#f5b942",

    "white": "#ffffff"
}


# ============================================================
# QUESTION BANK
#
# 7 TOPICS
# 3 DIFFICULTIES
# 2 QUESTIONS EACH
#
# TOTAL = 42 QUESTIONS
# ============================================================

questionBank = [

    # ========================================================
    # COMPLEXITY - EASY
    # ========================================================

    {
        "question": "What is the time complexity of accessing an array element using its index?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
        "answer": "O(1)",
        "topic": "Complexity",
        "difficulty": "Easy",
        "explanation": "Array elements can be accessed directly using their index, so the operation takes constant time."
    },

    {
        "question": "What is the time complexity of a loop that runs exactly n times?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
        "answer": "O(n)",
        "topic": "Complexity",
        "difficulty": "Easy",
        "explanation": "The loop performs n iterations, giving a linear time complexity of O(n)."
    },

    # COMPLEXITY - MEDIUM

    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"],
        "answer": "O(log n)",
        "topic": "Complexity",
        "difficulty": "Medium",
        "explanation": "Binary search divides the search space into half during every step."
    },

    {
        "question": "Two nested loops each execute n times. What is their complexity?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(2n)"],
        "answer": "O(n²)",
        "topic": "Complexity",
        "difficulty": "Medium",
        "explanation": "The inner loop executes n times for each of the n iterations of the outer loop."
    },

    # COMPLEXITY - HARD

    {
        "question": "What is the worst-case time complexity of Quick Sort?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"],
        "answer": "O(n²)",
        "topic": "Complexity",
        "difficulty": "Hard",
        "explanation": "Quick Sort can become O(n²) when the pivot repeatedly produces highly unbalanced partitions."
    },

    {
        "question": "What is the time complexity of Merge Sort in the worst case?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"],
        "answer": "O(n log n)",
        "topic": "Complexity",
        "difficulty": "Hard",
        "explanation": "Merge Sort divides the array into logarithmic levels and performs O(n) merging at each level."
    },


    # ========================================================
    # SORTING - EASY
    # ========================================================

    {
        "question": "Which sorting algorithm repeatedly compares adjacent elements?",
        "options": ["Bubble Sort", "Selection Sort", "Merge Sort", "Heap Sort"],
        "answer": "Bubble Sort",
        "topic": "Sorting",
        "difficulty": "Easy",
        "explanation": "Bubble Sort compares adjacent elements and swaps them when they are in the wrong order."
    },

    {
        "question": "Which sorting algorithm repeatedly selects the minimum element?",
        "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Merge Sort"],
        "answer": "Selection Sort",
        "topic": "Sorting",
        "difficulty": "Easy",
        "explanation": "Selection Sort finds the minimum element from the unsorted portion and places it in the correct position."
    },

    # SORTING - MEDIUM

    {
        "question": "Which sorting algorithm follows the divide-and-conquer approach?",
        "options": ["Bubble Sort", "Merge Sort", "Selection Sort", "Insertion Sort"],
        "answer": "Merge Sort",
        "topic": "Sorting",
        "difficulty": "Medium",
        "explanation": "Merge Sort divides the array into smaller parts, sorts them recursively, and merges them."
    },

    {
        "question": "Which sorting algorithm uses a pivot?",
        "options": ["Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort"],
        "answer": "Quick Sort",
        "topic": "Sorting",
        "difficulty": "Medium",
        "explanation": "Quick Sort selects a pivot and partitions the array around that pivot."
    },

    # SORTING - HARD

    {
        "question": "Which sorting algorithm guarantees O(n log n) worst-case time and uses a heap?",
        "options": ["Quick Sort", "Heap Sort", "Bubble Sort", "Insertion Sort"],
        "answer": "Heap Sort",
        "topic": "Sorting",
        "difficulty": "Hard",
        "explanation": "Heap Sort uses a binary heap and guarantees O(n log n) worst-case time."
    },

    {
        "question": "Which sorting algorithm can be implemented as a stable sorting algorithm?",
        "options": ["Heap Sort", "Quick Sort", "Merge Sort", "Selection Sort"],
        "answer": "Merge Sort",
        "topic": "Sorting",
        "difficulty": "Hard",
        "explanation": "Merge Sort can preserve the relative order of equal elements and therefore can be stable."
    },


    # ========================================================
    # SEARCHING - EASY
    # ========================================================

    {
        "question": "Which searching technique checks elements one by one?",
        "options": ["Binary Search", "Linear Search", "Jump Search", "Hash Search"],
        "answer": "Linear Search",
        "topic": "Searching",
        "difficulty": "Easy",
        "explanation": "Linear Search examines elements sequentially until the target is found."
    },

    {
        "question": "Binary Search requires the data to be:",
        "options": ["Random", "Sorted", "Duplicated", "Unstructured"],
        "answer": "Sorted",
        "topic": "Searching",
        "difficulty": "Easy",
        "explanation": "Binary Search depends on the data being sorted so that half of the search space can be eliminated."
    },

    # SEARCHING - MEDIUM

    {
        "question": "What is the best-case time complexity of Linear Search?",
        "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
        "answer": "O(1)",
        "topic": "Searching",
        "difficulty": "Medium",
        "explanation": "If the target is the first element, only one comparison is required."
    },

    {
        "question": "What is the worst-case time complexity of Binary Search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "answer": "O(log n)",
        "topic": "Searching",
        "difficulty": "Medium",
        "explanation": "Binary Search cuts the remaining search space in half at every step."
    },

    # SEARCHING - HARD

    {
        "question": "What is the average search time in a well-designed hash table?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
        "answer": "O(1)",
        "topic": "Searching",
        "difficulty": "Hard",
        "explanation": "With a good hash function and controlled collisions, average lookup is O(1)."
    },

    {
        "question": "Which searching algorithm is useful when the size of a sorted array is unknown?",
        "options": ["Linear Search", "Exponential Search", "Selection Search", "Bubble Search"],
        "answer": "Exponential Search",
        "topic": "Searching",
        "difficulty": "Hard",
        "explanation": "Exponential Search finds a suitable range by increasing the index exponentially and then uses Binary Search."
    },


    # ========================================================
    # GREEDY - EASY
    # ========================================================

    {
        "question": "What is the basic idea behind a greedy algorithm?",
        "options": [
            "Choose the locally best option",
            "Try every possible solution",
            "Always use recursion",
            "Store every subproblem"
        ],
        "answer": "Choose the locally best option",
        "topic": "Greedy",
        "difficulty": "Easy",
        "explanation": "Greedy algorithms make the best available local choice at each step."
    },

    {
        "question": "Which problem is commonly solved using a greedy strategy?",
        "options": [
            "Activity Selection",
            "Matrix Chain Multiplication",
            "N-Queens",
            "LCS"
        ],
        "answer": "Activity Selection",
        "topic": "Greedy",
        "difficulty": "Easy",
        "explanation": "Activity Selection can be optimally solved by repeatedly selecting the activity with the earliest finishing time."
    },

    # GREEDY - MEDIUM

    {
        "question": "What criterion is used in the Activity Selection problem?",
        "options": [
            "Earliest starting time",
            "Earliest finishing time",
            "Largest duration",
            "Smallest duration"
        ],
        "answer": "Earliest finishing time",
        "topic": "Greedy",
        "difficulty": "Medium",
        "explanation": "Selecting the activity that finishes earliest leaves the maximum remaining time for other activities."
    },

    {
        "question": "Which algorithm constructs a Minimum Spanning Tree using a greedy approach?",
        "options": ["Kruskal's Algorithm", "Floyd-Warshall", "Bellman-Ford", "Binary Search"],
        "answer": "Kruskal's Algorithm",
        "topic": "Greedy",
        "difficulty": "Medium",
        "explanation": "Kruskal's Algorithm repeatedly selects the smallest edge that does not create a cycle."
    },

    # GREEDY - HARD

    {
        "question": "Which algorithm is used to construct an optimal prefix code?",
        "options": ["Dijkstra", "Huffman Coding", "Kruskal", "Floyd-Warshall"],
        "answer": "Huffman Coding",
        "topic": "Greedy",
        "difficulty": "Hard",
        "explanation": "Huffman Coding repeatedly combines the two least frequent symbols to build an optimal prefix tree."
    },

    {
        "question": "Which shortest-path algorithm uses a greedy strategy?",
        "options": ["Dijkstra's Algorithm", "Floyd-Warshall", "Kruskal's Algorithm", "Warshall's Algorithm"],
        "answer": "Dijkstra's Algorithm",
        "topic": "Greedy",
        "difficulty": "Hard",
        "explanation": "Dijkstra repeatedly selects the unvisited vertex with the smallest tentative distance."
    },


    # ========================================================
    # DYNAMIC PROGRAMMING - EASY
    # ========================================================

    {
        "question": "Dynamic Programming is especially useful when a problem has:",
        "options": [
            "Overlapping subproblems",
            "Only one solution",
            "No subproblems",
            "Only sorted data"
        ],
        "answer": "Overlapping subproblems",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "explanation": "DP stores solutions to overlapping subproblems so they can be reused."
    },

    {
        "question": "Which technique stores previously computed results?",
        "options": ["Memoization", "Partitioning", "Sorting", "Traversal"],
        "answer": "Memoization",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "explanation": "Memoization stores the result of a subproblem so it does not need to be calculated again."
    },

    # DYNAMIC PROGRAMMING - MEDIUM

    {
        "question": "Which of the following is a classic Dynamic Programming problem?",
        "options": [
            "0/1 Knapsack",
            "Binary Search",
            "Activity Selection",
            "Linear Search"
        ],
        "answer": "0/1 Knapsack",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "explanation": "The 0/1 Knapsack problem has overlapping subproblems and optimal substructure."
    },

    {
        "question": "Which problem finds the longest subsequence common to two sequences?",
        "options": [
            "LCS",
            "MST",
            "BFS",
            "DFS"
        ],
        "answer": "LCS",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "explanation": "LCS stands for Longest Common Subsequence and is commonly solved using DP."
    },

    # DYNAMIC PROGRAMMING - HARD

    {
        "question": "What is the standard time complexity of the Dynamic Programming solution for LCS?",
        "options": ["O(m+n)", "O(mn)", "O(m²n²)", "O(log mn)"],
        "answer": "O(mn)",
        "topic": "Dynamic Programming",
        "difficulty": "Hard",
        "explanation": "The standard LCS DP table contains m × n states."
    },

    {
        "question": "Which technique is used to find the optimal parenthesization in Matrix Chain Multiplication?",
        "options": [
            "Dynamic Programming",
            "Linear Search",
            "BFS",
            "Greedy only"
        ],
        "answer": "Dynamic Programming",
        "topic": "Dynamic Programming",
        "difficulty": "Hard",
        "explanation": "Matrix Chain Multiplication uses DP to determine the minimum multiplication cost."
    },


    # ========================================================
    # GRAPH - EASY
    # ========================================================

    {
        "question": "Which data structure is commonly used by BFS?",
        "options": ["Stack", "Queue", "Heap", "Tree"],
        "answer": "Queue",
        "topic": "Graph",
        "difficulty": "Easy",
        "explanation": "BFS explores vertices level by level and therefore uses a queue."
    },

    {
        "question": "Which graph traversal explores as far as possible before backtracking?",
        "options": ["BFS", "DFS", "Kruskal", "Prim"],
        "answer": "DFS",
        "topic": "Graph",
        "difficulty": "Easy",
        "explanation": "Depth First Search explores deeply along a path before backtracking."
    },

    # GRAPH - MEDIUM

    {
        "question": "Which algorithm constructs an MST by growing a tree from a starting vertex?",
        "options": ["Prim's Algorithm", "Floyd-Warshall", "BFS", "DFS"],
        "answer": "Prim's Algorithm",
        "topic": "Graph",
        "difficulty": "Medium",
        "explanation": "Prim's Algorithm starts from a vertex and repeatedly adds the minimum-weight connecting edge."
    },

    {
        "question": "Which traversal can find the shortest path in an unweighted graph?",
        "options": ["DFS", "BFS", "Kruskal", "Prim"],
        "answer": "BFS",
        "topic": "Graph",
        "difficulty": "Medium",
        "explanation": "BFS visits vertices in increasing order of their distance from the source."
    },

    # GRAPH - HARD

    {
        "question": "Which algorithm finds shortest paths between all pairs of vertices?",
        "options": [
            "Floyd-Warshall",
            "Prim",
            "Kruskal",
            "Binary Search"
        ],
        "answer": "Floyd-Warshall",
        "topic": "Graph",
        "difficulty": "Hard",
        "explanation": "Floyd-Warshall computes shortest paths between every pair of vertices."
    },

    {
        "question": "Which algorithm supports negative edge weights and can detect negative cycles?",
        "options": [
            "Bellman-Ford",
            "Prim",
            "Kruskal",
            "Binary Search"
        ],
        "answer": "Bellman-Ford",
        "topic": "Graph",
        "difficulty": "Hard",
        "explanation": "Bellman-Ford can work with negative edge weights and can detect negative-weight cycles."
    },


    # ========================================================
    # BACKTRACKING - EASY
    # ========================================================

    {
        "question": "Backtracking generally builds a solution:",
        "options": [
            "Step by step",
            "Only after sorting",
            "Without checking constraints",
            "Using only greedy choices"
        ],
        "answer": "Step by step",
        "topic": "Backtracking",
        "difficulty": "Easy",
        "explanation": "Backtracking constructs a solution incrementally and abandons invalid partial solutions."
    },

    {
        "question": "Which problem is a classic Backtracking problem?",
        "options": [
            "N-Queens",
            "Binary Search",
            "Merge Sort",
            "Linear Search"
        ],
        "answer": "N-Queens",
        "topic": "Backtracking",
        "difficulty": "Easy",
        "explanation": "N-Queens places queens one by one while checking whether each placement is valid."
    },

    # BACKTRACKING - MEDIUM

    {
        "question": "What happens when a partial solution violates a constraint?",
        "options": [
            "The algorithm backtracks",
            "The solution is accepted",
            "The array is sorted",
            "The program always stops"
        ],
        "answer": "The algorithm backtracks",
        "topic": "Backtracking",
        "difficulty": "Medium",
        "explanation": "The algorithm removes the previous choice and tries another possibility."
    },

    {
        "question": "Which problem searches for subsets whose sum equals a target value?",
        "options": [
            "Sum of Subsets",
            "Merge Sort",
            "Dijkstra",
            "Binary Search"
        ],
        "answer": "Sum of Subsets",
        "topic": "Backtracking",
        "difficulty": "Medium",
        "explanation": "The Sum of Subsets problem can be solved by exploring include/exclude choices using backtracking."
    },

    # BACKTRACKING - HARD

    {
        "question": "Which problem assigns at most m colors so that adjacent vertices have different colors?",
        "options": [
            "M-Coloring",
            "Knapsack",
            "Activity Selection",
            "Binary Search"
        ],
        "answer": "M-Coloring",
        "topic": "Backtracking",
        "difficulty": "Hard",
        "explanation": "M-Coloring assigns colors to graph vertices while satisfying the adjacency constraint."
    },

    {
        "question": "What is the main purpose of pruning in Backtracking?",
        "options": [
            "Avoid impossible branches",
            "Increase branches",
            "Remove recursion",
            "Sort all choices"
        ],
        "answer": "Avoid impossible branches",
        "topic": "Backtracking",
        "difficulty": "Hard",
        "explanation": "Pruning eliminates branches that cannot lead to a valid solution."
    }
]


# ============================================================
# APPLICATION
# ============================================================

class DAAQuiz:

    def __init__(self, root):

        self.root = root

        self.root.title("DAA Challenge • Algorithm Master")
        self.root.geometry("1150x820")
        self.root.minsize(950, 700)

        self.root.configure(bg=C["bg"])

        # ----------------------------------------------------
        # QUIZ STATE
        # ----------------------------------------------------

        self.studentName = ""

        self.selectedTopic = "All"
        self.selectedDifficulty = "All"

        self.quizQuestions = []

        self.currentQuestion = 0

        self.score = 0
        self.correctAnswers = 0
        self.wrongAnswers = 0

        self.answersReview = []

        self.selectedAnswer = tk.StringVar()

        self.timeLeft = 30
        self.timerID = None

        self.confettiID = None

        self.topicOpen = False
        self.difficultyOpen = False

        self.show_index()


    # ========================================================
    # CLEAR SCREEN
    # ========================================================

    def clear_screen(self):

        if self.timerID is not None:

            try:
                self.root.after_cancel(self.timerID)
            except:
                pass

            self.timerID = None


        if self.confettiID is not None:

            try:
                self.root.after_cancel(self.confettiID)
            except:
                pass

            self.confettiID = None


        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # PREMIUM BACKGROUND
    # ========================================================

    def premium_background(self):

        canvas = tk.Canvas(
            self.root,
            bg=C["bg"],
            highlightthickness=0
        )

        canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # ----------------------------------------------------
        # LEFT BLUE GLOW
        # ----------------------------------------------------

        canvas.create_oval(
            -400,
            -150,
            450,
            700,
            fill="#06263b",
            outline=""
        )

        canvas.create_oval(
            -300,
            0,
            300,
            600,
            fill="#073047",
            outline=""
        )

        canvas.create_oval(
            -150,
            100,
            200,
            500,
            fill="#08394e",
            outline=""
        )


        # ----------------------------------------------------
        # RIGHT GREEN GLOW
        # ----------------------------------------------------

        canvas.create_oval(
            750,
            350,
            1400,
            1000,
            fill="#063426",
            outline=""
        )

        canvas.create_oval(
            850,
            450,
            1250,
            850,
            fill="#07412f",
            outline=""
        )


        # ----------------------------------------------------
        # TOP DARK BLUE GLOW
        # ----------------------------------------------------

        canvas.create_oval(
            250,
            -350,
            1000,
            300,
            fill="#06192e",
            outline=""
        )

        return canvas


    # ========================================================
    # BUTTON
    # ========================================================

    def make_button(
        self,
        parent,
        text,
        command,
        bg=None,
        width=20,
        height=2
    ):

        if bg is None:
            bg = C["card2"]

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=C["text"],
            activebackground=C["cyan_dark"],
            activeforeground=C["white"],
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            width=width,
            height=height
        )


    # ========================================================
    # INDEX PAGE
    # ========================================================

    def show_index(self):

        self.clear_screen()

        self.topicOpen = False
        self.difficultyOpen = False

        self.premium_background()


        # ----------------------------------------------------
        # MAIN CONTAINER
        # ----------------------------------------------------

        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.72,
            relheight=0.90
        )


        # ----------------------------------------------------
        # TOP BRAND
        # ----------------------------------------------------

        top = tk.Frame(
            container,
            bg=C["bg"]
        )

        top.pack(
            fill="x",
            pady=(10, 5)
        )


        tk.Label(
            top,
            text="DAA",
            bg=C["bg"],
            fg=C["cyan"],
            font=("Segoe UI", 17, "bold")
        ).pack(side="left")


        tk.Label(
            top,
            text="ALGORITHM CHALLENGE",
            bg=C["bg"],
            fg=C["muted"],
            font=("Segoe UI", 9, "bold")
        ).pack(
            side="left",
            padx=10,
            pady=5
        )


        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        tk.Label(
            container,
            text="Master Your Algorithms",
            bg=C["bg"],
            fg=C["text"],
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=(35, 2)
        )


        tk.Label(
            container,
            text="Challenge yourself across every major DAA topic.",
            bg=C["bg"],
            fg=C["muted"],
            font=("Segoe UI", 10)
        ).pack(
            pady=(0, 20)
        )


        # ----------------------------------------------------
        # MAIN CARD
        # ----------------------------------------------------

        card = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=40
        )


        # ----------------------------------------------------
        # NAME
        # ----------------------------------------------------

        tk.Label(
            card,
            text="STUDENT NAME",
            bg=C["card"],
            fg=C["muted"],
            font=("Segoe UI", 8, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 6)
        )


        self.nameEntry = tk.Entry(
            card,
            bg=C["input"] if "input" in C else "#0d1625",
            fg=C["text"],
            insertbackground=C["cyan"],
            relief="flat",
            highlightbackground=C["border"],
            highlightthickness=1,
            font=("Segoe UI", 11)
        )

        self.nameEntry.pack(
            fill="x",
            padx=30,
            ipady=9
        )


        # ----------------------------------------------------
        # TOPIC MAIN BUTTON
        # ----------------------------------------------------

        self.topicButton = self.make_button(
            card,
            "📚   ALL TOPICS",
            self.toggle_topics,
            C["card2"],
            30
        )

        self.topicButton.pack(
            fill="x",
            padx=30,
            pady=(17, 5)
        )


        # ----------------------------------------------------
        # TOPIC DROPDOWN
        # ----------------------------------------------------

        self.topicFrame = tk.Frame(
            card,
            bg=C["card2"]
        )


        # ----------------------------------------------------
        # DIFFICULTY MAIN BUTTON
        # ----------------------------------------------------

        self.difficultyButton = self.make_button(
            card,
            "🎯   ALL DIFFICULTIES",
            self.toggle_difficulties,
            C["card2"],
            30
        )

        self.difficultyButton.pack(
            fill="x",
            padx=30,
            pady=(7, 5)
        )


        # ----------------------------------------------------
        # DIFFICULTY DROPDOWN
        # ----------------------------------------------------

        self.difficultyFrame = tk.Frame(
            card,
            bg=C["card2"]
        )


        # ----------------------------------------------------
        # START
        # ----------------------------------------------------

        self.make_button(
            card,
            "START QUIZ   →",
            self.start_quiz,
            C["blue_dark"],
            30,
            2
        ).pack(
            fill="x",
            padx=30,
            pady=(20, 25)
        )


        tk.Label(
            container,
            text="7 Topics  •  42 Questions  •  Easy / Medium / Hard  •  30s",
            bg=C["bg"],
            fg=C["muted"],
            font=("Segoe UI", 8)
        ).pack(
            pady=10
        )


    # ========================================================
    # TOPIC DROPDOWN
    # ========================================================

    def toggle_topics(self):

        if self.topicOpen:

            self.topicFrame.pack_forget()

            self.topicOpen = False

            return


        self.difficultyFrame.pack_forget()

        self.difficultyOpen = False


        for widget in self.topicFrame.winfo_children():
            widget.destroy()


        topics = [
            ("ALL TOPICS", "All"),
            ("Complexity Analysis", "Complexity"),
            ("Sorting Algorithms", "Sorting"),
            ("Searching Algorithms", "Searching"),
            ("Greedy Algorithms", "Greedy"),
            ("Dynamic Programming", "Dynamic Programming"),
            ("Graph Algorithms", "Graph"),
            ("Backtracking", "Backtracking")
        ]


        self.topicFrame.pack(
            fill="x",
            padx=30,
            pady=(0, 7)
        )


        for display, value in topics:

            tk.Button(
                self.topicFrame,
                text=display,
                command=lambda v=value, d=display: self.select_topic(v, d),
                bg=C["card2"],
                fg=C["text"],
                activebackground=C["cyan_dark"],
                activeforeground=C["white"],
                relief="flat",
                bd=0,
                cursor="hand2",
                font=("Segoe UI", 9)
            ).pack(
                fill="x",
                pady=1,
                ipady=4
            )


        self.topicOpen = True


    def select_topic(self, value, display):

        self.selectedTopic = value

        if value == "All":

            self.topicButton.config(
                text="📚   ALL TOPICS"
            )

        else:

            self.topicButton.config(
                text=f"📚   {display.upper()}"
            )


        self.topicFrame.pack_forget()

        self.topicOpen = False


    # ========================================================
    # DIFFICULTY DROPDOWN
    # ========================================================

    def toggle_difficulties(self):

        if self.difficultyOpen:

            self.difficultyFrame.pack_forget()

            self.difficultyOpen = False

            return


        self.topicFrame.pack_forget()

        self.topicOpen = False


        for widget in self.difficultyFrame.winfo_children():
            widget.destroy()


        difficulties = [
            ("ALL DIFFICULTIES", "All"),
            ("Easy", "Easy"),
            ("Medium", "Medium"),
            ("Hard", "Hard")
        ]


        self.difficultyFrame.pack(
            fill="x",
            padx=30,
            pady=(0, 7)
        )


        for display, value in difficulties:

            tk.Button(
                self.difficultyFrame,
                text=display,
                command=lambda v=value, d=display:
                    self.select_difficulty(v, d),
                bg=C["card2"],
                fg=C["text"],
                activebackground=C["cyan_dark"],
                activeforeground=C["white"],
                relief="flat",
                bd=0,
                cursor="hand2",
                font=("Segoe UI", 9)
            ).pack(
                fill="x",
                pady=1,
                ipady=4
            )


        self.difficultyOpen = True


    def select_difficulty(self, value, display):

        self.selectedDifficulty = value

        if value == "All":

            self.difficultyButton.config(
                text="🎯   ALL DIFFICULTIES"
            )

        else:

            self.difficultyButton.config(
                text=f"🎯   {display.upper()}"
            )


        self.difficultyFrame.pack_forget()

        self.difficultyOpen = False


    # ========================================================
    # QUESTION SELECTION
    # ========================================================

    def create_quiz(self):

        topics = [
            "Complexity",
            "Sorting",
            "Searching",
            "Greedy",
            "Dynamic Programming",
            "Graph",
            "Backtracking"
        ]

        difficulties = [
            "Easy",
            "Medium",
            "Hard"
        ]


        selected = []


        # ----------------------------------------------------
        # ALL TOPICS + ALL DIFFICULTIES
        #
        # 1 QUESTION FROM EVERY COMBINATION
        #
        # 7 × 3 = 21 QUESTIONS
        # ----------------------------------------------------

        if (
            self.selectedTopic == "All"
            and
            self.selectedDifficulty == "All"
        ):

            for topic in topics:

                for difficulty in difficulties:

                    pool = [
                        q for q in questionBank
                        if q["topic"] == topic
                        and q["difficulty"] == difficulty
                    ]

                    random.shuffle(pool)

                    if pool:
                        selected.append(pool[0])


            random.shuffle(selected)

            return selected


        # ----------------------------------------------------
        # ONE TOPIC + ALL DIFFICULTIES
        #
        # 2 EASY + 2 MEDIUM + 2 HARD
        # ----------------------------------------------------

        if (
            self.selectedTopic != "All"
            and
            self.selectedDifficulty == "All"
        ):

            for difficulty in difficulties:

                pool = [
                    q for q in questionBank
                    if q["topic"] == self.selectedTopic
                    and q["difficulty"] == difficulty
                ]

                random.shuffle(pool)

                selected.extend(pool[:2])


            random.shuffle(selected)

            return selected


        # ----------------------------------------------------
        # ALL TOPICS + ONE DIFFICULTY
        #
        # 2 FROM EVERY TOPIC
        # ----------------------------------------------------

        if (
            self.selectedTopic == "All"
            and
            self.selectedDifficulty != "All"
        ):

            for topic in topics:

                pool = [
                    q for q in questionBank
                    if q["topic"] == topic
                    and q["difficulty"] == self.selectedDifficulty
                ]

                random.shuffle(pool)

                selected.extend(pool[:2])


            random.shuffle(selected)

            return selected


        # ----------------------------------------------------
        # ONE TOPIC + ONE DIFFICULTY
        # ----------------------------------------------------

        selected = [
            q for q in questionBank
            if q["topic"] == self.selectedTopic
            and q["difficulty"] == self.selectedDifficulty
        ]

        random.shuffle(selected)

        return selected


    # ========================================================
    # START QUIZ
    # ========================================================

    def start_quiz(self):

        name = self.nameEntry.get().strip()

        if not name:

            messagebox.showwarning(
                "Name Required",
                "Please enter your name."
            )

            return


        self.studentName = name

        self.quizQuestions = self.create_quiz()


        if not self.quizQuestions:

            messagebox.showerror(
                "No Questions",
                "No questions are available for this selection."
            )

            return


        self.currentQuestion = 0

        self.score = 0

        self.correctAnswers = 0

        self.wrongAnswers = 0

        self.answersReview = []


        self.show_question()


    # ========================================================
    # QUESTION PAGE
    # ========================================================

    def show_question(self):

        self.clear_screen()

        self.selectedAnswer.set("")

        self.timeLeft = 30

        self.premium_background()


        q = self.quizQuestions[self.currentQuestion]


        # ----------------------------------------------------
        # MAIN CONTAINER
        # ----------------------------------------------------

        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.82,
            relheight=0.90
        )


        # ----------------------------------------------------
        # TOP HEADER
        # ----------------------------------------------------

        header = tk.Frame(
            container,
            bg=C["bg"]
        )

        header.pack(
            fill="x",
            pady=(10, 15)
        )


        tk.Label(
            header,
            text="DAA  /  ALGORITHM CHALLENGE",
            bg=C["bg"],
            fg=C["cyan"],
            font=("Segoe UI", 10, "bold")
        ).pack(side="left")


        tk.Label(
            header,
            text=f"HELLO, {self.studentName.upper()}",
            bg=C["bg"],
            fg=C["muted"],
            font=("Segoe UI", 9, "bold")
        ).pack(side="right")


        # ----------------------------------------------------
        # PROGRESS
        # ----------------------------------------------------

        progressBackground = tk.Frame(
            container,
            bg=C["border"],
            height=5
        )

        progressBackground.pack(
            fill="x",
            pady=(0, 18)
        )


        progress = (
            self.currentQuestion + 1
        ) / len(self.quizQuestions)


        progressBar = tk.Frame(
            progressBackground,
            bg=C["cyan"]
        )

        progressBar.place(
            relwidth=progress,
            relheight=1
        )


        # ----------------------------------------------------
        # CARD
        # ----------------------------------------------------

        card = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True
        )


        # ----------------------------------------------------
        # QUESTION INFO
        # ----------------------------------------------------

        info = tk.Frame(
            card,
            bg=C["card"]
        )

        info.pack(
            fill="x",
            padx=32,
            pady=(27, 10)
        )


        tk.Label(
            info,
            text=f"{q['topic'].upper()}",
            bg="#0c3d4c",
            fg=C["cyan"],
            font=("Segoe UI", 8, "bold"),
            padx=9,
            pady=5
        ).pack(side="left")


        difficultyColors = {
            "Easy": "#064e3b",
            "Medium": "#5b3b08",
            "Hard": "#5c1717"
        }


        tk.Label(
            info,
            text=q["difficulty"].upper(),
            bg=difficultyColors[q["difficulty"]],
            fg=C["white"],
            font=("Segoe UI", 8, "bold"),
            padx=9,
            pady=5
        ).pack(
            side="left",
            padx=7
        )


        tk.Label(
            info,
            text=f"QUESTION {self.currentQuestion + 1} / {len(self.quizQuestions)}",
            bg=C["card"],
            fg=C["muted"],
            font=("Segoe UI", 9, "bold")
        ).pack(side="right")


        # ----------------------------------------------------
        # QUESTION TEXT
        # ----------------------------------------------------

        tk.Label(
            card,
            text=q["question"],
            bg=C["card"],
            fg=C["text"],
            font=("Segoe UI", 18, "bold"),
            wraplength=850,
            justify="left"
        ).pack(
            anchor="w",
            padx=32,
            pady=(12, 18)
        )


        # ----------------------------------------------------
        # TIMER
        # ----------------------------------------------------

        timerRow = tk.Frame(
            card,
            bg=C["card"]
        )

        timerRow.pack(
            fill="x",
            padx=32
        )


        self.timerLabel = tk.Label(
            timerRow,
            text="30s",
            bg=C["card2"],
            fg=C["cyan"],
            font=("Segoe UI", 10, "bold"),
            padx=12,
            pady=5
        )

        self.timerLabel.pack(
            side="right"
        )


        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------

        optionsFrame = tk.Frame(
            card,
            bg=C["card"]
        )

        optionsFrame.pack(
            fill="both",
            expand=True,
            padx=32,
            pady=(10, 5)
        )


        for i, option in enumerate(q["options"]):

            optionBox = tk.Frame(
                optionsFrame,
                bg=C["option"],
                highlightbackground=C["border"],
                highlightthickness=1
            )

            optionBox.pack(
                fill="x",
                pady=5
            )


            radio = tk.Radiobutton(
                optionBox,
                text=f"{chr(65 + i)}    {option}",
                variable=self.selectedAnswer,
                value=option,
                bg=C["option"],
                fg=C["text"],
                activebackground=C["option"],
                activeforeground=C["cyan"],
                selectcolor=C["bg2"],
                font=("Segoe UI", 10, "bold"),
                anchor="w",
                cursor="hand2"
            )

            radio.pack(
                fill="x",
                padx=14,
                pady=11
            )


        # ----------------------------------------------------
        # SUBMIT
        # ----------------------------------------------------

        self.make_button(
            card,
            "SUBMIT ANSWER   →",
            self.submit_answer,
            C["blue_dark"],
            24,
            2
        ).pack(
            pady=20
        )


        self.update_timer()


    # ========================================================
    # TIMER
    # ========================================================

    def update_timer(self):

        if self.timeLeft <= 0:

            self.submit_answer(
                timeout=True
            )

            return


        self.timerLabel.config(
            text=f"{self.timeLeft}s"
        )


        if self.timeLeft <= 10:

            self.timerLabel.config(
                fg=C["red"]
            )

        else:

            self.timerLabel.config(
                fg=C["cyan"]
            )


        self.timeLeft -= 1


        self.timerID = self.root.after(
            1000,
            self.update_timer
        )


    # ========================================================
    # SUBMIT ANSWER
    # ========================================================

    def submit_answer(self, timeout=False):

        if self.timerID:

            try:
                self.root.after_cancel(self.timerID)
            except:
                pass

            self.timerID = None


        q = self.quizQuestions[self.currentQuestion]


        if timeout:

            selected = "Time Expired"

        else:

            selected = self.selectedAnswer.get()


            if not selected:

                messagebox.showwarning(
                    "Select Answer",
                    "Please select an answer."
                )

                self.update_timer()

                return


        correct = selected == q["answer"]


        if correct:

            self.score += 1

            self.correctAnswers += 1

        else:

            self.wrongAnswers += 1


        self.answersReview.append({
            "question": q["question"],
            "selected": selected,
            "correct": q["answer"],
            "is_correct": correct,
            "topic": q["topic"],
            "difficulty": q["difficulty"],
            "explanation": q["explanation"]
        })


        self.show_explanation(
            correct,
            selected,
            q
        )


    # ========================================================
    # EXPLANATION
    # ========================================================

    def show_explanation(self, correct, selected, q):

        self.clear_screen()

        self.premium_background()


        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.76,
            relheight=0.80
        )


        card = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True
        )


        if correct:

            symbol = "✓"
            result = "CORRECT"
            color = C["green"]

        else:

            symbol = "✕"
            result = "INCORRECT"
            color = C["red"]


        tk.Label(
            card,
            text=symbol,
            bg=C["card"],
            fg=color,
            font=("Segoe UI", 42, "bold")
        ).pack(
            pady=(25, 0)
        )


        tk.Label(
            card,
            text=result,
            bg=C["card"],
            fg=color,
            font=("Segoe UI", 22, "bold")
        ).pack()


        tk.Label(
            card,
            text=q["question"],
            bg=C["card"],
            fg=C["text"],
            font=("Segoe UI", 13, "bold"),
            wraplength=780
        ).pack(
            padx=35,
            pady=15
        )


        if selected == "Time Expired":

            tk.Label(
                card,
                text="⏱  Time expired",
                bg=C["card"],
                fg=C["red"],
                font=("Segoe UI", 10, "bold")
            ).pack()

        else:

            tk.Label(
                card,
                text=f"Your answer: {selected}",
                bg=C["card"],
                fg=C["muted"],
                font=("Segoe UI", 10)
            ).pack()


        if not correct:

            tk.Label(
                card,
                text=f"Correct answer: {q['answer']}",
                bg=C["card"],
                fg=C["green"],
                font=("Segoe UI", 10, "bold")
            ).pack(
                pady=5
            )


        # ----------------------------------------------------
        # EXPLANATION BOX
        # ----------------------------------------------------

        explanationBox = tk.Frame(
            card,
            bg=C["card2"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        explanationBox.pack(
            fill="x",
            padx=35,
            pady=15
        )


        tk.Label(
            explanationBox,
            text="💡  EXPLANATION",
            bg=C["card2"],
            fg=C["cyan"],
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 4)
        )


        tk.Label(
            explanationBox,
            text=q["explanation"],
            bg=C["card2"],
            fg=C["text"],
            font=("Segoe UI", 9),
            wraplength=760,
            justify="left"
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )


        if self.currentQuestion + 1 < len(self.quizQuestions):

            text = "NEXT QUESTION   →"

            command = self.next_question

        else:

            text = "VIEW RESULT   →"

            command = self.show_result


        self.make_button(
            card,
            text,
            command,
            C["blue_dark"],
            24
        ).pack(
            pady=10
        )


    # ========================================================
    # NEXT QUESTION
    # ========================================================

    def next_question(self):

        self.currentQuestion += 1

        self.show_question()


    # ========================================================
    # RESULT PAGE
    # ========================================================

    def show_result(self):

        self.clear_screen()


        percentage = int(
            self.score /
            len(self.quizQuestions) *
            100
        )


        # ----------------------------------------------------
        # PERFECT SCORE
        # ----------------------------------------------------

        if percentage == 100:

            self.show_celebration()

            return


        self.premium_background()


        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.72,
            relheight=0.84
        )


        card = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True
        )


        tk.Label(
            card,
            text="QUIZ COMPLETE",
            bg=C["card"],
            fg=C["cyan"],
            font=("Segoe UI", 10, "bold")
        ).pack(
            pady=(30, 5)
        )


        tk.Label(
            card,
            text=self.studentName,
            bg=C["card"],
            fg=C["text"],
            font=("Segoe UI", 25, "bold")
        ).pack()


        tk.Label(
            card,
            text=f"{self.score} / {len(self.quizQuestions)}",
            bg=C["card"],
            fg=C["cyan"],
            font=("Segoe UI", 38, "bold")
        ).pack(
            pady=(18, 0)
        )


        tk.Label(
            card,
            text=f"{percentage}%",
            bg=C["card"],
            fg=C["text"],
            font=("Segoe UI", 19, "bold")
        ).pack()


        if percentage >= 80:

            performance = "Excellent Performance! 🔥"

        elif percentage >= 60:

            performance = "Great Work! 💪"

        elif percentage >= 40:

            performance = "Good Attempt! 📚"

        else:

            performance = "Keep Practicing! 🚀"


        tk.Label(
            card,
            text=performance,
            bg=C["card"],
            fg=C["muted"],
            font=("Segoe UI", 11)
        ).pack(
            pady=8
        )


        # ----------------------------------------------------
        # STAT BOXES
        # ----------------------------------------------------

        stats = tk.Frame(
            card,
            bg=C["card"]
        )

        stats.pack(
            pady=18
        )


        self.stat_box(
            stats,
            "CORRECT",
            self.correctAnswers,
            C["green"]
        ).pack(
            side="left",
            padx=7
        )


        self.stat_box(
            stats,
            "WRONG",
            self.wrongAnswers,
            C["red"]
        ).pack(
            side="left",
            padx=7
        )


        self.stat_box(
            stats,
            "TOTAL",
            len(self.quizQuestions),
            C["cyan"]
        ).pack(
            side="left",
            padx=7
        )


        # ----------------------------------------------------
        # BUTTONS
        # ----------------------------------------------------

        self.make_button(
            card,
            "VIEW ANSWERS",
            self.show_review,
            C["card2"],
            22
        ).pack(
            pady=7
        )


        self.make_button(
            card,
            "NEW TOPIC   →",
            self.show_index,
            C["blue_dark"],
            22
        ).pack(
            pady=5
        )


    # ========================================================
    # STAT BOX
    # ========================================================

    def stat_box(self, parent, title, value, color):

        frame = tk.Frame(
            parent,
            bg=C["card2"],
            highlightbackground=C["border"],
            highlightthickness=1,
            width=120,
            height=70
        )

        frame.pack_propagate(False)


        tk.Label(
            frame,
            text=value,
            bg=C["card2"],
            fg=color,
            font=("Segoe UI", 19, "bold")
        ).pack(
            pady=(7, 0)
        )


        tk.Label(
            frame,
            text=title,
            bg=C["card2"],
            fg=C["muted"],
            font=("Segoe UI", 7, "bold")
        ).pack()


        return frame


    # ========================================================
    # PERFECT SCORE CELEBRATION
    # ========================================================

    def show_celebration(self):

        self.clear_screen()

        self.premium_background()


        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.78,
            relheight=0.86
        )


        card = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["cyan_dark"],
            highlightthickness=2
        )

        card.pack(
            fill="both",
            expand=True
        )


        # ----------------------------------------------------
        # CONFETTI CANVAS
        # ----------------------------------------------------

        self.confettiCanvas = tk.Canvas(
            card,
            bg=C["card"],
            highlightthickness=0
        )

        self.confettiCanvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )


        # ----------------------------------------------------
        # CONTENT
        # ----------------------------------------------------

        content = tk.Frame(
            card,
            bg=C["card"]
        )

        content.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )


        tk.Label(
            content,
            text="🏆",
            bg=C["card"],
            font=("Segoe UI Emoji", 60)
        ).pack()


        tk.Label(
            content,
            text="PERFECT SCORE!",
            bg=C["card"],
            fg=C["cyan"],
            font=("Segoe UI", 29, "bold")
        ).pack(
            pady=5
        )


        tk.Label(
            content,
            text=f"Outstanding work, {self.studentName}!",
            bg=C["card"],
            fg=C["text"],
            font=("Segoe UI", 14, "bold")
        ).pack()


        tk.Label(
            content,
            text="You answered every question correctly.",
            bg=C["card"],
            fg=C["muted"],
            font=("Segoe UI", 10)
        ).pack(
            pady=5
        )


        tk.Label(
            content,
            text=f"{self.score} / {len(self.quizQuestions)}",
            bg=C["card"],
            fg=C["green"],
            font=("Segoe UI", 37, "bold")
        ).pack(
            pady=(15, 0)
        )


        tk.Label(
            content,
            text="100%  •  PERFECT",
            bg=C["card"],
            fg=C["yellow"],
            font=("Segoe UI", 12, "bold")
        ).pack()


        # ----------------------------------------------------
        # NEW TOPIC BUTTON
        # ----------------------------------------------------

        self.make_button(
            content,
            "NEW TOPIC   →",
            self.show_index,
            C["blue_dark"],
            22
        ).pack(
            pady=22
        )


        # Start confetti

        self.animate_confetti()


        # ----------------------------------------------------
        # AUTOMATICALLY RETURN TO INDEX
        #
        # 6 SECONDS
        # ----------------------------------------------------

        self.root.after(
            6000,
            self.auto_new_topic
        )


    def auto_new_topic(self):

        if hasattr(self, "confettiCanvas"):

            try:

                if self.confettiCanvas.winfo_exists():

                    self.show_index()

            except:

                pass


    # ========================================================
    # CONFETTI
    # ========================================================

    def animate_confetti(self):

        if not hasattr(self, "confettiCanvas"):
            return


        try:

            if not self.confettiCanvas.winfo_exists():
                return

        except:

            return


        self.confettiCanvas.delete("all")


        width = max(
            self.confettiCanvas.winfo_width(),
            600
        )

        height = max(
            self.confettiCanvas.winfo_height(),
            500
        )


        symbols = [
            "✦",
            "◆",
            "★",
            "•",
            "✧"
        ]


        confettiColors = [
            C["cyan"],
            C["blue"],
            C["green"],
            C["yellow"],
            C["red"]
        ]


        for _ in range(65):

            x = random.randint(
                10,
                width - 10
            )

            y = random.randint(
                0,
                height
            )


            self.confettiCanvas.create_text(
                x,
                y,
                text=random.choice(symbols),
                fill=random.choice(confettiColors),
                font=(
                    "Segoe UI",
                    random.randint(8, 17),
                    "bold"
                )
            )


        self.confettiID = self.root.after(
            350,
            self.animate_confetti
        )


    # ========================================================
    # REVIEW PAGE
    # ========================================================

    def show_review(self):

        self.clear_screen()

        self.premium_background()


        container = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.84,
            relheight=0.91
        )


        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = tk.Frame(
            container,
            bg=C["bg"]
        )

        header.pack(
            fill="x",
            pady=(5, 10)
        )


        tk.Label(
            header,
            text="ANSWER REVIEW",
            bg=C["bg"],
            fg=C["cyan"],
            font=("Segoe UI", 20, "bold")
        ).pack(side="left")


        tk.Label(
            header,
            text=f"{self.score} / {len(self.quizQuestions)}",
            bg=C["bg"],
            fg=C["text"],
            font=("Segoe UI", 13, "bold")
        ).pack(side="right")


        # ----------------------------------------------------
        # SCROLL AREA
        # ----------------------------------------------------

        outer = tk.Frame(
            container,
            bg=C["card"],
            highlightbackground=C["border"],
            highlightthickness=1
        )

        outer.pack(
            fill="both",
            expand=True
        )


        canvas = tk.Canvas(
            outer,
            bg=C["card"],
            highlightthickness=0
        )


        scrollbar = tk.Scrollbar(
            outer,
            orient="vertical",
            command=canvas.yview
        )


        scrollFrame = tk.Frame(
            canvas,
            bg=C["card"]
        )


        scrollFrame.bind(
            "<Configure>",
            lambda event:
                canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
        )


        canvas.create_window(
            (0, 0),
            window=scrollFrame,
            anchor="nw",
            width=900
        )


        canvas.configure(
            yscrollcommand=scrollbar.set
        )


        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar.pack(
            side="right",
            fill="y"
        )


        # ----------------------------------------------------
        # REVIEW ITEMS
        # ----------------------------------------------------

        for i, item in enumerate(self.answersReview):

            reviewCard = tk.Frame(
                scrollFrame,
                bg=C["card2"],
                highlightbackground=C["border"],
                highlightthickness=1
            )


            reviewCard.pack(
                fill="x",
                padx=20,
                pady=7
            )


            if item["is_correct"]:

                status = "✓ CORRECT"
                statusColor = C["green"]

            else:

                status = "✕ WRONG"
                statusColor = C["red"]


            top = tk.Frame(
                reviewCard,
                bg=C["card2"]
            )

            top.pack(
                fill="x",
                padx=15,
                pady=(10, 4)
            )


            tk.Label(
                top,
                text=f"QUESTION {i + 1}",
                bg=C["card2"],
                fg=C["cyan"],
                font=("Segoe UI", 8, "bold")
            ).pack(side="left")


            tk.Label(
                top,
                text=status,
                bg=C["card2"],
                fg=statusColor,
                font=("Segoe UI", 8, "bold")
            ).pack(side="right")


            tk.Label(
                reviewCard,
                text=item["question"],
                bg=C["card2"],
                fg=C["text"],
                font=("Segoe UI", 10, "bold"),
                wraplength=820,
                justify="left"
            ).pack(
                anchor="w",
                padx=15,
                pady=5
            )


            tk.Label(
                reviewCard,
                text=f"Your answer: {item['selected']}",
                bg=C["card2"],
                fg=C["muted"],
                font=("Segoe UI", 9)
            ).pack(
                anchor="w",
                padx=15,
                pady=2
            )


            tk.Label(
                reviewCard,
                text=f"Correct answer: {item['correct']}",
                bg=C["card2"],
                fg=C["green"],
                font=("Segoe UI", 9, "bold")
            ).pack(
                anchor="w",
                padx=15,
                pady=2
            )


            tk.Label(
                reviewCard,
                text=f"Explanation: {item['explanation']}",
                bg=C["card2"],
                fg=C["text"],
                font=("Segoe UI", 9),
                wraplength=820,
                justify="left"
            ).pack(
                anchor="w",
                padx=15,
                pady=(3, 12)
            )


        # ----------------------------------------------------
        # NEW TOPIC
        # ----------------------------------------------------

        self.make_button(
            container,
            "NEW TOPIC   →",
            self.show_index,
            C["blue_dark"],
            24
        ).pack(
            pady=10
        )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = DAAQuiz(root)

    root.mainloop()