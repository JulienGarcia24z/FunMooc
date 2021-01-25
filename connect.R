library(mongolite)
library("tidyverse")

# Scripte R contenant les identifiants à placer avec le scripte d'éxecution
source("file.R") 

# Connexion dans la bdd de mongodb voulu après avoir effectuer la connexion ssh avec le port 27017 et la connexion à mongodb depuis le terminal
url_path = paste("mongodb://",user,":",mdp,"@127.0.0.1:27017/admin",sep = "")
mongo_db = mongo(collection = "groupe2",db = "Datalab2020",url = url_path,verbose = TRUE)

# Requête nosql éffectuer dans la bdd ou l'on s'est connecter
print(mongo_db$find())
numberMsg = mongo_db$aggregate('[
    {
        "$unwind": {
            "path": "$content.endorsed_responses"        }
    }, {
        "$group": {
            "_id": "$content.endorsed_responses.username", 
            "number": {
                "$sum": 1
            }
        }
    }, {
        "$sort": {
            "number": -1
        }
    }
]')

df = data.frame(numberMsg)

new = select(df,number) %>%
      group_by(number)%>%
      count(number)
  
