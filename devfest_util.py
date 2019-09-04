import pandas as pd


def get_attendees():
    csv_file = pd.DataFrame(pd.read_csv("attendee_list.csv", sep=",", header=0, index_col=False))
    csv_file.to_json("file.json", orient="records", date_format="epoch", double_precision=10,
                     force_ascii=True, date_unit="ms", default_handler=None)
    print(csv_file)
    return None
