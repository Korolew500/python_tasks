import json


def compare(old: dict, new: dict, diff: list) -> dict:
    all_result = dict()

    def search(old_obj: dict | list, new_obj: dict | list) -> None:

        if isinstance(new_obj, dict):
            for i_key, i_value in new_obj.items():
                if i_key in diff:
                    if new_obj[i_key] != old_obj[i_key]:
                        all_result[i_key] = i_value
                if isinstance(i_value, dict | list):
                    search(old_obj[i_key], new_obj[i_key])

        if isinstance(new_obj, list):
            for number_obj, obj in enumerate(new_obj):
                if isinstance(obj, dict | list):
                    search(old_obj[number_obj], new_obj[number_obj])

    search(old, new)

    return all_result


if __name__ == '__main__':
    with open('json_old.json', 'r', encoding='UTF-8') as old_file:
        with open('json_new.json', 'r', encoding='UTF-8') as new_file:
            old_dict = json.load(old_file)
            new_dict = json.load(new_file)

            diff_list = ["services", "staff", "datetime"]
            result = compare(old_dict, new_dict, diff_list)
            print(result)

            with open('result.json', 'w', encoding='UTF-8') as file_result:
                json.dump(result, file_result, ensure_ascii=False, indent=4)
