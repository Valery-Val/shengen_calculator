from datetime import datetime, timedelta, date
import yaml

def config():
    with open("const.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":

    my_config = config()
    number_of_entries = int(input("How many times did you enter the Shengen area? \n"))
    counting_entries = 1
    my_dates_in_shengen = {}
    check_date = date.today() - timedelta(days=180)
    my_limit_in_shengen = my_config["LIMIT"]
    my_limit_in_bulgaria = my_config["LIMIT"]
    for i in range(number_of_entries):
        new_date = input(f"Enter your {counting_entries} entry date in format DD/MM/YY \n")
        entry_date = datetime.strptime(new_date, '%d/%m/%y').date()
        country = input("What country was it? \n")
        if country in my_config["SHENGEN"]:
            day_number = int(input("How many days did you spend there? \n"))
            my_dates_in_shengen[entry_date] = day_number
            if check_date <= entry_date:
                my_limit_in_shengen -= day_number
                my_limit_in_bulgaria -= day_number
            elif check_date <= entry_date + timedelta(days=day_number):
                my_limit_in_shengen -= (entry_date + timedelta(days=day_number)) - check_date
                my_limit_in_bulgaria -= (entry_date + timedelta(days=day_number)) - check_date
            elif check_date > entry_date + timedelta(days=day_number) and check_date > entry_date:
                pass
            else:
                print("Something went wrong")
        elif country == "Bulgaria":
            day_number = int(input("How many days did you spend there? \n"))
            if check_date <= entry_date:
                my_limit_in_bulgaria -= day_number
            elif check_date <= entry_date + timedelta(days=day_number):
                my_limit_in_bulgaria -= (entry_date + timedelta(days=day_number)) - check_date
            elif check_date > entry_date + timedelta(days=day_number) and check_date > entry_date:
                pass
            else:
                print("Something went wrong")
        else:
            pass
        counting_entries += 1

    # print(number_of_entries)
    # print(my_dates_in_shengen)
    print('------')
    print(f"""You have {my_limit_in_shengen} days left that you can spend in Shengen area. \n
    You can also spend {my_limit_in_bulgaria} days in Bulgaria.""")
