# Tripentregas REST API

1. install pip dependencies `pip install -r requirements.txt`.
2. For linux do, execute the following commands before step 3:

   1. `sudo apt install python3-dev build-essential`
   2. `sudo apt install libssl1.1`
   3. `sudo apt install libssl1.1=1.1.1f-1ubuntu2`
   4. `sudo apt install libssl-dev`
   5. `sudo apt-get install libmysqlclient-dev`
   6. `sudo apt-get install python3-tk`

3. For Mac OS do:

   1. `brew install mysql`

4. Set up .env.environment_name file
5. Run server with :
   - if youre on linux run`export PYTHON_ENV=dev && python manage.py runserver`
   - if youre on windows run:
     - `$env:PYTHON_ENV = 'dev'`
     - `python manage.py runserver`

## Docker set up

### Build

1. Build the docker image with: `docker build -t tripentregas .`

2. Test docker image with: `docker run --name tripentregas -p 8000:8000 --env-file .env.docker tripentregas`

### Push image to ECR

if youre on linux machine be sure to create gpg keys with: `gpg --generate-key` copy the pub hex and then `pass init _hexkey_`

1. Login to ECR with: `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 736175842379.dkr.ecr.us-east-1.amazonaws.com`

2. Create a repository in ECR and get its URI

3. Tag local image: `docker tag tripentregas 736175842379.dkr.ecr.us-east-1.amazonaws.com/tripentregas`

4. Push image with `docker push 736175842379.dkr.ecr.us-east-1.amazonaws.com/tripentregas`

5. Set up ECS Tasks
