rm(list=ls())

library(data.table)
library(ggplot2)
library(plyr)
library(ggmap)
library(extrafont)
library(scales)
library(data.table)
library(stringr)
library(grid)
library(plotly)

theme_set(theme_gray(base_family = "NanumGothicOTF"))

tashu_csv <- read.csv('/Users/jegalsumin/Documents/Data Science/Data set/tashu/tashu_cleaned.csv')
station_csv <- read.csv('/Users/jegalsumin/Documents/Data Science/Data set/test/1/station.csv')

rent_count <- count(tashu_csv, c('date'))
rent_graph <- ggplot(data=rent_count, aes(x=date, y=freq, group=1)) + 
  geom_line(colour="blue") + 
  scale_x_discrete(breaks = c("2013-06-01","2014-06-01","2015-06-01"),
                   labels = c("2013","2014","2015"))
rent_graph


tashu_group_sum <- count(tashu_csv, c('weekday','hour'))
heatmap <- ggplot(tashu_group_sum, aes(x=hour, y=as.character(weekday))) +
  geom_tile(aes(fill=freq)) +
  scale_fill_gradient(name='Usage count', low='white', high='pink') +
  xlab("freq") +
  theme(axis.title.y = element_blank()) + 
  scale_y_discrete(breaks = c("0","1","2","3","4","5","6"),
                   labels = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
heatmap



tashu_wed_total <- subset(tashu_csv, subset=(weekday==2 & (hour==7|hour==8|hour==18|hour==19)))
tashu_wed_morn <- subset(tashu_csv, subset=(weekday==2 & (hour==7|hour==8)))
tashu_wed_aft <- subset(tashu_csv, subset=(weekday==2 & (hour==18|hour==19)))

tashu_wed_morn <- count(tashu_wed_morn, c('RENT_STATION'))
tashu_wed_morn <- (arrange(tashu_wed_morn,desc(freq)))[1:5,]
tashu_wed_aft <- count(tashu_wed_aft, c('RENT_STATION'))
tashu_wed_aft <- (arrange(tashu_wed_aft,desc(freq)))[1:5,]

names(tashu_wed_morn)[names(tashu_wed_morn) == "RENT_STATION"] <- c("station")
names(tashu_wed_aft)[names(tashu_wed_aft) == "RENT_STATION"] <- c("station")
names(tashu_wed_morn)[names(tashu_wed_morn) == "station"] <- c("키오스크번호")
tashu_wed_morn <- merge(x = tashu_wed_morn, y = station_csv, by = '키오스크번호')
names(tashu_wed_morn)[names(tashu_wed_morn) == "키오스크번호"] <- c("station")
names(tashu_wed_aft)[names(tashu_wed_aft) == "station"] <- c("키오스크번호")
tashu_wed_aft <- merge(x = tashu_wed_aft, y = station_csv, by = '키오스크번호')
names(tashu_wed_aft)[names(tashu_wed_aft) == "키오스크번호"] <- c("station")

coordinates <- data.frame(do.call('rbind', strsplit(as.character(tashu_wed_morn$좌표), split = ',',fixed = TRUE)))
coordinates <- rename(coordinates, c(X1 = "lat", X2 = "lon"))
tashu_wed_morn <- cbind(tashu_wed_morn,coordinates)
coordinates <- data.frame(do.call('rbind', strsplit(as.character(tashu_wed_aft$좌표), split = ',',fixed = TRUE)))
coordinates <- rename(coordinates, c(X1 = "lat", X2 = "lon"))
tashu_wed_aft <- cbind(tashu_wed_aft,coordinates)

daejon_gc <-  geocode('Daejon')
daejon_cent <- as.numeric(daejon_gc)
dm <- 
  ggmap(get_googlemap(center=daejon_cent, scale = 1, maptype = "roadmap", zoom=13)) + 
  #geom_point(aes(x = as.numeric(as.character(lon)), y = as.numeric(as.character(lat))), colour = "purple", alpha = .5, size = tashu_wed_morn$freq*0.005, data = tashu_wed_morn)
  geom_point(aes(x = as.numeric(as.character(lon)), y = as.numeric(as.character(lat))), colour = "red", alpha = .5, size = tashu_wed_aft$freq*0.005, data = tashu_wed_aft)

dm


tashu_wed_total <- count(tashu_wed_total, c('RENT_STATION','RETURN_STATION'))
tashu_wed_total <- (arrange(tashu_wed_total,desc(freq)))[1:5,]
print(tashu_wed_total)



