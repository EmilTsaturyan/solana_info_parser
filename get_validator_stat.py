import requests

from repositories.validator_repository import validator_repository
from repositories.validator_stat_repository import validator_stat_repository
from db.models import ValidatorStat


class ValidatorStats:
    def __init__(self):
        pass

    def get_all_validators(self):
        """
        Get all validators from the validator repository.
        """
        return validator_repository.get_all_validators()

    def get_validator_stat(self, vote: str):
        response = requests.get(f"https://solanacompass.com/stats?validator={vote}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for validator {vote}: {response.status_code}")
            return None
    
    def parse_validator_stat(self, validator_stat):
        """
        Parse the validator stat data to extract relevant information.
        """
        epoch_charts = validator_stat.get("epochCharts", {})
        validator_apy = epoch_charts.get("validatorAPY", {})
        validator_apy_data = validator_apy.get("data", {})
        epoch_trends = validator_stat.get("epochTrends", {})

        return validator_apy_data, epoch_trends
    
    def run(self):
        """
        Main function to get validator stats and save it to the database.
        """
        validators = self.get_all_validators()
        for validator in validators:
            vote = validator.vote
            print(f"Processing validator: {validator.identity} with vote: {vote} with id: {validator.id}")
            if vote:
                validator_stat = self.get_validator_stat(vote)
                if validator_stat:
                    validator_apy_data, epoch_trends = self.parse_validator_stat(validator_stat)
                    
                    validators_stats = []
                    for epoch, apy in validator_apy_data.items():
                        epoch_trend = epoch_trends.get(epoch, {})

                        validator_stat = ValidatorStat(**{
                            "identity": validator.identity,
                            "epoch": int(epoch),
                            "activatedStake": int(epoch_trend.get("balance", 0)),
                            "vote": validator.vote,
                            "apy": float(apy),
                        })
                        validators_stats.append(validator_stat)
                    
                    validator_stat_repository.add_many_validator_stats(validators_stats, 1000)

                        



if __name__ == "__main__":
    validator_stats = ValidatorStats()
    validator_stats.run()
