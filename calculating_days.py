from datetime import datetime, timedelta, date
import yaml

def config():
    with open("const.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":

    def date_validation():
        new_d = input(f"Enter your {counting_entries} entry date in format DD/MM/YY \n")
        check_this = datetime.strptime(new_d, '%d/%m/%y').date()
        if check_this <= date.today():
            if my_dates_in_shengen == {} or check_this >= (max(my_dates_in_shengen) + timedelta(days =(my_dates_in_shengen[(max(my_dates_in_shengen))]))):
                return check_this
            else:
                print("Are you sure? It seems that you haven't finished the previous trip yet. \nLet's try again!")
                date_validation()
        else:
            print("Please, enter the valid date")
            date_validation()

    def period_validation():
        day_number = int(input("How many days did you spend there? \n"))
        if (my_limit_in_shengen - day_number) >= 0:
            return int(day_number)
        else:
            print("It's already more than 90 days. Enter the appropriate number of days. \n")
            period_validation()

    my_config = config()
    number_of_entries = int(input("How many times did you enter the Shengen area? \n"))
    counting_entries = 1
    my_dates_in_shengen = {}
    check_date = date.today() - timedelta(days=180)
    my_limit_in_shengen = my_config["LIMIT"]
    my_limit_in_bulgaria = my_config["LIMIT"]
    for i in range(number_of_entries):
        entry_date = date_validation()
        country = input("What country was it? \n")
        if country in my_config["SHENGEN"]:
            day_number = period_validation()
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
            day_number = period_validation()
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


    print('------')
    print(f"""You have {my_limit_in_shengen} days left that you can spend in Shengen area. \n
    You can also spend {my_limit_in_bulgaria} days in Bulgaria.""")
