class Pet():
    def __init__(
        self,
        portrait="asserts/calm.png",
        name="",
        satiety=100,
        activity=100,
        cheerfulness=100,
        mood=300,
        satiety_change=1,
        activity_change=1,
        cheerfulness_change=1,
        mood_change=1
    ):
        self.portrait = portrait
        self.name = name
        self.satiety = satiety
        self.activity = activity
        self.cheerfulness = cheerfulness        
        self.mood = mood
        self.satiety_change = satiety_change
        self.activity_change = activity_change
        self.cheerfulness_change = cheerfulness_change
        self.mood_change = mood_change

    def feed(self, calories):
        self.fullness += calories
        print(f"{self.name} съел {calories} и теперь у него {self.satiety}")

