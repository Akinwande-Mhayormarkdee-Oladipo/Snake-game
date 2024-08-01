from turtle import Turtle
ALIGN = 'center'
FONT_TUPLE = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score"""
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT_TUPLE)

    def increase_score(self):
        """Increase the score by 1"""
        self.score += 1
        self.update_scoreboard()
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_scoreboard()

    def game_over(self):
        """Show game over message"""
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT_TUPLE)

    def reset_score(self):
        """Reset the score"""
        self.score = 0
        self.update_scoreboard()
