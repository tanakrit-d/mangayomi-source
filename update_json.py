import json
import re
import requests
from datetime import datetime


def fetch_all_releases(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(api_url, headers=headers)
    releases = response.json()
    sorted_releases = sorted(releases, key=lambda x: x["published_at"], reverse=False)

    return sorted_releases


def fetch_latest_release(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(api_url, headers=headers)
    releases = response.json()
    sorted_releases = sorted(releases, key=lambda x: x["published_at"], reverse=True)

    if sorted_releases:
        return sorted_releases[0]

    raise ValueError("No release found.")


def purge_old_news(data, fetched_versions):
    if "news" not in data:
        return

    valid_identifiers = {f"release-{version}" for version in fetched_versions}

    data["news"] = [
        entry for entry in data["news"] if entry["identifier"] in valid_identifiers
    ]


def update_json_file(json_file, fetched_data_all, fetched_data_latest):
    with open(json_file, "r") as file:
        data = json.load(file)

    app = data["apps"][0]

    if "versions" not in app:
        app["versions"] = []

    fetched_versions = []

    for release in fetched_data_all:
        full_version = release["tag_name"].lstrip("v")
        version = re.search(r"(\d+\.\d+\.\d+)", full_version).group(1)
        version_date = release["published_at"]
        fetched_versions.append(version)

        description = release["body"]
        keyword = "Mangayomi Release Information"
        if keyword in description:
            description = description.split(keyword, 1)[1].strip()

        description = re.sub("<[^<]+?>", "", description)  # Remove HTML tags
        description = (
            description.replace(r"\*{2}", "").replace("-", "•").replace("`", '"')
        )

        download_url = next(
            (
                asset["browser_download_url"]
                for asset in release["assets"]
                if asset["name"].endswith(".ipa")
            ),
            None,
        )
        size = next(
            (
                asset["size"]
                for asset in release["assets"]
                if asset["browser_download_url"] == download_url
            ),
            None,
        )

        version_entry = {
            "version": version,
            "date": version_date,
            "localizedDescription": description,
            "downloadURL": download_url,
            "size": size,
        }

        app["versions"] = [v for v in app["versions"] if v["version"] != version]

        if download_url:
            app["versions"].insert(0, version_entry)

    latest_version = fetched_data_latest["tag_name"].lstrip("v")
    tag = fetched_data_latest["tag_name"]
    version_match = re.search(r"(\d+)\.(\d+)\.(\d+)", latest_version)

    if version_match:
        _, _, patch = map(int, version_match.groups())
    else:
        raise ValueError("Invalid version format")

    app["version"] = version
    app["versionDate"] = fetched_data_latest["published_at"]

    description = fetched_data_latest["body"]
    description = re.sub("<[^<]+?>", "", description)  # Remove HTML tags
    description = description.replace(r"\*{2}", "").replace("-", "•").replace("`", '"')

    app["versionDescription"] = description
    app["downloadURL"] = next(
        (
            asset["browser_download_url"]
            for asset in fetched_data_latest["assets"]
            if asset["name"].endswith(".ipa")
        ),
        None,
    )
    app["size"] = next(
        (
            asset["size"]
            for asset in fetched_data_latest["assets"]
            if asset["browser_download_url"] == app["downloadURL"]
        ),
        None,
    )

    purge_old_news(data, fetched_versions)

    if "news" not in data:
        data["news"] = []

    news_identifier = f"release-{latest_version}"
    if not any(item["identifier"] == news_identifier for item in data["news"]):
        formatted_date = datetime.strptime(
            fetched_data_latest["published_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d %b")
        
        # Determine caption and imageURL based on patch number
        if patch == 0:
            caption = "Major update for Mangayomi is here!"
            image_url = "https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/images/news/available_black.webp"
        else:
            caption = "Update for Mangayomi now available!"
            image_url = "https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/images/news/update_black.webp"
        
        news_entry = {
            "appID": "com.kodjodevf.mangayomi",
            "title": f"{latest_version} - {formatted_date}",
            "identifier": news_identifier,
            "caption": caption,
            "date": fetched_data_latest["published_at"],
            "tintColor": "71717A",
            "imageURL": image_url,
            "notify": True,
            "url": f"https://github.com/kodjodevf/mangayomi/releases/tag/{tag}",
        }
        data["news"].append(news_entry)


    news_identifier = f"release-{latest_version}"
    if not any(item["identifier"] == news_identifier for item in data["news"]):
        formatted_date = datetime.strptime(
            fetched_data_latest["published_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d %b")
        news_entry = {
            "appID": "com.kodjodevf.mangayomi",
            "title": f"{latest_version} - {formatted_date}",
            "identifier": news_identifier,
            "caption": "Update for Mangayomi now available!",
            "date": fetched_data_latest["published_at"],
            "tintColor": "71717A",
            "imageURL": "https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/images/news/update_black.webp",
            "notify": True,
            "url": f"https://github.com/kodjodevf/mangayomi/releases/tag/{tag}",
        }
        data["news"].append(news_entry)

    with open(json_file, "w") as file:
        json.dump(data, file, indent=2)


def main():
    repo_url = "kodjodevf/mangayomi"
    json_file = "apps.json"

    fetched_data_all = fetch_all_releases(repo_url)
    fetched_data_latest = fetch_latest_release(repo_url)
    update_json_file(json_file, fetched_data_all, fetched_data_latest)


if __name__ == "__main__":
    main()
