#!/bin/bash

PYTHON="python3"
MY_TITLE="Requ"

function requ() {
  flags=$1
  if [ "$flags" = "-i" ]; then
    # Updating pip
    $2 -m pip install --upgrade pip
    # Install all modules via pip
    $2 -m pip install -r requirements.txt
    clear
  elif [ "$flags" = "-c" ]; then
    echo """
      If you want to help us or advise or correct our code,
      you can contact us via email: requiepmail@gmail.com.
      You can also write to the form on our website or
      contribute on GitHub. For more information, please
      visit the creator's GitHub profile.
    """
  elif [ "$flags" = "-h" ]; then
    echo """
      Application help menu: requ-im -
          example:
            requ <FLAG> <PYTHON_INTERPRETER>
          options:
              :args: - [
                '-i' - installation
                '-h' - help
                '-c' - contribution
                '<path>' - launch editor with specified path
              ]
          information:
              :links: - [
                'GitHub' - https://github.com/requiep/requ-im
              ]
          LICENSE - Apache License 2.0 /
              https://github.com/requiep/requ-im/blob/main/LICENSE
          AUTHOR - Requiep /
              https://github.com/requiep/
    """
  else
     echo -e '\033]2;'$MY_TITLE'\007'
     $PYTHON setup.py $flags
  fi
}
