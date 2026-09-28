# Community Food Donation Tracker
# This program keeps track of food donations and displays
# statistics about the donations that were entered.

print("===================================")
print("   Community Food Donation Tracker")
print("===================================")

donations = []

try:
    number_of_donations = int(input("How many donations wouldl you like to enter?"))

    if number_of_donations <= 0:
        print("Please enter at least one donation.")

    else:
        for i in range(number_of_donations):

            try:
                print("\nDonation", i + 1)
                items = int(input("Enter the number of food item donated: "))

                if items < 0:
                    print("The number of items cannot be negative.")
                else:
                    donations.append(items)
                    print("Donations recorded successfully.")

            except ValueError:
                print("Invalid input, Please enter a whole number.")

            finally:
                print("Donation entry processed.")

             # Display statistics if valid donations were entered
        if len(donations) > 0:
            total = sum(donations)
            average = total / len(donations)
            largest = max(donations)
            smallest = min(donations)

            print("\n===================================")
            print("         Donation Statistics")
            print("===================================")

            print("Valid donations:", len(donations))
            print("Total food items donated:", total)
            print("Average items per donation:", round(average, 2))
            print("Largest donation:", largest)
            print("Smallest donation:", smallest)

        else:
            print("\nNo valid donations were entered.")

except ValueError:
    print("Invalid input. The number of donations must be a whole number.")

finally:
    print("\nThank you for helping support the community!")
    print("Program finished.")