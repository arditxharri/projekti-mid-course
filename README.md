*** Task 1: Create a new repo in Bitbucket cloud with a simple "hello from Bitbucket" script (3 points)**

1. Log in to your Bitbucket account.
2. Click on the "+" sign to create a new repository.
3. Follow the steps to create a new repository, give it a name, and select your repository settings.
4. Once the repository is created, add a simple "hello from Bitbucket" script and commit it.

**Task 2: Create a new repo in GitHub with a simple "hello from GH" script (3 points)**

1. Log in to your GitHub account.
2. Click on the "+" sign in the upper right corner to create a new repository.
3. Follow the steps to create a new repository on GitHub, give it a name, and configure its settings.
4. Once the repository is created, add a simple "hello from GitHub" script and commit it.

**Task 3: Create a script to mirror clone old repos to new in GitLab (9 points)**
1. Run the python script named: mirror-repo.py: python3 mirror-repos.py (Note: you need python3 installed)
2. Insert source GIT Repository URL
3. Insert Destination GIT Repository URL
4. The script will ask you to authenticate to the destination Git Repositoy
5. Enter Username & Password
6. Done

**Task 4: Create a local repository for the script and push it to a remote repo in GitLab (3 points)**
1. Set up a remote repository in GitLab.
2. Give execute permission to the script.
    chmod +x local-to-gitlab.sh
3. Change the repo and the url to your gitlab repo/url name
5. Run the script

**Task 5: Create a script to check source and target repos and synchronize them if there are new changes (6 points)**
This script will involve checking for changes in the source and target repositories and synchronizing them as needed. You can use Git hooks or a custom script to automate this.
1. Check for changes in the source repository.
2. If changes are detected, fetch the changes and merge or rebase them.
3. Push the changes to the target repository if necessary.

**Task 6: Create a container from the script from goal 5 and run it locally using Docker run (8 points)**
1. Create a Dockerfile for your synchronization script.
2. Build a Docker image from the Dockerfile.
    docker build -t [image-name][tag] .
    ex: docker build -t mirror-repos:v1
4. Run the Docker container using the `docker run` command.
    docker run [image-name][tag]
    ex: docker run mirror-repos:v1

**Task 7: Run the container on Minikube locally (8 points)**
1. Install and set up Minikube.
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    minikube start --driver=docker

2. Create a Kubernetes Deployment or Pod configuration that uses your Docker image. (yaml file)
3. Deploy the configuration to Minikube using `kubectl apply`.
    kubectl apply -f mirror-git-app.yaml
4. Monitor the status of the deployment and access the running container.
    kubectl get pods
