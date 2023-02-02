class UtilsHelper:

    @staticmethod
    def get_values_from_dict(target: dict):
        return {
            k : v
            for k, v in target.items()
            if v is not None
        }