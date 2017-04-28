library(ggplot2)
library(ggmap)
library(extrafont)
library(scales)
library(data.table)
library(stringr)
library(treemap)

theme_set(theme_gray(base_family = "NanumGothicOTF"))

fitbit <- read.csv("/Users/jegalsumin/Documents/Data Science/Data set/fitbit/fitbit_cleaned.csv")
one_weeks <- read.csv("/Users/jegalsumin/Documents/Data Science/Data set/fitbit/one_weeks.csv")
fitbit_df <- read.csv("/Users/jegalsumin/Documents/Data Science/Data set/fitbit/fitbit_df.csv")

#mod sleep
sleep_df_heatmap <- ggplot(fitbit_df, aes(y=as.character(weekday), x=as.character(week))) +
  geom_tile(aes(fill=sleep)) +
  scale_fill_gradient(name='Usage count', low='white', high='brown') +
  xlab("sleep") +
  theme(axis.title.y = element_blank()) + 
  scale_x_discrete(breaks = c("13","14","15","16"),
                   labels = c("Mar 3rd","Mar 4rd","Apr 1rd","Apr 2rd")) +
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
sleep_df_heatmap

step_heatmap <- ggplot(fitbit, aes(y=as.character(weekday), x=as.character(week))) +
  geom_tile(aes(fill=steps)) +
  scale_fill_gradient(name='Usage count', low='white', high='green') +
  xlab("steps") +
  theme(axis.title.y = element_blank()) + 
  scale_x_discrete(breaks = c("13","14","15","16"),
                   labels = c("Mar 3rd","Mar 4rd","Apr 1rd","Apr 2rd")) +
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
step_heatmap

hearts_heatmap <- ggplot(fitbit, aes(y=as.character(weekday), x=week)) +
  geom_tile(aes(fill=hearts)) +
  scale_fill_gradient(name='Usage count', low='white', high='pink') +
  xlab("hearts") +
  theme(axis.title.y = element_blank()) + 
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
hearts_heatmap

sleep_heatmap <- ggplot(fitbit, aes(y=as.character(weekday), x=week)) +
  geom_tile(aes(fill=sleep)) +
  scale_fill_gradient(name='Usage count', low='white', high='brown') +
  xlab("sleep") +
  theme(axis.title.y = element_blank()) + 
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                  labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
sleep_heatmap

one_week_heatmap <- ggplot(one_weeks, aes(x=time, y=as.character(weekday))) +
  geom_tile(aes(fill=steps)) +
  scale_fill_gradient(name='Usage count', low='white', high='brown') +
  xlab("sleep") +
  theme(axis.title.y = element_blank()) + 
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
one_week_heatmap

treemap(fitbit_df,
        index=c("week", "weekday_name"),
        vSize=c("hearts"),
        title.legend="count of steps",
        vColor="steps",
        type="value")
