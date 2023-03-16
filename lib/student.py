class Student:
    def hello(self, phrase=""):
        print(f"Hey there! I'm so excited to learn stuff.\n{phrase}" if phrase != "" else "Hey there! I'm so excited to learn stuff.")

    def raise_hand(self, phrase="Pick me!"):
        print(phrase)

class ChattyStudent(Student):
    def hello(self):
        super().hello("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for i in range(10):
            super().raise_hand()


stud=Student()
stud.hello()
stud.raise_hand()

chatty=ChattyStudent()
chatty.hello()    
chatty.raise_hand()