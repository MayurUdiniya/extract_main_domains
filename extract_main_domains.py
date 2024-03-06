import re
import tldextract

def extract_main_domain(domain):
    extracted = tldextract.extract(domain)
    return f"{extracted.domain}.{extracted.suffix}"

if __name__ == "__main__":
    with open("domains.txt", "r") as file:
        domains = file.read().splitlines()

    main_domains = set()
    for domain in domains:
        main_domain = extract_main_domain(domain)
        main_domains.add(main_domain)

    for main_domain in sorted(main_domains):
        print(main_domain)
