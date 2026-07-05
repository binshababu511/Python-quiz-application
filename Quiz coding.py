import tkinter as tk
from tkinter import font as tkfont
import random

# ─────────────────────────────────────────────
#  QUESTION BANK
# ─────────────────────────────────────────────
QUESTIONS = {
    "country": {
        "easy": [
            {"q": "What is the capital of France?",            "opts": ["Paris","London","Berlin","Rome"],           "ans": 0},
            {"q": "Which country has the largest population?", "opts": ["India","USA","China","Russia"],             "ans": 2},
            {"q": "What is the capital of Japan?",             "opts": ["Beijing","Seoul","Tokyo","Bangkok"],        "ans": 2},
            {"q": "Which is the 'Land of the Rising Sun'?",    "opts": ["China","South Korea","Japan","Thailand"],  "ans": 2},
            {"q": "What is the capital of Australia?",         "opts": ["Sydney","Melbourne","Brisbane","Canberra"],"ans": 3},
        ],
        "medium": [
            {"q": "Which is the smallest country in the world?",       "opts": ["Monaco","Vatican City","San Marino","Nauru"],     "ans": 1},
            {"q": "Which country has the most natural lakes?",         "opts": ["Russia","USA","Brazil","Canada"],                 "ans": 3},
            {"q": "Amazon River flows mainly through which country?",  "opts": ["Colombia","Peru","Brazil","Bolivia"],             "ans": 2},
            {"q": "Which country is in both Europe and Asia?",         "opts": ["Turkey","Egypt","Morocco","Israel"],              "ans": 0},
            {"q": "What is the capital of New Zealand?",               "opts": ["Auckland","Christchurch","Wellington","Dunedin"],"ans": 2},
        ],
        "difficult": [
            {"q": "Which country has the most time zones?",            "opts": ["Russia","USA","France","China"],                  "ans": 2},
            {"q": "Which African country is the most populous?",      "opts": ["South Africa","Ethiopia","Egypt","Nigeria"],      "ans": 3},
            {"q": "What is the capital of Bhutan?",                    "opts": ["Kathmandu","Thimphu","Dhaka","Colombo"],         "ans": 1},
            {"q": "Which country has the longest coastline?",          "opts": ["Russia","Australia","Canada","Norway"],          "ans": 2},
            {"q": "Only country with non-rectangular national flag?",  "opts": ["Nepal","Bhutan","Sri Lanka","Maldives"],         "ans": 0},
        ],
    },
    "sports": {
        "easy": [
            {"q": "Players in a soccer team on the field?",    "opts": ["9","11","10","12"],                                "ans": 1},
            {"q": "Which country invented basketball?",        "opts": ["USA","Canada","UK","Spain"],                      "ans": 0},
            {"q": "Which sport uses a shuttlecock?",           "opts": ["Tennis","Squash","Badminton","Table Tennis"],     "ans": 2},
            {"q": "How many rings on the Olympic flag?",       "opts": ["4","6","5","7"],                                  "ans": 2},
            {"q": "Which sport is called 'King of Sports'?",   "opts": ["Cricket","Basketball","Football","Tennis"],       "ans": 2},
        ],
        "medium": [
            {"q": "Which country won the most FIFA World Cups?",       "opts": ["Germany","Argentina","Brazil","Italy"],        "ans": 2},
            {"q": "Most men's Grand Slam singles titles holder?",      "opts": ["Federer","Nadal","Djokovic","Sampras"],       "ans": 2},
            {"q": "How many balls in a cricket over?",                 "opts": ["4","8","5","6"],                              "ans": 3},
            {"q": "'Birdie' is a term used in which sport?",           "opts": ["Cricket","Golf","Tennis","Badminton"],       "ans": 1},
            {"q": "Which country hosted the 2016 Summer Olympics?",    "opts": ["China","UK","USA","Brazil"],                 "ans": 3},
        ],
        "difficult": [
            {"q": "Total Olympic gold medals won by Michael Phelps?",  "opts": ["18","23","20","25"],                         "ans": 1},
            {"q": "Year of the first FIFA World Cup?",                 "opts": ["1928","1934","1930","1926"],                 "ans": 2},
            {"q": "Most goals in a single World Cup tournament?",      "opts": ["Ronaldo","Klose","Just Fontaine","Muller"], "ans": 2},
            {"q": "Diameter of a basketball hoop in inches?",          "opts": ["16","18","20","22"],                         "ans": 1},
            {"q": "Most Olympic gold medals overall (all time)?",      "opts": ["China","Russia","Great Britain","USA"],     "ans": 3},
        ],
    },
    "gk": {
        "easy": [
            {"q": "How many continents are there on Earth?",   "opts": ["5","6","7","8"],                                  "ans": 2},
            {"q": "Chemical symbol for water?",                "opts": ["Wa","HO","H2O","H2"],                             "ans": 2},
            {"q": "Who painted the Mona Lisa?",                "opts": ["Van Gogh","Picasso","Da Vinci","Michelangelo"],   "ans": 2},
            {"q": "Largest planet in our solar system?",       "opts": ["Saturn","Neptune","Uranus","Jupiter"],            "ans": 3},
            {"q": "How many sides does a hexagon have?",       "opts": ["5","7","6","8"],                                  "ans": 2},
        ],
        "medium": [
            {"q": "Who developed the theory of general relativity?", "opts": ["Newton","Bohr","Hawking","Einstein"],        "ans": 3},
            {"q": "Approximate speed of light in vacuum?",          "opts": ["3x10^6 m/s","3x10^8 m/s","3x10^5 m/s","3x10^7 m/s"],"ans": 1},
            {"q": "Who wrote 'Romeo and Juliet'?",                   "opts": ["Dickens","Austen","Shakespeare","Orwell"],   "ans": 2},
            {"q": "Largest organ in the human body?",                "opts": ["Liver","Heart","Lung","Skin"],              "ans": 3},
            {"q": "In which year did World War II end?",              "opts": ["1943","1944","1945","1946"],                "ans": 2},
        ],
        "difficult": [
            {"q": "Atomic number of Gold (Au)?",                     "opts": ["47","78","79","80"],                         "ans": 2},
            {"q": "Who discovered penicillin?",                      "opts": ["Pasteur","Fleming","Lister","Koch"],         "ans": 1},
            {"q": "Coriolis effect influences rotation of?",         "opts": ["Tides","Cyclones","Earthquakes","Tsunamis"],"ans": 1},
            {"q": "Who wrote 'Critique of Pure Reason'?",            "opts": ["Nietzsche","Descartes","Hegel","Kant"],      "ans": 3},
            {"q": "How many bones in the adult human body?",         "opts": ["196","206","216","226"],                     "ans": 1},
        ],
    },
}

