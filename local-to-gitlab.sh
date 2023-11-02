#!/bin/bash

# Create a new local repository
mkdir local-repo-from-script
cd local-repo-from-script
git init

# Create a new file for testing purposes
touch ardit.txt
echo "Created local repository" > ardit.txt

# Stage all of your changes
git add .

# Commit your changes with a message
git commit -m "Create local repository for script"

# Create a new remote repository on GitLab
git remote add origin https://gitlab.com/arditxharri/local-repo-from-script.git

git branch -M main

# Push your local repository to the remote GitLab repository
git push -uf origin main