class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        # Call the parent class's hello() method
        super().hello()
        # Add additional chatty behavior
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        # Call super() ten times to print "Pick me!" ten times
        for _ in range(10):
            super().raise_hand()

# Example usage:
student = Student()
student.hello()         # Output: "Hey there! I'm so excited to learn stuff."
student.raise_hand()    # Output: "Pick me!"

chatty_student = ChattyStudent()
chatty_student.hello()  # Output: "Hey there! I'm so excited to learn stuff." followed by the chatty message
chatty_student.raise_hand()  # Output: "Pick me!" printed ten times
