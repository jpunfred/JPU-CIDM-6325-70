Jordan Unfred

E-Comm & Web Dev (CIDM-6325-70)

# Update 12/5/2023
- Deployment Error

I was unsuccessful in deploying the project to the EC2 Ubuntu instance on AWS. I have attached screenshots (Figures) of the project running on repl.it. Here is a list of the things I attempted:

.  Started a new Amazon EC2 Instance
. sudo apt-get update - this will update all the pre installed packages for the ubuntu image that is on the EC2 instance

. sudo apt-get upgrade - this will make sure all packages are on their latest version

.  git clone  https://github.com/jpunfred/JPU-CIDM-6325-70.git - this will get the actual project files onto the EC2 instance for deployment 

. download django using pip - this will give us the files of django that are rewuired to run the app 

. sudo apt install python3-pip -y - this will install pip, a package manager for python

. pip install django - this command will actually install django to the EC2 instance 

. cd into /JPU-CIDM-6325-70/Final Project/Advising-Project-v4 - this will bring us directly to the directory that we need to be in to run the application

. run python3 manage.py makemigrations - this will create the migration file

.run python3 manage.py migrate - this will actually apply the migrations

. add a custom inbound rule to allow traffic to the port that the app is running on (8000) - we do this in the security group settings of the instance on the AWS
	GUI to allow traffic to port 8000
 
.  run python3 manage.py runserver 0.0.0.0:8000 - this will then run the server that we can connect to via instance_ip:8000/advinterface, however this returns null

. install gunicorn with pip install gunicorn - trying to run the .wsgi of the app with gunicorn to see if I can access the deployed app

. run gunicorn advinterface.wsgi - this will allow us to hopefully get into the application however, this attempt also returns null

# Final Project Requested Information

Submit the following materials to this dropbox:

1. The URL to your site: https://junfred.com
2. A username and password for me access your VPS with sudo access

 Sign in [Here](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fus-east-2.console.aws.amazon.com%2Fec2%2Fhome%3Fregion%3Dus-east-2%26state%3DhashArgs%2523ConnectToInstance%253AinstanceId%253Di-04dc466cb6bb7606e%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fec2&forceMobileApp=0&code_challenge=YGvjSbVLLLloO1JWx0dt2Bb8ObXC-d4cdqMlqUFxvrY&code_challenge_method=SHA-256)
 Select Root User
 Root user email address: [Jordan.unfred258@yahoo.com](mailto:Jordan.unfred258@yahoo.com)
 Password: R3con258!
3. A username and password for me to sign in to the admin area of your Django site (NOT THE SAME ACCOUNT AS ABOVE)

 Username: juadmin
 Password: djangomaster258


4. A link and access to your Github Repository

[https://github.com/jpunfred/JPU-CIDM-6325-70/tree/main/Final%20Project](https://github.com/jpunfred/JPU-CIDM-6325-70/tree/main/Final%20Project)


5. The Zip up the FULL CONTENTS of your source code and submit that ZIP file here
