docker build -t tripentregas .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 736175842379.dkr.ecr.us-east-1.amazonaws.com
docker tag tripentregas 736175842379.dkr.ecr.us-east-1.amazonaws.com/tripentregas
docker push 736175842379.dkr.ecr.us-east-1.amazonaws.com/tripentregas