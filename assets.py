COUNTRY_FILE = "assets/country-options.txt"

def get_countries_list() -> list or None:
    with open(COUNTRY_FILE, "r") as f_countries:
        countries = [country.split("\n")[0] for country in f_countries.readlines()]

    return countries

