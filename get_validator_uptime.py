import requests
from datetime import datetime

from repositories.validator_repository import validator_repository
from repositories.validator_uptime_repository import validator_uptime_repository


class GetValidatorUptime:
    def __init__(self):
        pass

    def get_all_validators(self):
        """
        Get all validators from the validator repository.
        """
        return validator_repository.get_all_validators()

    def get_validator_uptime(self, vote: str):
        response = requests.get(f"https://api.stakewiz.com/validator_delinquencies/{vote}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def run(self):
        """
        Main function to get validator uptime and save it to the database.
        """
        validators = self.get_all_validators()
        for validator in validators:
            print(validator.id)
            vote = validator.vote
            if vote:
                uptime_datas = self.get_validator_uptime(vote)
                if uptime_datas:
                    for uptime_data in uptime_datas:
                        date = datetime.strptime(uptime_data["date"], "%Y-%m-%d").date()
                        delinquent_minutes = int(uptime_data["delinquent_minutes"])
                        print(f"Validator: {validator.identity}, Date: {date}, Delinquent Minutes: {delinquent_minutes}")
                        validator_uptime_repository.create({
                            "identity": validator.identity,
                            "created_at": date,
                            "delinquent": delinquent_minutes,
                        })



if __name__ == "__main__":
    get_validator_uptime = GetValidatorUptime()
    get_validator_uptime.run()
