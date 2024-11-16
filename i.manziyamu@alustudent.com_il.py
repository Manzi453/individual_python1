#Assignment class
class Assignment:
    def _init_(self, name, type, score, weight):
        self.name = name
        self.type = type
        self.score = score
        self.weight = weight

    def weighted_score(self):
        return (self.score * self.weight) / 100


# Define the Student class
class Student:
    def _init_(self, assignments):
        self.assignments = assignments
        self.formative_assignments = [a for a in assignments if a.type == 'FA']
        self.summative_assignments = [a for a in assignments if a.type == 'SA']

    def calculate_weighted_totals(self):
        formative_total = sum(a.weighted_score() for a in self.formative_assignments)
        summative_total = sum(a.weighted_score() for a in self.summative_assignments)
        return formative_total, summative_total

    def check_progression(self):
        formative_total, summative_total = self.calculate_weighted_totals()
        passed_formative = formative_total >= 30
        passed_summative = summative_total >= 20

        if passed_formative and passed_summative:
            return "Pass: You have progressed."
        elif not passed_formative and not passed_summative:
            return "Fail: Retake the course."
        elif not passed_formative and passed_summative:
            return "Fail: Low score in formative assignments. Retake needed."
        else:
            return "Fail: Low score in summative assignments. Retake needed."

    def resubmission_eligibility(self):
        # Find formative assignments with scores below 50%
        eligible_for_resubmission = [
            a for a in self.formative_assignments if a.score < 50
        ]
        return eligible_for_resubmission

    def display_transcript(self, order="ascending"):
        # Sort assignments based on score
        sorted_assignments = sorted(
            self.assignments,
            key=lambda a: a.score,
            reverse=(order == "descending")
        )

        print(f"\nTranscript Breakdown ({order.capitalize()} Order):")
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-----------------------------------------------------------")
        for a in sorted_assignments:
            print(f"{a.name:<18} {a.type:<15} {a.score:<10} {a.weight}")
        print("-----------------------------------------------------------")


# Sample usage of the application
if name == "_main_":
    # Collect assignments data from user or define them here for testing
    assignments = [
        Assignment("Assignment 1", "FA", 45, 15),
        Assignment("Assignment 2", "FA", 90, 10),
        Assignment("Assignment 3", "FA", 45, 10),
        Assignment("Assignment 4", "FA", 80, 15),
        Assignment("Assignment 5", "FA", 48, 10),
        Assignment("Midterm", "SA", 34, 20),
        Assignment("Final Exam", "SA", 95, 20)
    ]

    # Create a Student object with these assignments
    student = Student(assignments)

    # Calculate and display progression status
    print(student.check_progression())

    # Check for resubmission eligibility
    resubmissions = student.resubmission_eligibility()
    if resubmissions:
        print("\nEligible for Resubmission:")
        for a in resubmissions:
            print(f"{a.name} (Score: {a.score}%)")
    else:
        print("\nNo assignments eligible for resubmission.")

    # Display transcript in desired order
    order = input("Enter transcript order (ascending/descending): ").strip().lower()
    student.display_transcript(order)
