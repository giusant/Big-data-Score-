d <- read.csv("cs-training_v2.csv") # carga de dados
df= data.frame (d)
set.seed(33)      # Definir semente aleatoriedade
va <- sample(150000) # Geração vetor aleatório

treino <- d[va[1:90000],]
teste  <- d[va[90001:150000],]
View(treino)
# Regressão Logistica
treino$SeriousDlqin2yrs_f <-  as.factor(treino$SeriousDlqin2yrs)

mod <- glm(SeriousDlqin2yrs_f~age, data=treino, family=binomial(link="logit"))

summary(mod)
predicted <- predict(mod, teste, type="response")

View(predicted )