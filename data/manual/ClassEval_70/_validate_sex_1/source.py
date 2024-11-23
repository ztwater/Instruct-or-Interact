class PersonRequest:
    def _validate_sex(sex):
        if sex in ['Man', 'Woman', 'UGM']:
            return sex
        else:
            return None