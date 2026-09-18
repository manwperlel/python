discography = {
    "Padlock, hair": 2024,
    "Cellinisilio": 2025,
    "1-1": 2026
}

discography.update({"The Yellow Album": 2027})


for album, year in discography.items():
    print(f"The album '{album}' was released in {year}.")

discography.pop("The Yellow Album")
print(discography.get("The Yellow Album"))