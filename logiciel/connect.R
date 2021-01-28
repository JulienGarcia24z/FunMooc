library(mongolite)
library(tidyverse)
library(lubridate)

# Scripte R contenant les identifiants à placer avec le scripte d'éxecution
source("file.R") 

# Connexion dans la bdd
url_path = paste("mongodb://",user,":",mdp,"@127.0.0.1:27017/admin",sep = "")
mongo_db = mongo(collection = "groupe2",db = "Datalab2020",url = url_path,verbose = TRUE)

# Requête qui affiche le nombre d'utilisateurs
df_data = mongo_db$aggregate('[{"$group": {"_id": "$content.created_at"}}]')

df2 = data.frame(df_data)
df2 = df2 %>%
      mutate(new_date = format(as.Date(X_id),"%Y-%m"), 
             heure = hour(as.Date(X_id)))
#ymd(as.Date(df2$X_id))

graph = df2 %>%
  group_by(new_date ) %>%
  count() %>%
  ggplot(aes(x=new_date, y=n) ) + geom_point(size= 3, color="red")+
  ggtitle("Evolution des messages postés") +
  xlab("Temps") + ylab("Nombre de messages")

print(graph)

