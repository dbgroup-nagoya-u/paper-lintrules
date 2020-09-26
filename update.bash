#!/bin/bash
# set -xeu # for debug
TAR_DIR="tmp_for_textlint"
USER="dbgroup-nagoya-u"
REPOSITORY="test-public-textlint-settings"


# Check if commands exist.
ESC=$(printf '\033')
RED="${ESC}[31m"
if ! command -v wget &> /dev/null
then
    echo "wget could not be found."
    printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install wget'
    exit
fi
if ! command -v jq &> /dev/null
then
    echo "jq could not be found."
    printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install jq'
    exit
fi

# Download from the latest tags
curl --silent https://api.github.com/repos/${USER}/${REPOSITORY}/tags > res.json
tag_latest=$(jq '.[] | .name' res.json | sort -rV | head -n1 | sed 's/"//g')
latest_file="${tag_latest}.tar.gz"
rm res.json

repository_url="https://github.com/${USER}/${REPOSITORY}"
wget ${repository_url}/archive/${latest_file}

# Untar files in |TAR_DIR|
mkdir ${TAR_DIR} && tar -zxvf ${latest_file} -C ${TAR_DIR} --strip-components 1
rm ${latest_file}

(
  # Sync files
  pushd ${TAR_DIR}
  dirarray=($(find . -mindepth 1 -type d))

  popd
  for dirname in ${dirarray[@]}; do
    mkdir -p ${dirname}
  done

  pushd ${TAR_DIR}
  # TODO: Clarify exclude file and directory. It'd be broken when *.md files are needed.
  for file in $(find . -type d \( -path './.git' -o -path './dir' \) -prune -false -o -type f -not -name '**.md' -not -name 'paper.txt' -not -name 'update.bash'); do
    mv ${file} ../${file}
  done
)
rm -rf ${TAR_DIR}

# TODO: Error handling
ESC=$(printf '\033')
GREEN="${ESC}[32m"
printf "${GREEN}%s${ESC}[m\n" 'Update paper-lint settings successfully!'
