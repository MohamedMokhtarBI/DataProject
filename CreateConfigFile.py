import configparser  

config=configparser.ConfigParser()
#config.read('C:/Users/Mokhtar/Desktop/DataProject/DataProject/configfile.ini')

#Create GCP Account Section
config.add_section('GCP_ACCOUNT')
config.set('GCP_ACCOUNT','USERNAME','mokhtarmouhamed24@gmail.com')
config.set('GCP_ACCOUNT','PASSWORD','ConsultantBI2474089124740891')

#Create database Section 
config.add_section('DATABASE')
config.set('DATABASE','USERNAME','root')
config.set('DATABASE','PASSWORD','root')
config.set('DATABASE','SERVER','LOCALHOST')
config.set('DATABASE','DATABASE','DATAPROJECT')


#Create Data source
config.add_section('DATA')
config.set('DATA','SOURCE','C:/Users/Mokhtar/Desktop/DataProject/DataProject/stack-overflow-developer-survey-2022/survey_results_public.csv')

with open(r"C:/Users/Mokhtar/Desktop/DataProject/DataProject/configfile.ini","w") as configfile:
   config.write(configfile)


a=config["DATA"]["SOURCE"]
print(a)