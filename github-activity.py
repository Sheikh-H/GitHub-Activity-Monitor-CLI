import os
import sys
import requests
import json
from rich import print as rprint
import time


def ptt(message):
    rprint(f"{message}".encode("utf-16", "surrogatepass").decode("utf-16"))


def fetch_request(username):
    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url, timeout=10).json()

    with open("response.json", "w") as f:
        json.dump(response, f, indent=2)

    with open("response.json", "r") as f:
        data = json.load(f)
        return data


def error_message(*messages):
    clear_screen()
    for message in messages:
        print(message)
        time.sleep(1)
    time.sleep(3)
    clear_screen()
    sys.exit()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def all_activity(username):
    data = fetch_request(username)

    rprint(
        f"\tListing all activities for GitHub user: '[bold green]{username.upper()}[/bold green]'..."
    )
    time.sleep(2)
    for info in data:
        print("-" * 115)
        rprint(
            f"[bold]Event Type[/bold]: [dim]{info['type'].replace("Event", "")}[/dim] \t\t\t\t\t\t\t\t\t [bold]At: [/bold][dim]{info['created_at'].replace('T', " ").replace('Z',"")}[/dim]"
        )
        rprint(f"[bold]Repo Name[/bold]: {info['repo']['name']}")
        payload = info.get("payload", {})
        description = payload.get("description", {})
        if description:
            rprint(
                f"[bold]Repo Description[/bold]: \n{description}".encode(
                    "utf-16", "surrogatepass"
                ).decode("utf-16")
            )


def filtered_activity(username, filter):
    event_types = [
        "commitcommentevent",
        "createevent",
        "deleteevent",
        "discussionevent",
        "forkevent",
        "forkapplyevent",
        "gollumevent",
        "issuecommentevent",
        "issuesevent",
        "labelevent",
        "memberevent",
        "membershipevent",
        "milestoneevent",
        "organizationevent",
        "orgblockevent",
        "pagebuildevent",
        "projectcardevent",
        "projectcolumnevent",
        "projectevent",
        "publicevent",
        "pullrequestevent",
        "pullrequestreviewevent",
        "pullrequestreviewcommentevent",
        "pullrequestreviewthreadevent",
        "pushevent",
        "releaseevent",
        "repositoryevent",
        "repositoryimportevent",
        "repositoryvulnerabilityalertevent",
        "securityadvisoryevent",
        "sponsorshipevent",
        "starevent",
        "statusevent",
        "teamevent",
        "teamaddevent",
        "watchevent",
        "workflowdispatchevent",
        "workflowrunevent",
    ]  # I used AI to generate a list of all possible even types in lowercase to make error handling easier

    if filter.lower() not in event_types:
        error_message(
            "There is no event type with that entry, try another filter.",
            "Here is a list of filters you can use:",
            "['CommitCommentEvent', 'CreateEvent', 'DeleteEvent', 'DiscussionEvent', 'ForkEvent', 'ForkApplyEvent', 'GollumEvent', 'IssueCommentEvent', 'IssuesEvent', 'LabelEvent', 'MemberEvent', 'MembershipEvent', 'MilestoneEvent', 'OrganizationEvent', 'OrgBlockEvent', 'PageBuildEvent', 'ProjectCardEvent', 'ProjectColumnEvent', 'ProjectEvent', 'PublicEvent', 'PullRequestEvent', 'PullRequestReviewEvent', 'PullRequestReviewCommentEvent', 'PullRequestReviewThreadEvent', 'PushEvent', 'ReleaseEvent', 'RepositoryEvent', 'RepositoryImportEvent', 'RepositoryVulnerabilityAlertEvent', 'SecurityAdvisoryEvent', 'SponsorshipEvent', 'StarEvent', 'StatusEvent', 'TeamEvent', 'TeamAddEvent', 'WatchEvent', 'WorkflowDispatchEvent', 'WorkflowRunEvent']",
        )
    data = fetch_request(username)
    rprint(
        f"\tListing [bold blue]{filter[:-5].upper()}[/bold blue] activities for GitHub user: '[bold green]{username.upper()}[/bold green]'..."
    )
    time.sleep(2)
    for info in data:
        if info["type"].lower() == filter.lower():
            print("-" * 115)
            info_type = str(info["type"])
            if info_type:
                rprint(
                    f"[bold green]Event Type[/bold green]: [dim]{info_type[:-5]}[/dim] \t\t\t\t\t\t\t\t\t [bold]At: [/bold][dim]{info['created_at'].replace('T', " ").replace('Z',"")}[/dim]"
                )
            rprint(f"[bold]Repo Name[/bold]: {info['repo']['name']}")
            payload = info.get("payload", {})
            description = payload.get("description", {})
            if description:
                rprint(
                    f"[bold]Repo Description[/bold]: \n{description}".encode(
                        "utf-16", "surrogatepass"
                    ).decode("utf-16")
                )


def main():
    clear_screen()
    if len(sys.argv) == 2:
        all_activity(sys.argv[1])
    elif len(sys.argv) == 3:
        filtered_activity(sys.argv[1], sys.argv[2])
    else:
        error_message(
            "To use this application, enter the GitHub username of the persons GitHub events you would like to see",
            "Usage: github-activity.py 'username'",
            "You can also filter by the type of events by entering it as a parameter after the username",
            "Usage: github-activity.py [username] [filter]",
        )


if __name__ == "__main__":
    main()
