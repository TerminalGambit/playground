class Player:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name

    def speak(self, message):
        print(f"{self.name}: {message}")

    def shout(self, message):
        print(f"{self.name}: {message.upper()}")

def main():
    player = Player()
    player.set_name("John")
    player.speak("Hello everyone!")
    player.shout("I'm the best player!")


if __name__ == "__main__":
    main()
