#!/bin/bash

function requ() {
  flags=$1
  if [ "$flags" = "-i" ]; then
    echo """
      Installing
    """
  elif [ "$flags" = "-c" ]; then
    echo """
      If you want to help us or advise or correct our code,
      you can contact us by mail: requiepmail@gmail.com you
      can also write to the form on our website, you can also
      send it to github or see more information in the creator's
      github profile.
    """
  elif [ "$flags" = "-h" ]; then
    echo """
      Application help menu: requ-im -
          options:
              :args: - [
                '-i' - installing
                '-h' - help
                '-c' - contributing
                '<path>' - launch editor with far path
              ]
          information:
              :links: - [
                'github' - https://github.com/requiep/requ-im
              ]
          LICENSE - Apache License 2.0 /
              https://github.com/requiep/requ-im/blob/main/LICENSE
          AUTHOR - Requiep /
              https://github.com/requiep/
    """
  else
    python setup.py $flags
  fi
}