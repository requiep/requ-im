#!/bin/bash

function requ() {
  flags=$1
  if [ "$flags" = "-i" ]; then
    echo """
      Installing
    """
  elif [ "$flags" = "-c" ]; then
    echo """
      C
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