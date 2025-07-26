import json
from codewars import get_kata_completed, get_kata_description, get_kata_completed_solution
from bd import add_kata_len_in_json_file, get_kata_len_from_json_file
from file_gestion import write_python_file, write_description_file, regroup_fils_by_name
from github import init_git, add_files_to_git, commit_changes, set_remote, push_to_remote

def main():
    username = input("Enter your Codewars username: ").strip()
    kata_datas = get_kata_personal_info(get_kata_completed(username))
    kata_completed_data = get_kata_completed_solution(username)
    if kata_completed_data is not None and kata_datas is not None:
        nb_of_new_katas = get_nb_of_kata_to_add(kata_datas)
        if nb_of_new_katas > 0:
            print(f"You have {nb_of_new_katas} new katas to add.")
            add_kata_len_in_json_file(len(kata_datas))
            create_kata_files(kata_datas, kata_completed_data, nb_of_new_katas)
            init_git()
            add_files_to_git()
            commit_changes(f"Add {nb_of_new_katas} new katas and their descriptions")
            set_remote(input("Enter your remote repository URL: ").strip())
            push_to_remote()
            print("All new katas have been added and pushed to your GitHub repository.")

            
        else:
            print("No new katas to add.")
            
    


def get_kata_personal_info(kata_data):
    if kata_data is not None:
        print(f"Total completed katas: {len(kata_data)}")
        kata_new_datas = {}
        for kata in kata_data:
            kata_new_data = {"name": kata["name"],"language": kata["completedLanguages"], "desc": get_kata_description(kata["id"])}
            kata_new_datas[kata["id"]] = kata_new_data
        return kata_new_datas
    else:
        print("No completed katas found or an error occurred.")
        return None

def get_nb_of_kata_to_add(kata_datas):
    previous_len = get_kata_len_from_json_file()
    if kata_datas is not None:
        return len(kata_datas) - previous_len
    else:
        print("No kata data available.")
        return 0
    
def create_kata_files(kata_datas, kata_completed_data, len):
    if kata_datas is not None and kata_completed_data is not None:
        for kata_id, kata_info in kata_datas.items():
            if len > 0:
                if kata_id not in kata_completed_data:
                    print(f"Kata {kata_info['name']} not found in completed solutions.")
                    continue
                print(f"Creating files for kata: {kata_info['name']}")
                file_name = ""+kata_id
                python_file = write_python_file(f"{file_name}.py", kata_completed_data[kata_id]["code"])
                desc_file = write_description_file(f"{file_name}_description.txt", kata_info["desc"], kata_info["name"])
                if python_file and desc_file:
                    regroup_fils_by_name(python_file, file_name)
                    regroup_fils_by_name(desc_file, file_name)
                len -= 1
            else:
                print("No new katas to create files for.")
                break
    else:
        print("No kata data to create files.")
if __name__ == "__main__":
    main()