#!/bin/bash
# This script gets the latest files on |USER|/|REPOSITORY|.

# set -xeu # for debug
USER="dbgroup-nagoya-u"
REPOSITORY="paper-lintrules"

ESC=$(printf '\033')
RED="${ESC}[31m"
GREEN="${ESC}[32m"
BLUE="${ESC}[34m"

# Check if commands exist.
if ! command -v wget &>/dev/null;
then
  printf "wget could not be found.\n"
  printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install wget'
  exit 1
fi

if ! command -v unzip &>/dev/null;
then
  printf "unzip could not be found.\n"
  printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install unzip'
  exit 1
fi

# Download from the latest commit on main branch.
latest_file_url="https://github.com/${USER}/${REPOSITORY}/archive/main.zip"
wget -q ${latest_file_url} --show-progress
latest_file="main.zip"

# Unzip files in |unzip_dir|.
unzip_dir="${REPOSITORY}-main"
unzip -qq ${latest_file}
rm ${latest_file}

# Sync files.
(
  pushd ${unzip_dir} > /dev/null
  dirarray=($(find . -mindepth 1 -type d))

  popd > /dev/null
  for dirname in ${dirarray[@]}; do
    mkdir -p ${dirname}
  done

  pushd ${unzip_dir} > /dev/null
  # TODO: Clarify exclude file and directory.
  for file in $(find . -type d \( -path './.github/ISSUE_TEMPLATE' -o -path './dir' \) -prune -false -o -type f -not -name 'README.md' -not -name '**.tex' -not -name 'update.bash' -not -name 'dict_check.py');
  do
    diff -N ${file} ../${file} > /dev/null
    if [ $? -ne 0 ] ;
    then
      # TODO: Add merge option. Currenctly, it makes local script updated forcely.
      mv ${file} ../${file}
      printf "${BLUE}${file}${ESC}[m %s\n" 'has been updated.'
    fi
  done
)
rm -rf ${unzip_dir}

# TODO: Error handling
printf "${GREEN}%s${ESC}[m\n" 'Update paper-lintrules settings successfully!'
