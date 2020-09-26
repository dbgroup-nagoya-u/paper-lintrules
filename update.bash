#!/bin/bash
# set -xeu # for debug
TAR_DIR="tmp_for_textlint"
TAR_FILE="v0.1.tar.gz"
REPOSITORY_URL="https://github.com/dbgroup-nagoya-u/test-public-textlint-settings"

# TODO: TAR_FILEをここで指定せず、GitHubのAPIを使って最新版を持ってくるようにする
# TODO: GitHub Actionsを使ってリポジトリを更新するたびにタグが付くと嬉しい
wget ${REPOSITORY_URL}/archive/${TAR_FILE}

mkdir ${TAR_DIR} && tar -zxvf ${TAR_FILE} -C ${TAR_DIR} --strip-components 1

(
  pushd ${TAR_DIR}
  dirarray=($(find . -mindepth 1 -type d))

  popd
  for dirname in ${dirarray[@]}; do
    mkdir -p ${dirname}
  done

  pushd ${TAR_DIR}
  for file in $(find . -type d \( -path './.git' -o -path './dir' \) -prune -false -o -type f -not -name 'README.md' -not -name 'paper.txt'); do
    mv ${file} ../${file}
  done
)
rm ${TAR_FILE}
rm -rf ${TAR_DIR}

ESC=$(printf '\033')
GREEN="${ESC}[32m"
printf "${GREEN}%s${ESC}[m\n" 'Update paper-lint settings successfully!'
