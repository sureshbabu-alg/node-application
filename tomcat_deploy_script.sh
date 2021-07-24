project_version=$(cat pom.xml | grep "version" | head -1 | awk '{print $1}' | sed "s/<version>//" | sed "s/<.*//")
mv /var/lib/jenkins/workspace/node-application/target/nodeapp-$project_version.war /var/lib/jenkins/workspace/node-application/target/webapp.war
scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/suresh.pem /var/lib/jenkins/workspace/node-application/target/webapp.war ec2-user@3.83.235.141:/opt/tomcat8/webapps/
