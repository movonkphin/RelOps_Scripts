# RelOps_Scripts
Just a bunch of scripts used for some RelOps things.\
\
\
query_opsgenie_services - This looks at and lists the services we currently have in OpsGenie, outputting the results to a text file.\
\
This requires the following external python modules: 

requests\
json
\
\
query_statuspage_components - This looks at and lists the components we currently have in StatusPage, listing the current component group, name, and operational state. Outputting the results to a text file.\
\
This requires the following external python modules: 

requests\
json\
datetime
\
\
incident_reporting - This pulls a list of incidents that have been logged on statuspage, giving the ID, the data/time when the incident was opened, its current status and which components and component groups it was logged against. 
\
This requires the following external python modules: 

requests\
csv
\
\
reset_all_user_subs - this iterates through each user, defaulting their component email subscriptions to be empty, which statuspage treats as a hard reset and signing them up to all component subscriptions. This is useful because when a user is subscribed to all compnents if we add any new components statuspage auto enrolls them into subscribing to it. 
\
This requires the following external python modules: 

requests\
json\
time
\
\
histo - this generates a hustrogram of how many users are subscribed to each form of update, email, SMS, etc. 
\
This requires the following external python modules: 

requests\
matplotlib.pyplot
