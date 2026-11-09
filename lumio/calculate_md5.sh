#!/bin/bash
BUCKET=$1
rclone md5sum lumio:${BUCKET} --download >${BUCKET}.md5
