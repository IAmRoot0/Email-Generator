import argparse

def generate_email_addresses(first_name, last_name, domain):
    # List of common email formats
    email_formats = [
        f"{first_name}.{last_name}@{domain}",
        f"{first_name[0]}{last_name}@{domain}",
        f"{first_name}{last_name}@{domain}",
        f"{last_name}.{first_name}@{domain}",
        f"{first_name}_{last_name}@{domain}",
        f"{first_name[0]}_{last_name}@{domain}",
        f"{first_name}{last_name[0]}@{domain}"
    ]
    
    return email_formats

def process_file(file_path, domain):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        name = line.strip().split()
        if len(name) == 2:
            first_name, last_name = name
            emails = generate_email_addresses(first_name, last_name, domain)
            print(f"\nGenerated Email Addresses for {first_name} {last_name}:")
            for email in emails:
                print(email)
        else:
            print(f"Invalid name format in line: '{line.strip()}'")

def main():
    parser = argparse.ArgumentParser(description='Generate email addresses from names.')
    parser.add_argument('-f', '--file', type=str, help='Path to the text file containing names (first last).')
    parser.add_argument('-n', '--name', nargs=2, metavar=('FIRST_NAME', 'LAST_NAME'), 
                        help='First and last name to generate email addresses.')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Email domain (e.g., domain.com).')

    args = parser.parse_args()

    if args.file:
        process_file(args.file, args.domain)
    elif args.name:
        first_name, last_name = args.name
        emails = generate_email_addresses(first_name, last_name, args.domain)
        print(f"\nGenerated Email Addresses for {first_name} {last_name}:")
        for email in emails:
            print(email)
    else:
        print("Please provide either a file with names or individual names.")

if __name__ == "__main__":
    main()
