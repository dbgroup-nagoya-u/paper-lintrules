#!/bin/bash
# This script gets the latest files on |USER|/|REPOSITORY|.

# set -xeu # for debug
USER="dbgroup-nagoya-u"
REPOSITORY="test-public-textlint-settings"

# Check if commands exist.
ESC=$(printf '\033')
RED="${ESC}[31m"
if ! command -v wget &>/dev/null; then
  echo "wget could not be found."
  printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install wget'
  exit 1
fi
if ! command -v jq &>/dev/null; then
  echo "jq could not be found."
  printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install jq'
  exit 1
fi

# Download from the latest commit on master branch.
latest_file_url="https://github.com/${USER}/${REPOSITORY}/archive/master.zip"
wget ${latest_file_url}
latest_file="master.zip"

# Unzip files in |unzip_dir|.
unzip_dir="${REPOSITORY}-master"
unzip ${latest_file}
rm ${latest_file}

# Sync files.
(
  pushd ${unzip_dir}
  dirarray=($(find . -mindepth 1 -type d))

  popd
  for dirname in ${dirarray[@]}; do
    mkdir -p ${dirname}
  done

  pushd ${unzip_dir}
  for file in $(find . -type d \( -path './.github/ISSUE_TEMPLATE' -o -path './dir' \) -prune -false -o -type f -not -name 'README.md' -not -name 'paper.txt' -not -name 'update.bash'); do
    mv ${file} ../${file}
  done
)
rm -rf ${unzip_dir}

# TODO: Error handling
ESC=$(printf '\033')
GREEN="${ESC}[32m"
printf "${GREEN}%s${ESC}[m\n" 'Update paper-lint settings successfully!'
