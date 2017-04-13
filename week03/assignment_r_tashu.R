setwd("/Users/jegalsumin/Documents/Data Science/Class_Data-Science/week03")

library(data.table)
library(ggplot2)
library(plyr)
library(ggmap)

#데이터 읽어오기
tashu_csv <- read.csv("tashu.csv")
station_csv <- read.csv("station.csv")

rent_count <- count(tashu_csv, c('RENT_STATION'))
return_count <- count(tashu_csv, c('RETURN_STATION'))

#데이터 합치기
names(rent_count)[names(rent_count) == "RENT_STATION"] <- c("station")
names(return_count)[names(return_count) == "RETURN_STATION"] <- c("station")

total_count <- merge(rent_count, return_count, all=TRUE)
total_count <- aggregate(freq~station,total_count,sum)
ggplot(data=total_count, aes(x=station, y=freq, fill=station)) + 
  geom_bar(stat="identity")

#top10
top10 <- (arrange(total_count,desc(freq)))[1:10,]

#과제 1
top10$station<-as.factor(top10$station)
bar_top10 <- ggplot(data=top10, aes(x=station, y=freq, fill=station)) + 
  geom_bar(stat="identity") + 
  theme_minimal() + 
  geom_text(aes(label=freq), vjust=1.6, color="white",position = position_dodge(0.9), size=1.7) + 
  scale_y_continuous(labels = scales::comma)
bar_top10

#과제 2
names(total_count)[names(total_count) == "station"] <- c("키오스크번호")
total_station <- merge(x = total_count, y = station_csv, by = '키오스크번호')
names(total_count)[names(total_count) == "키오스크번호"] <- c("station")

coordinates <- data.frame(do.call('rbind', strsplit(as.character(total_station$좌표), split = ',',fixed = TRUE)))
coordinates <- rename(coordinates, c(X1 = "lat", X2 = "lon"))
total_station <- cbind(total_station,coordinates)

#total_station에서 lon,lat int나 num으로 바꾸고도 해보자
daejon_gc <-  geocode('Daejon')
daejon_cent <- as.numeric(daejon_gc)
dm <- 
  ggmap(get_googlemap(center=daejon_cent, scale = 1, maptype = "roadmap", zoom=13)) + 
  geom_point(aes(x = as.numeric(as.character(lon)), y = as.numeric(as.character(lat))), colour = "purple", alpha = .5, size = total_station$freq*0.000025, data = total_station)
dm

#과제 3
trace <- na.omit(tashu_csv)
trace <- count(trace, c('RENT_STATION','RETURN_STATION'))
trace <- (arrange(trace,desc(freq)))[1:20,]
trace_discrete <- trace
trace_discrete$RENT_STATION <- as.factor(trace$RENT_STATION)
trace_discrete$RETURN_STATION <- as.factor(trace$RETURN_STATION)
names(trace_discrete)[names(trace_discrete) == "RENT_STATION"] <- c("Rent_Station")
names(trace_discrete)[names(trace_discrete) == "RETURN_STATION"] <- c("Return_Station")
names(trace_discrete)[names(trace_discrete) == "freq"] <- c("Frequency")
point_trace_discrete <- ggplot(data=trace_discrete, aes(x=Rent_Station, y=Return_Station, size = Frequency)) + 
  geom_point(colour='#F183CA') + 
  coord_fixed(ratio = 3/4)
point_trace_discrete
point_trace <- ggplot(data=trace, aes(x=RENT_STATION, y=RETURN_STATION, size = freq)) + 
  geom_point(colour="#86E2D5") +
  scale_x_continuous(breaks=seq(0, max(trace$RENT_STATION), 10)) + 
  scale_y_continuous(breaks=seq(0, max(trace$RETURN_STATION), 10)) +
  coord_fixed(ratio = 3/4)
point_trace