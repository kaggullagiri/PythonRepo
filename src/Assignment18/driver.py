from src.Assignment18.util import filtered_emails

if __name__ == '__main__':
    n = int(input("Enter the number of emails: "))
    emails = [input("Enter email: ") for i in range(n)]

    filtered_emails = filtered_emails(emails)

    print("Filtered and sorted emails:")
    print(filtered_emails)