CAT_LABELS = {"country": "🌍 Countries", "sports": "🏆 Sports", "gk": "🧠 General Knowledge"}
LVL_LABELS = {"easy": "Easy", "medium": "Medium", "difficult": "Difficult"}
LETTERS    = ["A", "B", "C", "D"]
TIME_LIMIT = 30

# ─────────────────────────────────────────────
#  COLOR PALETTE
# ─────────────────────────────────────────────
BG      = "#0d1117"
SURFACE = "#161b27"
CARD    = "#1e2535"
BORDER  = "#2a3248"
CYAN    = "#22d3ee"
GOLD    = "#fbbf24"
PINK    = "#f472b6"
GREEN   = "#4ade80"
RED     = "#f87171"
ORANGE  = "#fb923c"
WHITE   = "#e2e8f0"
MUTED   = "#64748b"

# ─────────────────────────────────────────────
#  MAIN APPLICATION CLASS
# ─────────────────────────────────────────────
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizMaster — Second Chance Edition")
        self.root.geometry("900x640")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        # state
        self.category       = None
        self.level          = None
        self.questions      = []
        self.current_idx    = 0
        self.score          = 0
        self.chance         = 0
        self.answered       = False
        self.timer_id       = None
        self.timer_val      = TIME_LIMIT
        self.score_history  = []
        self.first_correct  = 0
        self.second_correct = 0
        self.wrongs         = 0
        self.timeouts       = 0

        # fonts
        self.f_title  = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.f_large  = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.f_medium = tkfont.Font(family="Helvetica", size=13, weight="bold")
        self.f_normal = tkfont.Font(family="Helvetica", size=12)
        self.f_small  = tkfont.Font(family="Helvetica", size=10)
        self.f_timer  = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.f_big    = tkfont.Font(family="Helvetica", size=52, weight="bold")

        self.main_frame = tk.Frame(self.root, bg=BG)
        self.main_frame.pack(fill="both", expand=True)

        self.show_category_screen()

    # ── clear all widgets ──────────────────────
    def clear(self):
        for w in self.main_frame.winfo_children():
            w.destroy()
        self.stop_timer()

    # ── top cyan header ────────────────────────
    def make_header(self, title, subtitle=""):
        hdr = tk.Frame(self.main_frame, bg=CYAN, pady=6)
        hdr.pack(fill="x")
        tk.Label(hdr, text=title, font=self.f_title,
                 bg=CYAN, fg=BG).pack()
        if subtitle:
            tk.Label(hdr, text=subtitle, font=self.f_small,
                     bg=CYAN, fg=SURFACE).pack()

    # ── dark card frame ────────────────────────
    def make_card(self, parent, **kw):
        kw.setdefault("highlightbackground", BORDER)
        kw.setdefault("highlightthickness", 1)
        return tk.Frame(parent, bg=CARD, **kw)
    # ══════════════════════════════════════════
    #  SCREEN 1 — CATEGORY
    # ══════════════════════════════════════════
    def show_category_screen(self):
        self.clear()
        self.make_header("🎯  QuizMaster",
                         "Second Chance Edition  ·  30 Seconds Per Question")

        tk.Label(self.main_frame, text="Choose a Category",
                 font=self.f_large, bg=BG, fg=CYAN).pack(pady=(28, 14))

        grid = tk.Frame(self.main_frame, bg=BG)
        grid.pack()

        cats = [
            ("country", "🌍", "Countries",        "Capitals, flags & geography", CYAN),
            ("sports",  "🏆", "Sports",            "Athletes, records & games",   GOLD),
            ("gk",      "🧠", "General Knowledge", "Science, history & culture",  PINK),
        ]
        for cat, icon, name, hint, color in cats:
            card = self.make_card(grid, width=245, height=170,
                                  cursor="hand2",
                                  highlightbackground=color,
                                  highlightthickness=2)
            card.pack(side="left", padx=14, pady=8)
            card.pack_propagate(False)

            inner = tk.Frame(card, bg=CARD)
            inner.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(inner, text=icon,  font=tkfont.Font(size=30), bg=CARD).pack()
            tk.Label(inner, text=name,  font=self.f_medium, bg=CARD, fg=color).pack(pady=(4,2))
            tk.Label(inner, text=hint,  font=self.f_small,  bg=CARD, fg=MUTED,
                     wraplength=210).pack()

            for w in [card, inner] + inner.winfo_children():
                w.bind("<Button-1>", lambda e, c=cat: self.select_category(c))
                try: w.config(cursor="hand2")
                except: pass

        tk.Label(self.main_frame,
                 text="CGB1121 – Python Programming  |  Project Review 2",
                 font=self.f_small, bg=BG, fg=MUTED).pack(side="bottom", pady=8)

    def select_category(self, cat):
        self.category = cat
        self.show_level_screen()

    # ══════════════════════════════════════════
    #  SCREEN 2 — LEVEL
    # ══════════════════════════════════════════
    def show_level_screen(self):
        self.clear()
        self.make_header("📊  Choose Difficulty",
                         f"Category: {CAT_LABELS[self.category]}")

        tk.Label(self.main_frame, text="Select a Level",
                 font=self.f_large, bg=BG, fg=CYAN).pack(pady=(28, 14))

        grid = tk.Frame(self.main_frame, bg=BG)
        grid.pack()

        levels = [
            ("easy",      "🟢", "Easy",      "Beginner · 2 chances · 30 s",      GREEN),
            ("medium",    "🟡", "Medium",    "Intermediate · 2 chances · 30 s",  GOLD),
            ("difficult", "🔴", "Difficult", "Expert · 2 chances · 30 s",        RED),
        ]
        for lvl, icon, name, hint, color in levels:
            card = self.make_card(grid, width=225, height=160,
                                  cursor="hand2",
                                  highlightbackground=color,
                                  highlightthickness=2)
            card.pack(side="left", padx=14, pady=8)
            card.pack_propagate(False)

            inner = tk.Frame(card, bg=CARD)
            inner.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(inner, text=icon,  font=tkfont.Font(size=28), bg=CARD).pack()
            tk.Label(inner, text=name,  font=self.f_medium, bg=CARD, fg=color).pack(pady=(4,2))
            tk.Label(inner, text=hint,  font=self.f_small,  bg=CARD, fg=MUTED).pack()

            for w in [card, inner] + inner.winfo_children():
                w.bind("<Button-1>", lambda e, l=lvl: self.select_level(l))
                try: w.config(cursor="hand2")
                except: pass

        tk.Button(self.main_frame, text="← Back to Categories",
                  font=self.f_small, bg=SURFACE, fg=MUTED,
                  relief="flat", cursor="hand2", padx=14, pady=8,
                  activebackground=CARD, activeforeground=WHITE,
                  command=self.show_category_screen).pack(pady=20)

    def select_level(self, lvl):
        self.level          = lvl
        qs                  = list(QUESTIONS[self.category][lvl])
        random.shuffle(qs)
        self.questions      = qs
        self.current_idx    = 0
        self.score          = 0
        self.first_correct  = 0
        self.second_correct = 0
        self.wrongs         = 0
        self.timeouts       = 0
        self.score_history  = []
        self.show_quiz_screen()

    # ══════════════════════════════════════════
    #  SCREEN 3 — QUIZ
    # ══════════════════════════════════════════
    def show_quiz_screen(self):
        self.clear()
        self.answered = False
        self.chance   = 0

        idx   = self.current_idx
        total = len(self.questions)
        q     = self.questions[idx]

        # save score snapshot for back-nav
        if len(self.score_history) <= idx:
            self.score_history.append(self.score)
        else:
            self.score_history[idx] = self.score

        # ── TOP BAR ──
        top = tk.Frame(self.main_frame, bg=SURFACE, pady=8)
        top.pack(fill="x")

        left = tk.Frame(top, bg=SURFACE)
        left.pack(side="left", padx=16)
        tk.Label(left, text=f"Question {idx+1} of {total}",
                 font=self.f_medium, bg=SURFACE, fg=MUTED).pack(anchor="w")

        bdg = tk.Frame(left, bg=SURFACE)
        bdg.pack(anchor="w", pady=2)
        tk.Label(bdg, text=CAT_LABELS[self.category],
                 font=self.f_small, bg=CYAN, fg=BG,
                 padx=8, pady=2).pack(side="left", padx=(0,6))
        lc = {"easy": GREEN, "medium": GOLD, "difficult": RED}[self.level]
        tk.Label(bdg, text=LVL_LABELS[self.level],
                 font=self.f_small, bg=lc, fg=BG,
                 padx=8, pady=2).pack(side="left")

        right = tk.Frame(top, bg=SURFACE)
        right.pack(side="right", padx=16)

        score_col = tk.Frame(right, bg=SURFACE)
        score_col.pack(side="left", padx=(0, 20))
        tk.Label(score_col, text="SCORE", font=self.f_small, bg=SURFACE, fg=MUTED).pack()
        self.score_lbl = tk.Label(score_col, text=str(self.score),
                                   font=self.f_timer, bg=SURFACE, fg=GOLD)
        self.score_lbl.pack()

        timer_col = tk.Frame(right, bg=SURFACE)
        timer_col.pack(side="left")
        tk.Label(timer_col, text="TIME", font=self.f_small, bg=SURFACE, fg=MUTED).pack()
        self.timer_lbl = tk.Label(timer_col, text=str(TIME_LIMIT),
                                   font=self.f_timer, bg=SURFACE, fg=CYAN)
        self.timer_lbl.pack()

        # ── PROGRESS BAR ──
        pb_bg = tk.Frame(self.main_frame, bg=BORDER, height=5)
        pb_bg.pack(fill="x")
        fill_w = int(900 * (idx / total))
        tk.Frame(pb_bg, bg=CYAN, height=5, width=fill_w).place(x=0, y=0)

        # ── SECOND CHANCE BANNER ──
        self.chance_frame = tk.Frame(self.main_frame, bg="#3a2a00", pady=7)
        tk.Label(self.chance_frame,
                 text="⚠️   Wrong! You have ONE more chance — choose carefully!   (Correct = +5 pts)",
                 font=self.f_small, bg="#3a2a00", fg=GOLD).pack()

        # ── POINTS HINT ──
        ph = tk.Frame(self.main_frame, bg=BG)
        ph.pack(fill="x", padx=20, pady=(6, 0))
        self.pts_hint = tk.Label(ph, text="Correct now  →  +10 pts",
                                  font=self.f_small, bg=BG, fg=MUTED)
        self.pts_hint.pack(anchor="e")

        # ── QUESTION ──
        q_card = self.make_card(self.main_frame, pady=14, padx=16)
        q_card.pack(fill="x", padx=20, pady=(6, 10))
        tk.Label(q_card, text=q["q"], font=self.f_medium,
                 bg=CARD, fg=WHITE, wraplength=830,
                 justify="left").pack(anchor="w")

        # ── OPTIONS (2×2 grid) ──
        opts_outer = tk.Frame(self.main_frame, bg=BG)
        opts_outer.pack(fill="x", padx=20)
        self.opt_btns = []

        for i, opt_text in enumerate(q["opts"]):
            row_i = i // 2
            col_i = i % 2

            bf = tk.Frame(opts_outer, bg=CARD,
                          highlightbackground=BORDER,
                          highlightthickness=1)
            bf.grid(row=row_i, column=col_i, padx=5, pady=4, sticky="ew")
            opts_outer.columnconfigure(col_i, weight=1)

            ll = tk.Label(bf, text=LETTERS[i],
                          font=self.f_medium, bg=BORDER, fg=WHITE,
                          width=3, pady=10)
            ll.pack(side="left")

            tl = tk.Label(bf, text=opt_text,
                          font=self.f_normal, bg=CARD, fg=WHITE,
                          anchor="w", padx=10, pady=10, cursor="hand2")
            tl.pack(side="left", fill="x", expand=True)

            for w in [bf, ll, tl]:
                w.bind("<Button-1>", lambda e, idx=i: self.handle_answer(idx))
                w.config(cursor="hand2")

            self.opt_btns.append((bf, ll, tl))

        # ── FEEDBACK ──
        self.fb_frame = tk.Frame(self.main_frame, bg=BG, pady=3)
        self.fb_frame.pack(fill="x", padx=20, pady=(6, 0))
        self.fb_lbl = tk.Label(self.fb_frame, text="",
                                font=self.f_small, bg=BG, fg=WHITE,
                                wraplength=860, justify="left")
        self.fb_lbl.pack(anchor="w")

        # ── BOTTOM BUTTONS ──
        btn_row = tk.Frame(self.main_frame, bg=BG)
        btn_row.pack(fill="x", padx=20, pady=(4, 8))

        self.next_btn = tk.Button(btn_row, text="Next Question  →",
                                   font=self.f_medium, bg=PINK, fg=BG,
                                   relief="flat", cursor="hand2",
                                   padx=20, pady=8,
                                   activebackground="#c0365c",
                                   command=self.next_question)

        back_text = "🏠  Home" if idx == 0 else f"←  Back to Q{idx}"
        self.back_btn = tk.Button(btn_row, text=back_text,
                                   font=self.f_small, bg=SURFACE, fg=MUTED,
                                   relief="flat", cursor="hand2",
                                   padx=14, pady=8,
                                   activebackground=CARD,
                                   activeforeground=WHITE,
                                   command=self.quiz_back)
        self.back_btn.pack(side="bottom", fill="x", pady=(4, 0))

        # start timer
        self.timer_val = TIME_LIMIT
        self.start_timer()

    # ══════════════════════════════════════════
    #  ANSWER HANDLER
    # ══════════════════════════════════════════
    def handle_answer(self, chosen):
        if self.answered:
            return

        q   = self.questions[self.current_idx]
        ans = q["ans"]

        if chosen == ans:
            # ── CORRECT ──
            self.answered = True
            self.stop_timer()

            pts = 10 if self.chance == 0 else 5
            self.score += pts
            if self.chance == 0:
                self.first_correct += 1
            else:
                self.second_correct += 1

            self.score_lbl.config(text=str(self.score))
            self.chance_frame.pack_forget()

            bf, ll, tl = self.opt_btns[chosen]
            bf.config(highlightbackground=GREEN)
            ll.config(bg=GREEN, fg=BG)
            tl.config(bg="#0f3320", fg=GREEN)

            self._disable_opts()
            msg = f"✅   Correct!  +{pts} points"
            if self.chance == 1:
                msg += "  (2nd chance)"
            self._show_fb(msg, GREEN, "#0f3320")
            self.next_btn.pack(side="top", fill="x", pady=(0, 4))

        else:
            # ── WRONG ──
            bf, ll, tl = self.opt_btns[chosen]
            bf.config(highlightbackground=RED)
            ll.config(bg=RED, fg=WHITE)
            tl.config(bg="#3a0f0f", fg=RED)
            for w in [bf, ll, tl]:
                w.unbind("<Button-1>")
                w.config(cursor="arrow")

            if self.chance == 0:
                # first wrong → second chance
                self.chance = 1
                self.chance_frame.pack(fill="x", padx=20, pady=(4, 0))
                self.pts_hint.config(text="Correct now  →  +5 pts", fg=ORANGE)
                self._show_fb("❌   Wrong! Try again — you have ONE more chance.",
                               RED, "#3a0f0f")
            else:
                # second wrong → reveal answer
                self.answered = True
                self.stop_timer()
                self.wrongs += 1
                self.chance_frame.pack_forget()

                cbf, cll, ctl = self.opt_btns[ans]
                cbf.config(highlightbackground=GOLD)
                cll.config(bg=GOLD, fg=BG)
                ctl.config(bg="#3a2a00", fg=GOLD)

                self._disable_opts()
                self._show_fb(
                    f"💡   Correct answer:  {q['opts'][ans]}   |   0 points",
                    GOLD, "#3a2a00")
                self.next_btn.pack(side="top", fill="x", pady=(0, 4))

    # ══════════════════════════════════════════
    #  TIMER
    # ══════════════════════════════════════════
    def start_timer(self):
        self._tick()

    def _tick(self):
        if self.answered:
            return
        self.timer_lbl.config(text=str(self.timer_val))
        if self.timer_val > 15:
            self.timer_lbl.config(fg=CYAN)
        elif self.timer_val > 7:
            self.timer_lbl.config(fg=GOLD)
        else:
            self.timer_lbl.config(fg=RED)

        if self.timer_val <= 0:
            self._on_timeout()
            return
        self.timer_val -= 1
        self.timer_id = self.root.after(1000, self._tick)

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def _on_timeout(self):
        if self.answered:
            return
        self.answered = True
        self.timeouts += 1
        q   = self.questions[self.current_idx]
        ans = q["ans"]

        self.chance_frame.pack_forget()
        self._disable_opts()

        cbf, cll, ctl = self.opt_btns[ans]
        cbf.config(highlightbackground=GOLD)
        cll.config(bg=GOLD, fg=BG)
        ctl.config(bg="#3a2a00", fg=GOLD)

        self._show_fb(
            f"⏰   Time's up!   Correct answer:  {q['opts'][ans]}   |   0 points",
            ORANGE, "#3a1a00")
        self.next_btn.pack(side="top", fill="x", pady=(0, 4))

    # ══════════════════════════════════════════
    #  HELPERS
    # ══════════════════════════════════════════
    def _disable_opts(self):
        for bf, ll, tl in self.opt_btns:
            for w in [bf, ll, tl]:
                w.unbind("<Button-1>")
                w.config(cursor="arrow")

    def _show_fb(self, msg, fg, bg):
        self.fb_frame.config(bg=bg)
        self.fb_lbl.config(text=msg, fg=fg, bg=bg, padx=10, pady=6)

    # ══════════════════════════════════════════
    #  NAVIGATION
    # ══════════════════════════════════════════
    def next_question(self):
        self.current_idx += 1
        if self.current_idx < len(self.questions):
            self.show_quiz_screen()
        else:
            self.show_result_screen()

    def quiz_back(self):
        self.stop_timer()
        if self.current_idx == 0:
            self.show_category_screen()
        else:
            self.current_idx -= 1
            self.score = self.score_history[self.current_idx]
            self.show_quiz_screen()

    # ══════════════════════════════════════════
    #  SCREEN 4 — RESULT SCREEN
    #  Shows total POINTS (not count)
    #  Full breakdown: X×10 + Y×5 = total
    # ══════════════════════════════════════════
    def show_result_screen(self):
        self.clear()

        total     = len(self.questions)
        max_score = total * 10          # 5 × 10 = 50
        pct       = self.score / max_score

        # grade
        if pct == 1.0:
            emoji, grade, gc = "🏆", "PERFECT SCORE!", GOLD
        elif pct >= 0.8:
            emoji, grade, gc = "🌟", "Excellent!",     GREEN
        elif pct >= 0.6:
            emoji, grade, gc = "👍", "Good Job!",      CYAN
        elif pct >= 0.4:
            emoji, grade, gc = "😐", "Keep Practicing",ORANGE
        else:
            emoji, grade, gc = "😅", "Better Luck Next Time", RED

        self.make_header("📋  Quiz Result",
                         f"{CAT_LABELS[self.category]}   ·   {LVL_LABELS[self.level]}")

        # ── GRADE + SCORE ──────────────────────────
        top_card = self.make_card(self.main_frame, pady=12)
        top_card.pack(fill="x", padx=22, pady=(14, 8))

        tk.Label(top_card, text=f"{emoji}   {grade}",
                 font=self.f_title, bg=CARD, fg=gc).pack()

        score_row = tk.Frame(top_card, bg=CARD)
        score_row.pack(pady=4)

        tk.Label(score_row, text=str(self.score),
                 font=self.f_big, bg=CARD, fg=GOLD).pack(side="left")
        tk.Label(score_row, text=f" / {max_score}  pts",
                 font=self.f_large, bg=CARD, fg=MUTED).pack(side="left",
                                                              pady=(16, 0))

        # ── SCORE BREAKDOWN ────────────────────────
        tk.Label(self.main_frame, text="Score Breakdown",
                 font=self.f_medium, bg=BG, fg=CYAN).pack(anchor="w",
                                                           padx=22, pady=(4, 3))

        bk = self.make_card(self.main_frame)
        bk.pack(fill="x", padx=22, pady=(0, 8))

        rows = [
            ("✅  1st Attempt Correct",
             f"{self.first_correct}  ×  10 pts  =  "
             f"{self.first_correct * 10} pts",
             GREEN),
            ("⚡  2nd Attempt Correct",
             f"{self.second_correct}  ×  5 pts   =  "
             f"{self.second_correct * 5} pts",
             GOLD),
            ("❌  Both Attempts Wrong",
             f"{self.wrongs} question(s)  =  0 pts",
             RED),
            ("⏰  Timed Out",
             f"{self.timeouts} question(s) =  0 pts",
             ORANGE),
        ]

        for label, value, color in rows:
            row_f = tk.Frame(bk, bg=CARD, pady=7)
            row_f.pack(fill="x", padx=14)
            tk.Label(row_f, text="●", font=self.f_normal,
                     bg=CARD, fg=color, width=2).pack(side="left")
            tk.Label(row_f, text=label, font=self.f_normal,
                     bg=CARD, fg=WHITE, anchor="w").pack(side="left",
                                                          fill="x", expand=True)
            tk.Label(row_f, text=value, font=self.f_medium,
                     bg=CARD, fg=color, anchor="e").pack(side="right")
            tk.Frame(bk, bg=BORDER, height=1).pack(fill="x", padx=14)

        # total row
        tot_f = tk.Frame(bk, bg=SURFACE, pady=9)
        tot_f.pack(fill="x")
        tk.Label(tot_f, text="   🎯  Total Score",
                 font=self.f_medium, bg=SURFACE, fg=WHITE).pack(side="left", padx=14)
        tk.Label(tot_f,
                 text=f"{self.score} / {max_score} pts",
                 font=self.f_medium, bg=SURFACE, fg=CYAN).pack(side="right", padx=14)

        # formula line  e.g.  3 × 10pts  +  1 × 5pts  =  35 pts
        formula = f"{self.first_correct} × 10pts"
        if self.second_correct:
            formula += f"  +  {self.second_correct} × 5pts"
        formula += f"  =  {self.score} pts"
        tk.Label(self.main_frame, text=formula,
                 font=self.f_small, bg=BG, fg=MUTED).pack(pady=(2, 8))

        # ── ACTION BUTTONS ─────────────────────────
        btn_row = tk.Frame(self.main_frame, bg=BG)
        btn_row.pack(pady=4)

        tk.Button(btn_row, text="🔄  Retry Same Level",
                  font=self.f_small, bg=SURFACE, fg=WHITE,
                  relief="flat", cursor="hand2", padx=14, pady=8,
                  activebackground=CARD,
                  command=lambda: self.select_level(self.level)
                  ).pack(side="left", padx=8)

        tk.Button(btn_row, text="📊  Change Level",
                  font=self.f_small, bg=SURFACE, fg=WHITE,
                  relief="flat", cursor="hand2", padx=14, pady=8,
                  activebackground=CARD,
                  command=self.show_level_screen
                  ).pack(side="left", padx=8)

        tk.Button(btn_row, text="🏠  Home",
                  font=self.f_small, bg=PINK, fg=BG,
                  relief="flat", cursor="hand2", padx=20, pady=8,
                  activebackground="#c0365c",
                  command=self.show_category_screen
                  ).pack(side="left", padx=8)


# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = QuizApp(root)
    root.mainloop()