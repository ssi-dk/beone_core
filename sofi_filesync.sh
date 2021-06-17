#!/bin/bash


# Transfer files from /opt/sofi/upload_dir to the nfs mount in the live environment
# This works around the inability to bind the nfs mount to a volume within the api container itself

set -Eeuo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/.env 

inotifywait -mrq -e modify,create $SOFI_UPLOAD_DIR | while read DIRECTORY EVENT FILE
do
   mv $SOFI_UPLOAD_DIR/* $BIFROST_UPLOAD_DIR/
done
