import time
from pathlib import Path
from git import Repo
from get_issues import get_issues


def clone_issues_repos(path_repos_dir: Path, path_raw_issues: Path, verbose=False):
    print("Cloning repos for", path_raw_issues, 'into', path_repos_dir)

    # Loop over all repos and clone them
    issues = get_issues(path_raw_issues)
    
    #print(issues[0])

    for issue in issues:
        time_start = time.time()

        if verbose:
            print("Cloning Issue:", issue["repo"], issue["base_commit"])
    
        clone_path = path_repos_dir / issue['repo_name']
    
        # Skip if clone path exists
        # This is optional bc it doesn't handle half cloned repos
        if clone_path.exists():
            if verbose:
                print("Repo folder already exists. Skipping.")
            continue
    
        print(f"Cloning repository into {clone_path}")
        repo = Repo.clone_from(issue['repo_url'], to_path=clone_path)
    
        repo.git.checkout(issue['base_commit'])
    
        print(f"Cloned issue in {time.time()-time_start:.2f}s")
    
