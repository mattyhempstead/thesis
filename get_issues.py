import json
import unidiff
from pathlib import Path


# PATH_RAW_ISSUES = 'data/raw/data-dev.json'
# PATH_RAW_ISSUES = 'data/raw/data-test.json'
# PATH_RAW_ISSUES = 'data/raw/data-train.json'


def process_issue(issue_raw):

    if "patch" not in issue_raw:
        # print("Patch missing. Skipping.", issue_raw["repo"], issue_raw["base_commit"])
        print(issue_raw.keys())
        raise Exception("Patch missing?", issue_raw)

    issue = {
        "instance_id": issue_raw["instance_id"],  # Go to https://github.com/{repo}/issues/{num} to get PR link
        "repo": issue_raw["repo"],
        "repo_author": issue_raw["repo"].split("/")[0],
        "repo_name": issue_raw["repo"].split("/")[1],
        "base_commit": issue_raw["base_commit"],
        "created_at": issue_raw["created_at"],
        "version": issue_raw["version"],
        # "environment_setup_commit": issue_raw["environment_setup_commit"],
        "problem_statement": issue_raw["problem_statement"],
        # "patch": issue_raw["patch"],
    }


    issue["repo_url"] = f"https://github.com/{issue['repo']}.git"

    issue_num = issue["instance_id"].split("-")[-1]
    issue["pr_url"] = f"https://github.com/{issue['repo']}/pull/{issue_num}"


    # Calculate modified files from patch
    patch_string = issue_raw["patch"]
    patch_set = unidiff.PatchSet(patch_string)
    modified_files = [patch.target_file[2:] for patch in patch_set]
    issue["modified_files"] = modified_files

    return issue



def get_issues(path_raw_issues: Path):

    # SOURCE_PATH = 'data/swe-bench-dev.json'
    # SOURCE_PATH = 'data/swe-bench.json'

    # Load the file into a local variable
    with open(path_raw_issues, 'r') as file:
        data_raw = json.load(file)

    # print(list(issue.keys()))

    issues = []
    for issue_raw in data_raw:
        try:
            issue = process_issue(issue_raw)
        except Exception as ex:
            print("Failed to process issue", json.dumps(issue_raw, indent=4))
            raise ex

        issues.append(issue)

    # Find changes files
    return issues


if __name__ == "__main__":
    issues = get_issues()

    print("Count:", len(issues))
    print(issues[0])

