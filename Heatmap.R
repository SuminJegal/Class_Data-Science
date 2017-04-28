library(ggplot2)
library(ggmap)
library(extrafont)
library(scales)
library(data.table)
library(stringr)

theme_set(theme_gray(base_family = "NanumGothicOTF"))

tashu <- read.csv("/Users/jegalsumin/Documents/Data Science/Data set/tashu/tashu_cleaned.csv")

# Heatmap
tashu_2015_8_df <- subset(tashu, subset=(year==2015 & month==8))

day_hour_df <- data.frame(table(tashu_2015_8_df$hour, tashu_2015_8_df$day)) #hour와day의pair의 개수를 세줌
colnames(day_hour_df) <- c("hour", "day", "Freq")
#names(day_hour_df)[1] = "hour"
#names(day_hour_df)[2] = "day"

heatmap <- ggplot(day_hour_df, aes(x=hour, y=day)) +
  geom_tile(aes(fill=Freq)) +
  scale_fill_gradient(name='2015 / 8 day per time heatmap', low='white', high='red')
heatmap


tashu_2015_df <- subset(tashu, subset=(year==2015))

week_day_df <- data.frame(table(tashu_2015_df$weekday, tashu_2015_df$week))
colnames(week_day_df) <- c("Weekday", "Week", "Freq")
week_day_df$month <- as.integer(as.numeric(week_day_df$Week) / 4.5 + 1)
wheatmap <- ggplot(week_day_df, aes(y=Weekday, x=Week)) +
  geom_tile(aes(fill=Freq)) +
  scale_fill_gradient(name='Usage count', low='white', high='pink') +
  scale_x_discrete(breaks = c("2","6","10","15","20","24","29","34","39","44","48","53"),
                   labels = c("Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec")) +
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")) +
  xlab("2015") +
  theme(axis.title.y = element_blank())
wheatmap