import sys
 

class Member:
    """Represents a single gym member."""
    def __init__(self, member_id, name, age, gender, phone, bmi=0):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.bmi = bmi

    def __str__(self):
        return f"ID: {self.member_id} | Name: {self.name} | Phone: {self.phone}"


class GymManager:
    """Manages the collection of members and gym operations."""
    def __init__(self):
        self.members = {} # Dictionary to store members {id: MemberObject}

    def add_member(self):
        print("\n          --- Add New Member ---")
        try:
            m_id = input("Enter Member ID (unique): ").strip()
            if m_id in self.members:
                print("Error: ID already exists.")
                return

            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            gender = input("Enter Gender (M/F): ").strip().upper()
            phone = input("Enter Phone Number: ").strip()

            # Optional: Calculate BMI immediately
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))
            bmi = round(weight / (height ** 2), 2)

            new_member = Member(m_id, name, age, gender, phone, bmi)
            self.members[m_id] = new_member
            print(f"Success! Member {name} added with BMI {bmi}.")

        except ValueError:
            print("Invalid input! Age, weight, and height must be numbers.")


    def view_all_members(self):
        print("\n           --- All Members ---")
        if not self.members:
            print("No members found.")
            return

        print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Gender':<8} {'BMI':<6} {'Phone':<15}")
        print("-" * 70)
        for m in self.members.values():
            print(f"{m.member_id:<10} {m.name:<20} {m.age:<5} {m.gender:<8} {m.bmi:<6} {m.phone:<15}")


    def search_member(self):
        print("\n           --- Search Member ---")
        m_id = input("Enter Member ID to search: ").strip()
        member = self.members.get(m_id)

        if member:
            print("\nMember Found:")
            print(f"Name: {member.name}")
            print(f"Age: {member.age}")
            print(f"Contact: {member.phone}")
            print(f"BMI Score: {member.bmi}")

            # Simple BMI Category logic
            if member.bmi < 18.5: category = "Underweight"
            elif 18.5 <= member.bmi < 24.9: category = "Normal"
            else: category = "Overweight"
            print(f"Status: {category}")
        else:
            print("Member ID not found.")

    def delete_member(self):
        print("\n           --- Delete Member ---")
        m_id = input("Enter Member ID to delete: ").strip()
        if m_id in self.members:
            removed = self.members.pop(m_id)
            print(f"Member {removed.name} deleted successfully.")
        else:
            print("Member ID not found.")

def main():
    gym = GymManager()


    while True:
        print("\n============================")
        print("   GYM MANAGEMENT SYSTEM    ")
        print("============================")
        print("1. Add Member")
        print("2. View All Members")
        print("3. Search Member (Details & BMI)")
        print("4. Delete Member")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            gym.add_member()
        elif choice == '2':
            gym.view_all_members()
        elif choice == '3':
            gym.search_member()
        elif choice == '4':
            gym.delete_member()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
