#!/bin/bash

#===============================================================================
# search_labnotebook.sh
#   Wrapper for egrep to search all Markdown files in lab notebook category.
#   Will return name of file and line where search term occurs.
#   Case-sensitive, will highlight matching term. 
#   Usage: search_labnotebook.sh [search term]
#===============================================================================

for FILE in $( ls content/lab-notebook/*.md ); 
do
    OUTPUT=$( cat $FILE | egrep -wi --color=auto "$*" )
    if [ -n "$OUTPUT" ];
    then
        echo $FILE
        echo $OUTPUT
    fi
done
