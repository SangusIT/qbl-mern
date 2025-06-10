def get_config():
    try:
        with open('sample_qbl.yaml', 'r', encoding="utf8", errors="ignore") as file:
            data = file.read()
        return data
    except Exception as exc:
        print(exc)

config = get_config()
config_split = config.split('\n')
print(config_split[0].split(':'))
# if second element is blank then it's a header
# also need to count the number of leading tabs
# basically you'll need your own custom parser for this type of YAML file